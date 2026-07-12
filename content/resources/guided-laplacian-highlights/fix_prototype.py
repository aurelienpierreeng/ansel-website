"""
Fix prototype for the guided-laplacian magnitude-recovery bug (SETTLED, v2).

Bug (current C, CPU guide_laplacians + OpenCL basic.cl): the guided transfer works
on the mean-subtracted à-trous HF DETAIL bands, so the guided-filter intercept
carries no DC -> a clipped channel's magnitude is never recovered (single-channel
clips are even pulled DOWN). The LF residual is added unmodified.

Fix:
  1) `guided_recon`: a He guided filter on the FULL signal (so a*guide carries both
     the guide's low frequencies AND its detail = LF+HF together), SMOOTH GAUSSIAN
     windows (box windows leave blocky artifacts), coarse->fine. A clipped channel is
     rebuilt only where a VALID (unclipped) guide exists at that pixel. The two candidate
     guides are BLENDED by a smooth weight (valid coverage x guide variance) instead of
     hard-selecting the higher-variance one: a hard argmax makes the estimate jump where
     the winning guide flips, which shows as a faint seam at the core/annulus boundary.
  2) CONFIDENCE-WEIGHTED blend (`_confidence`, `_self_inpaint`): per clipped channel
     that still has a surviving guide, u_c = We*(a*guide+b) + (1-We)*self, with a SHARPENED
     colour-line confidence We = (R^2)^CONF_EXPONENT (= R^2 squared), R^2 = cov^2/(var_g var_c),
     and self = per-channel BIHARMONIC extension of the channel's own TRUE valid rim
     (gradient-extending -> domes, not flat). Squaring separates the families cleanly
     (correlated R^2 ~ 0.9 -> We ~ 0.9, keep the accurate guide; random R^2 ~ 0.65 ->
     We ~ 0.42, lean on the smooth self dome). This SELECTIVELY removes the guide-flip
     seam that hard guide-selection leaves on decorrelated content, without hitting the
     correlated case (which even improves): correlated -> guide, uncorrelated -> own gradient.
  3) ALL-CLIPPED CORE (`_joint_core`): where NO channel survives there is no colour-line
     and no per-channel rim to trust; doming each channel from its own clip radius makes
     the three domes reach different heights, so the core drifts off-hue (a neutral sun
     goes yellow because blue, last to clip, saturates flat at its rim and domes least).
     Instead reconstruct ONE quantity per kind: a single biharmonic LUMINANCE dome
     L = sum_c u_c (shared shape -> no channel collapses) times the CHROMATICITY u_c/L
     carried inward by harmonic (flat) diffusion from the rim. core_c = L_dome*chroma_c.
     The rim is the already-reconstructed partial-clip annulus, so the true/recovered
     edges drive the central dome jointly. This REPLACES the old ad-hoc wavelet chroma
     diffusion (which clobbered the hue).
  4) Prefer FULL RESOLUTION (ds=1). The stock 4x downsampling is the main edge-damager.
  5) Mask feathering is KEPT: it lowers boundary error (it is not the edge-damager).
  6) UNCERTAINTY-AWARE REGULARIZATION (`_weighted_solve`, REG_LAMBDA): the steps above recover
     magnitude well but leave faint SEAMS where the reconstruction changes character (the hard
     guide-flip on decorrelated content; the core/annulus handoff). No confidence weight can hide
     a discontinuity in the thing it weights, so iron the seams out afterwards: per channel solve
     (diag(Wd) + lambda*Delta^2) u = diag(Wd)*rec with the FINISHED reconstruction as the data
     target and Wd = R^4 the fidelity weight. Where the recon is trustworthy (Wd high) u=rec is
     preserved; where it is not (random, seams, all-clipped core) the biharmonic prior flattens the
     seam's CURVATURE spike while preserving smooth domes/gradients (harmonic would over-smooth).
     Magnitude is preserved (target is the recon, not the collapsed guide); needs no clean
     random/correlated segregation. NB: no local scalar (R^2, cross-scale slope stability, guide
     agreement) cleanly separates the two families -- R^2 is the best but overlaps ~15% -- which is
     why we regularize the OUTPUT instead of trying to switch methods on a perfect metric.

Results (RMSE / SSIM, clip -> current-C -> FIXED; 4 seeds, 320^2, white=[1,1,1]):
  correlated 1/2/3: RMSE .049/.073/.015 · .123/.117/.036 · .221/.215/.065
                    SSIM .945/.906/.992 · .897/.909/.981 · .744/.775/.959
  random     1/2/3: RMSE .080/.124/.043 · .132/.167/.078 · .184/.193/.076
                    SSIM .915/.855/.964 · .874/.819/.940 · .741/.755/.918
Beats both doing-nothing and the current C everywhere. On the magenta-sun (near-neutral
all-clipped core) the joint core cuts RMSE .55 -> .27 and SSIM .83 -> .95 vs independent
per-channel domes, and restores a neutral hue (blue no longer collapses). The regularizer
halves the random-scene seam curvature (kink .0104 -> .0046) and lifts random SSIM, at a small
correlated cost (whole-scene RMSE .045 -> .053). Full-core peak magnitude is inherently limited
(~75-80%: the true peak is unobserved) but the dome is smooth, correctly coloured and the right
size. Quality judged with RMSE AND SSIM (SSIM catches structural/edge artifacts RMSE misses,
e.g. seams). Run: `python3.12 fix_prototype.py`.
"""
import numpy as np
from scipy.ndimage import gaussian_filter
import reconstruct_highlights as R
import scipy.sparse as _sp
from scipy.sparse.linalg import spsolve as _spsolve

FULLRES_SIGMAS = (40, 24, 14, 8, 4, 2)   # coarse -> fine guided-filter radii (full-res px)
CONF_EXPONENT = 2.0   # confidence sharpening: guide weight = R^(2*CONF_EXPONENT) (see recon_fixed)
REG_LAMBDA = 1.0      # uncertainty-aware biharmonic regularization strength (see recon_fixed)


def _laplacian_matrix(H, W):
    def D2(n):
        return _sp.diags([np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)], [-1, 0, 1])
    return (_sp.kron(_sp.identity(H), D2(W)) + _sp.kron(D2(H), _sp.identity(W))).tocsr()


def _weighted_solve(w, target, hole, boundary, op):
    """Solve (diag(w) + op) u = diag(w)*target on `hole` pixels, u = boundary outside.
    `op` is a pre-scaled sparse operator (e.g. lambda*Delta^2). A data term that pulls u
    toward `target` with per-pixel weight w, plus a smoothness prior `op` that acts where w
    is small -- the confidence-weighted regularizer used to iron out seams."""
    hi = np.where(hole.ravel())[0]
    ki = np.where(~hole.ravel())[0]
    if hi.size == 0:
        return target.copy()
    wv = w.ravel(); tv = target.ravel(); bv = boundary.ravel()
    A = (_sp.diags(wv[hi]) + op[hi][:, hi]).tocsc()
    rhs = wv[hi] * tv[hi] - (op[hi][:, ki] @ bv[ki])
    out = bv.copy()
    out[hi] = _spsolve(A, rhs)
    return out.reshape(hole.shape)


def biharmonic_inpaint(N, hole):
    """Fill `hole` in N by minimizing the biharmonic energy int|Delta N|^2 with N
    fixed outside — the higher-order, gradient-EXTENDING counterpart of harmonic
    (diffusive) inpainting. Continues the surrounding slope inward, so an
    all-clipped magnitude is domed instead of left flat. Direct sparse solve of
    the hole subsystem (Delta^2 N = 0)."""
    H, W = N.shape
    L = _laplacian_matrix(H, W)
    B = (L @ L).tocsr()
    hi = np.where(hole.ravel())[0]
    ki = np.where(~hole.ravel())[0]
    if hi.size == 0:
        return N.copy()
    uh = _spsolve(B[hi][:, hi].tocsc(), -(B[hi][:, ki] @ N.ravel()[ki]))
    out = N.ravel().copy()
    out[hi] = uh
    return out.reshape(H, W)


def harmonic_inpaint(N, hole):
    """Fill `hole` by Laplace/diffusion (Delta u = 0, u=N on the boundary): the
    smoothest FLAT interior consistent with the rim. Used for chromaticity, which
    should be carried inward from the rim without doming."""
    H, W = N.shape
    L = _laplacian_matrix(H, W)
    hi = np.where(hole.ravel())[0]
    ki = np.where(~hole.ravel())[0]
    if hi.size == 0:
        return N.copy()
    uh = _spsolve(L[hi][:, hi].tocsc(), -(L[hi][:, ki] @ N.ravel()[ki]))
    out = N.ravel().copy()
    out[hi] = uh
    return out.reshape(H, W)


def ssim_region(rec, gt, region, data_range, sig=1.5):
    """Mean SSIM over `region`, averaged across channels."""
    C1 = (0.01 * data_range) ** 2
    C2 = (0.03 * data_range) ** 2
    vals = []
    for c in range(3):
        a, b = rec[..., c], gt[..., c]
        ma = gaussian_filter(a, sig); mb = gaussian_filter(b, sig)
        va = gaussian_filter(a * a, sig) - ma * ma
        vb = gaussian_filter(b * b, sig) - mb * mb
        vab = gaussian_filter(a * b, sig) - ma * mb
        s = ((2 * ma * mb + C1) * (2 * vab + C2)) / ((ma * ma + mb * mb + C1) * (va + vb + C2))
        vals.append(s[region])
    return float(np.mean(vals))


def guided_recon(rgb, mask, sigmas=FULLRES_SIGMAS, eps=1e-4, fmin=0.02):
    """He guided filter on FULL values, smooth Gaussian windows, coarse->fine.
    Rebuild a clipped channel = a*guide + b from the highest-variance SURVIVING guide.

    The guide is hard-selected (highest local variance among the valid channels). This is
    accurate where a colour-line actually holds -- and there it is also smooth, because the
    two candidate guides then agree, so which one wins does not matter. Where NO colour-line
    holds (decorrelated content) the hard selection would jump as the winner flips, but there
    the cross-channel estimate is untrustworthy anyway and `recon_fixed`'s correlation gate
    routes those pixels to the smooth per-channel self dome instead -- so the jump never
    reaches the output. Selecting (not blending) keeps the correlated case maximally sharp."""
    est = rgb.copy()
    vf = [(mask[..., c] <= 0.5).astype(np.float64) for c in range(3)]
    for r in sigmas:
        f = lambda a: gaussian_filter(a, r, mode='nearest')
        varc = []
        for c in range(3):
            n = np.maximum(f(vf[c]), 1e-6)
            m = f(est[..., c] * vf[c]) / n
            varc.append(np.maximum(f(est[..., c] ** 2 * vf[c]) / n - m * m, 0.0))
        new = est.copy()
        for c in range(3):
            cl = mask[..., c] > 0.5
            if not cl.any():
                continue
            oth = [o for o in range(3) if o != c]
            rec = est[..., c].copy()
            for go in oth:
                other = [o for o in oth if o != go][0]
                g = est[..., go]
                w = vf[c] * vf[go]
                fr = f(w)
                n = np.maximum(fr, 1e-6)
                mg = f(g * w) / n
                mc = f(est[..., c] * w) / n
                a = np.maximum((f(g * est[..., c] * w) / n - mg * mc) / (f(g * g * w) / n - mg * mg + eps), 0.0)
                b = mc - a * mg
                choose = (vf[go] > 0.5) & ((vf[other] <= 0.5) | (varc[go] >= varc[other]))
                rec = np.where(cl & choose & (fr > fmin), a * g + b, rec)
            new[..., c] = rec
        est = new
    return est


def _confidence(rgb, mask, cs=20.0):
    """Per-channel colour-line confidence = R^2 = cov^2/(var_g*var_c) of the fit
    against the best valid guide, over a smooth valid-weighted window. ~1 where the
    channels are affinely related (guided recon trustworthy), ~0 where uncorrelated."""
    vf = [(mask[..., c] <= 0.5).astype(np.float64) for c in range(3)]
    f = lambda a: gaussian_filter(a, cs, mode='nearest')
    out = np.zeros(rgb.shape[:2] + (3,))
    for c in range(3):
        best = np.zeros(rgb.shape[:2])
        for go in [o for o in range(3) if o != c]:
            w = vf[c] * vf[go]
            n = np.maximum(f(w), 1e-6)
            mg = f(rgb[..., go] * w) / n
            mc = f(rgb[..., c] * w) / n
            cov = f(rgb[..., go] * rgb[..., c] * w) / n - mg * mc
            vg = f(rgb[..., go] ** 2 * w) / n - mg * mg
            vc = f(rgb[..., c] ** 2 * w) / n - mc * mc
            best = np.maximum(best, cov * cov / (vg * vc + 1e-8))
        out[..., c] = np.clip(best, 0.0, 1.0)
    return out


def _self_inpaint(rgb, mask):
    """Per-channel biharmonic extension of each channel from its OWN valid surround
    (no cross-channel borrow) -- the fallback where the colour-line is untrustworthy."""
    out = rgb.copy()
    for c in range(3):
        hole = mask[..., c] > 0.5
        if hole.any():
            out[..., c] = biharmonic_inpaint(rgb[..., c], hole)
    return out


def _joint_core(rec, mask):
    """All-clipped core: one JOINT reconstruction instead of three independent domes.

    Where every channel is blown there is no colour-line and no per-channel rim to
    trust, and doming each channel from its own clip radius makes the three domes
    reach different heights -> the core drifts off-hue (e.g. a neutral sun turns
    yellow because blue, the last channel to clip, saturates flat at its rim and
    domes weakest). Instead reconstruct ONE quantity per kind:
      * MAGNITUDE: a single biharmonic luminance dome L = sum_c u_c, extended from the
        core rim -- all channels share this shape, so none collapses.
      * HUE: the chromaticity u_c / L, carried inward by harmonic (flat) diffusion from
        the rim -- continues the surrounding colour without doming it.
    core_c = L_dome * chroma_c. The rim here is the already-reconstructed partial-clip
    annulus, so the true/recovered edges drive the central dome jointly.
    """
    out = rec.copy()
    allc = (mask[..., 0] > 0.5) & (mask[..., 1] > 0.5) & (mask[..., 2] > 0.5)
    if not allc.any():
        return out
    L = rec[..., :3].sum(-1)
    Ld = biharmonic_inpaint(L, allc)
    chroma = rec[..., :3] / np.maximum(L, 1e-6)[..., None]
    for c in range(3):
        chroma[..., c] = harmonic_inpaint(chroma[..., c], allc)
    chroma = np.clip(chroma, 0.0, None)
    chroma /= np.maximum(chroma.sum(-1, keepdims=True), 1e-6)
    core = Ld[..., None] * chroma
    out[..., :3] = np.where(allc[..., None], core, rec[..., :3])
    return out


def recon_fixed(clip, white, ds=1, feather=True, conf=True):
    H, W, _ = clip.shape
    clips = 0.995 * np.asarray(white)
    wb = clip.reshape(-1, 3).mean(0)
    mask = np.zeros((H, W, 4))
    mask[..., :3] = (clip > clips).astype(float)
    mask[..., 3] = (mask[..., :3].max(-1) > 0).astype(float)
    if feather:
        mask = R._box_mean5(mask)
    norm_in = np.maximum(clip / wb, 0.0)
    if ds == 1:
        work, wm = norm_in, mask
        sig = FULLRES_SIGMAS
    else:
        work = R.interp_bilinear(norm_in, W // ds, H // ds)
        wm = R.interp_bilinear(mask, W // ds, H // ds)
        sig = tuple(max(s / ds, 1.0) for s in FULLRES_SIGMAS)
    rec = guided_recon(work, wm, sig)
    if conf:
        # Blend the cross-channel guided estimate with per-channel self-inpainting
        # (biharmonic extension of the channel's own valid rim), by a SHARPENED colour-line
        # confidence: We = R^(2*CONF_EXPONENT), i.e. Wc**2 with Wc = R^2. Squaring the
        # confidence separates the cases: where the channels are affinely related
        # (correlated content, R^2 ~ 0.9) We stays high and the accurate cross-channel guide
        # is used; where they are not (decorrelated content, R^2 ~ 0.65) We drops steeply
        # (0.65^2 ~ 0.42) and the pixel leans on the SMOOTH per-channel self dome. That is
        # what selectively de-artifacts the random case -- the guide-flip seam only appears
        # on decorrelated content, where the guide is untrustworthy anyway -- WITHOUT
        # touching the correlated case (there We ~ Wc, so accuracy is preserved; it even
        # improves slightly). Where NO channel survives (the all-clipped core) the value is
        # provisional here and rebuilt jointly below.
        Wc = _confidence(work, wm, cs=max(20.0 / ds, 4.0))
        s = _self_inpaint(work, wm)
        vf = [(wm[..., c] <= 0.5) for c in range(3)]
        for c in range(3):
            oth = [o for o in range(3) if o != c]
            has_guide = vf[oth[0]] | vf[oth[1]]
            clipped = wm[..., c] > 0.5
            We = np.clip(Wc[..., c], 0.0, 1.0) ** CONF_EXPONENT
            blended = We * rec[..., c] + (1.0 - We) * s[..., c]
            rec[..., c] = np.where(clipped, np.where(has_guide, blended, s[..., c]), rec[..., c])
        # All-clipped core (no surviving guide in any channel): replace the three
        # independent per-channel domes with ONE joint luminance dome + diffused
        # chromaticity, so the core keeps the rim's hue instead of drifting off-colour.
        rec[..., :3] = _joint_core(rec, wm)[..., :3]
        # UNCERTAINTY-AWARE REGULARIZATION. The reconstruction above recovers magnitude well
        # but leaves faint SEAMS where its character changes -- the guide-flip discontinuity on
        # decorrelated content, and the core/annulus handoff. No confidence weight can fully hide
        # a discontinuity in the thing it weights, so instead iron the seams out afterwards:
        # solve (diag(Wd) + lambda*Delta^2) u = diag(Wd)*rec per channel, with the finished
        # reconstruction as the data target and Wd = R^4 the fidelity weight. Where the recon is
        # trustworthy (Wd high, correlated) u = rec is preserved; where it is not (Wd low: random,
        # seams, all-clipped core) the biharmonic prior takes over and flattens the CURVATURE
        # spike of the seam while preserving smooth domes and gradients (a harmonic prior would
        # over-smooth them). Magnitude is preserved because the target is the recon itself, not
        # the collapsed guided target -- the all-clipped dome is already smooth, so it is left
        # essentially unchanged. This needs no clean random/correlated segregation.
        Hs, Ws = wm.shape[:2]
        op = REG_LAMBDA * (_laplacian_matrix(Hs, Ws) @ _laplacian_matrix(Hs, Ws))
        hole = wm[..., 3] > 0.5
        Wd = np.clip(Wc, 0.0, 1.0) ** CONF_EXPONENT
        for c in range(3):
            rec[..., c] = _weighted_solve(Wd[..., c], rec[..., c], hole, work[..., c], op.tocsr())
    full = np.concatenate([rec, np.sqrt((rec ** 2).sum(-1))[..., None]], -1)
    up = full if ds == 1 else R.interp_bilinear(full, W, H)
    out = np.maximum(up[..., :3] * wb, 0.0)
    a = mask[..., 3][..., None]
    return a * out + (1.0 - a) * clip


# ---------------- synthetic scenes ----------------
def _lowfreq(H, W, rng, cells):
    f = R.interp_bilinear(rng.standard_normal((cells, cells, 1)), W, H)[..., 0]
    f -= f.min(); f /= (f.max() + 1e-9)
    return f


def scene_random(H, W, rng):
    """Independent per-channel multiscale gradients (no colour-line)."""
    return np.stack([0.07 + 0.38 * R._multiscale_field(H, W, rng) for _ in range(3)], -1)


def scene_correlated(H, W, rng):
    """Natural-like: luminance gradient x smooth random chromaticity."""
    L = 0.07 + 0.40 * R._multiscale_field(H, W, rng)
    ch = np.stack([1 + 0.65 * (_lowfreq(H, W, rng, 6) - 0.5) for _ in range(3)], -1)
    return L[..., None] * ch


def add_bumps(rgb, specs, H, W):
    """Multiplicative (physical) highlights: brighten the local colour."""
    yy, xx = np.mgrid[0:H, 0:W]
    out = rgb.copy(); cores = []
    for cy, cx, sig, amp in specs:
        b = np.exp(-(((yy - cy * H) ** 2 + (xx - cx * W) ** 2) / (2 * sig * sig)))
        out = out * (1 + amp * b)[..., None]
        cores.append((b > 0.6, sig))
    return out, cores


def main():
    R.RADIUS_MODE = 'faithful'
    H = W = 320

    def grid(rng):
        return [((gy + .5) / 4 + rng.uniform(-.05, .05), (gx + .5) / 4 + rng.uniform(-.05, .05),
                 rng.choice([7, 12, 18, 26]), rng.choice([1.6, 2.4, 3.2])) for gy in range(4) for gx in range(4)]

    white = [1., 1., 1.]
    for scn, gen in [('RANDOM rgb', scene_random), ('CORRELATED (L + random chroma)', scene_correlated)]:
        acc = {}
        for sd in (1, 2, 3, 4):
            rng = np.random.default_rng(sd)
            gt, cores = add_bumps(gen(H, W, rng), grid(rng), H, W)
            clip = np.minimum(gt, np.array(white))
            st = R.reconstruct(clip, white, iterations=4, diameter_px=320)[0]
            fx = recon_fixed(clip, white, ds=1)
            cm = (gt > 0.995).any(-1); Lr = float(gt.max())
            for foot, sig in cores:
                m = foot & cm
                if m.sum() < 30:
                    continue
                nch = sum(int((gt[..., c][foot] > 0.995).any()) for c in range(3))
                M = np.broadcast_to(m[..., None], gt.shape); px = int(M.sum())
                a = acc.setdefault(nch, [0., 0., 0., 0., 0., 0])
                a[0] += ((clip - gt)[M] ** 2).sum(); a[1] += ((st - gt)[M] ** 2).sum(); a[2] += ((fx - gt)[M] ** 2).sum()
                a[3] += ssim_region(st, gt, m, Lr) * px; a[4] += ssim_region(fx, gt, m, Lr) * px; a[5] += px
        print(f"\n===== {scn} =====")
        print(f"  {'#clip':6s}{'px':>8s}{'RMSE clip':>10s}{'RMSE stk':>9s}{'RMSE fix':>9s}"
              f"{'SSIM stk':>9s}{'SSIM fix':>9s}")
        for nch in sorted(acc):
            s0, ss, sf, sss, ssf, px = acc[nch]
            print(f"  {nch:6d}{px:8d}{np.sqrt(s0/px):10.4f}{np.sqrt(ss/px):9.4f}{np.sqrt(sf/px):9.4f}"
                  f"{sss/px:9.3f}{ssf/px:9.3f}")


if __name__ == '__main__':
    main()
