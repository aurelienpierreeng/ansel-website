"""
Pure-NumPy port of Ansel's guided-laplacian highlight reconstruction
(src/iop/highlights.c : guide_laplacians + heat_PDE_diffusion + wavelets_process),
minus the demosaicing/remosaicing (works directly on RGB).

Verified against the C/OpenCL sources; see the companion article.
"""
import numpy as np

# ---- constants (src/common/bspline.h) ----
B_SPLINE_SIGMA        = 1.0553651328015339
B_SPLINE_TO_LAPLACIAN = 3.182727439285017
DS_FACTOR             = 4
RED, GREEN, BLUE, ALPHA = 0, 1, 2, 3
_FILT = np.array([1., 4., 6., 4., 1.]) / 16.0
_KISO = np.array([0.25, 0.5, 0.25, 0.5, -3.0, 0.5, 0.25, 0.5, 0.25])


def equivalent_sigma_at_step(sigma, s):
    r = sigma
    for k in range(1, s + 1):
        r = np.sqrt(r * r + (2.0 ** k * sigma) ** 2)
    return r


def _shift(a, dy, dx):
    """Shift (H,W,C) by (dy,dx) with clamped (replicate) borders."""
    H, W = a.shape[:2]
    yi = np.clip(np.arange(H) + dy, 0, H - 1)
    xi = np.clip(np.arange(W) + dx, 0, W - 1)
    return a[yi][:, xi]


def _blur_bspline(a, mult):
    """Separable 5-tap a-trous B-spline blur at stride `mult`, clamped, LF>=0."""
    v = (_FILT[0] * _shift(a, -2 * mult, 0) + _FILT[1] * _shift(a, -mult, 0)
         + _FILT[2] * a + _FILT[3] * _shift(a, mult, 0) + _FILT[4] * _shift(a, 2 * mult, 0))
    v = np.maximum(v, 0.0)
    h = (_FILT[0] * _shift(v, 0, -2 * mult) + _FILT[1] * _shift(v, 0, -mult)
         + _FILT[2] * v + _FILT[3] * _shift(v, 0, mult) + _FILT[4] * _shift(v, 0, 2 * mult))
    return np.maximum(h, 0.0)


def _decompose(a, mult):
    LF = _blur_bspline(a, mult)
    return a - LF, LF          # HF, LF


def interp_bilinear(a, Wout, Hout):
    """Faithful port of interpolate_bilinear() (fast_guided_filter.h)."""
    Hin, Win = a.shape[:2]
    x_in = (np.arange(Wout) / Wout) * Win
    y_in = (np.arange(Hout) / Hout) * Hin
    xp = np.clip(np.floor(x_in).astype(int), 0, Win - 1)
    xn = np.clip(np.floor(x_in).astype(int) + 1, 0, Win - 1)
    yp = np.clip(np.floor(y_in).astype(int), 0, Hin - 1)
    yn = np.clip(np.floor(y_in).astype(int) + 1, 0, Hin - 1)
    Dx_next = xn - x_in; Dx_prev = 1.0 - Dx_next
    Dy_next = yn - y_in; Dy_prev = 1.0 - Dy_next
    NW = a[np.ix_(yp, xp)]; NE = a[np.ix_(yp, xn)]
    SW = a[np.ix_(yn, xp)]; SE = a[np.ix_(yn, xn)]
    dxn = Dx_next[None, :, None]; dxp = Dx_prev[None, :, None]
    dyn = Dy_next[:, None, None]; dyp = Dy_prev[:, None, None]
    return dyp * (SW * dxn + SE * dxp) + dyn * (NW * dxn + NE * dxp)


def _box_mean5(a):
    """5x5 box average per channel with replicate borders (dt_box_mean r=2)."""
    from scipy.ndimage import uniform_filter
    return uniform_filter(a, size=(5, 5, 1), mode='nearest')


def guide_laplacians(HF, LF, mask, out, mult, radius_sq, first, last):
    eps = 1e-12
    do = mask[..., ALPHA] > 0.0
    S = np.zeros_like(HF); Ssq = np.zeros_like(HF)
    pR = np.zeros_like(HF); pG = np.zeros_like(HF); pB = np.zeros_like(HF)
    for dy in (-mult, 0, mult):
        for dx in (-mult, 0, mult):
            s = _shift(HF, dy, dx)
            S += s; Ssq += s * s
            pR += s * s[..., RED:RED + 1]
            pG += s * s[..., GREEN:GREEN + 1]
            pB += s * s[..., BLUE:BLUE + 1]
    means = S / 9.0
    var = np.maximum(Ssq / 9.0 - means * means, 0.0)
    var[..., ALPHA] = 0.0
    guide = np.argmax(var[..., :3], axis=-1)                       # (H,W) in {0,1,2}
    g_var = np.take_along_axis(var[..., :3], guide[..., None], -1)[..., 0]
    g_mean = np.take_along_axis(means[..., :3], guide[..., None], -1)[..., 0]
    P = np.stack([pR, pG, pB], axis=-2)                            # (H,W,3,4)
    idx = np.broadcast_to(guide[..., None, None], P.shape[:2] + (1, 4))
    prod = np.take_along_axis(P, idx, axis=-2)[..., 0, :]          # (H,W,4)
    cov = prod / 9.0 - means * g_mean[..., None]
    slope = np.maximum(cov / np.where(g_var > 0, g_var, 1.0)[..., None], 0.0)
    intercept = means - slope * g_mean[..., None]
    g_val = np.take_along_axis(HF[..., :3], guide[..., None], -1)[..., 0]   # guide HF at center
    blend = mask / radius_sq
    transferred = blend * (slope * g_val[..., None] + intercept) + (1.0 - blend) * HF
    apply = (do & (g_var > eps))[..., None]
    hf = np.where(apply, transferred, HF)

    op = hf if first else hf + out
    if last:
        op = np.maximum(op + LF, 0.0)
        norm = np.maximum(np.sqrt(np.sum(op[..., :3] ** 2, axis=-1)), 1e-6)
        op = op / norm[..., None]
        op[..., ALPHA] = norm
    out[...] = op


def heat_pde(HF, LF, mask, out, mult, first, last, first_order):
    do = mask[..., ALPHA] > 0.0
    norm_backup = HF[..., ALPHA].copy()
    lap = np.zeros_like(HF); k = 0
    for dy in (-mult, 0, mult):
        for dx in (-mult, 0, mult):
            lap += _KISO[k] * _shift(HF, dy, dx); k += 1
    kappa = 1.0 / B_SPLINE_TO_LAPLACIAN
    hf = HF.copy()
    upd = mask[..., :3] * kappa * (lap[..., :3] - first_order * HF[..., :3])
    hf[..., :3] = HF[..., :3] + np.where(do[..., None], upd, 0.0)
    hf[..., ALPHA] = norm_backup

    op = hf if first else hf + out
    if last:
        op = np.maximum(op + LF, 0.0)
        norm = np.sqrt(np.sum(op[..., :3] ** 2, axis=-1))
        denom = np.where(do & (norm > 1e-4), norm, 1.0)
        op = op.copy()
        op[..., :3] = op[..., :3] / denom[..., None]
        op[..., :3] = op[..., :3] * op[..., ALPHA][..., None]
    out[...] = op


RADIUS_MODE = 'faithful'   # 'faithful' | 'noDS' | 'stride' | 'none'
FEATHER = True             # feather the clip mask (5x5 box) into a soft opacity


def _radius_sq(s):
    if RADIUS_MODE == 'faithful':   # exactly the C code: sqf(equivalent_sigma_at_step(B, s*DS_FACTOR))
        return equivalent_sigma_at_step(B_SPLINE_SIGMA, s * DS_FACTOR) ** 2
    if RADIUS_MODE == 'noDS':       # drop the DS_FACTOR from the step index
        return equivalent_sigma_at_step(B_SPLINE_SIGMA, s) ** 2
    if RADIUS_MODE == 'stride':     # window-area weighting ~ (2^s)^2
        return float((1 << s) ** 2)
    return 1.0                      # 'none' : no scale attenuation, blend = mask


def wavelets_process(inp, out, mask, scales, variant, first_order=0.0):
    LF_prev = inp
    for s in range(scales):
        mult = 1 << s
        HF, LF = _decompose(LF_prev, mult)
        first, last = (s == 0), (s == scales - 1)
        radius_sq = _radius_sq(s)
        if variant == 'RGB':
            guide_laplacians(HF, LF, mask, out, mult, radius_sq, first, last)
        else:
            heat_pde(HF, LF, mask, out, mult, first, last, first_order)
        LF_prev = LF


def reconstruct(clipped, white, clip=1.0, iterations=4, diameter_px=256, solid_color=0.0):
    """clipped: (H,W,3) linear RGB; white: (3,) per-channel white level."""
    H, W, _ = clipped.shape
    clips = 0.995 * clip * np.asarray(white)                     # per-channel threshold
    # --- interpolated [R/wb, G/wb, B/wb, ||RGB||] + per-channel clip mask ---
    wb = clipped.reshape(-1, 3).mean(axis=0)                     # local channel normalization
    interp = np.zeros((H, W, 4))
    interp[..., :3] = np.maximum(clipped / wb, 0.0)
    interp[..., ALPHA] = np.sqrt(np.sum(clipped ** 2, axis=-1))
    mask = np.zeros((H, W, 4))
    mask[..., :3] = (clipped > clips).astype(float)
    mask[..., ALPHA] = (mask[..., :3].max(axis=-1) > 0).astype(float)
    if FEATHER:
        mask = _box_mean5(mask)                                  # feather -> opacity alpha
    # --- downsample (decimation, exactly as the C bilinear at 4:1) ---
    dsW, dsH = W // DS_FACTOR, H // DS_FACTOR
    ds_interp = interp_bilinear(interp, dsW, dsH)
    ds_mask = interp_bilinear(mask, dsW, dsH)
    scales = int(np.clip(np.ceil(np.log2(diameter_px / DS_FACTOR)), 1, 12))
    temp = np.zeros_like(ds_interp)
    for _ in range(iterations):
        wavelets_process(ds_interp, temp, ds_mask, scales, 'RGB', solid_color)
        wavelets_process(temp, ds_interp, ds_mask, scales, 'CHROMA', solid_color)
    # --- upsample + blend by feathered alpha (skip remosaic) ---
    up = interp_bilinear(ds_interp, W, H)
    a = mask[..., ALPHA][..., None]
    recon_rgb = np.maximum(up[..., :3] * wb, 0.0)
    return a * recon_rgb + (1.0 - a) * clipped, scales


# ===================== synthetic scene + experiment =====================
def _multiscale_field(H, W, rng):
    f = np.zeros((H, W))
    for scale in (128, 64, 32, 16, 8, 4):
        gh, gw = max(H // scale, 2), max(W // scale, 2)
        g = rng.standard_normal((gh, gw, 1))
        f += interp_bilinear(g, W, H)[..., 0] * (scale ** 0.75)
    f -= f.min(); f /= (f.max() + 1e-9)
    return f


# Per-channel white levels: green has the least head-room, so a neutral highlight
# clips green first -> the classic magenta cast. (Mirrors processed_maximum / WB.)
WHITE = np.array([1.10, 0.86, 1.00])


def make_scene(H=256, W=256, seed=7):
    """A near-neutral, low-saturation textured base carrying bright, near-neutral
    highlights of varying size. Because the per-channel white levels differ, a
    modest highlight clips only green (single channel), while a bright one clips
    every channel (all). The true colour is near-neutral, so a cast-removing
    reconstruction has a well-posed target."""
    rng = np.random.default_rng(seed)
    L = _multiscale_field(H, W, rng)
    base = 0.08 + 0.42 * L[..., None] + 0.06 * np.stack(
        [_multiscale_field(H, W, rng) for _ in range(3)], axis=-1)   # near-neutral, < any white
    yy, xx = np.mgrid[0:H, 0:W]

    def gauss(cy, cx, s):
        return np.exp(-(((yy - cy) ** 2 + (xx - cx) ** 2) / (2.0 * s * s)))

    # cy, cx, sigma, peak, hue tint (near-neutral), size  -- peak sets #clipped channels
    specs = [
        (0.28, 0.18,  9.0, 0.62, (1.00, 0.98, 0.97), 'small'),
        (0.28, 0.50, 17.0, 0.62, (1.00, 0.98, 0.97), 'medium'),
        (0.28, 0.83, 30.0, 0.62, (1.00, 0.98, 0.97), 'large'),
        (0.72, 0.18,  9.0, 1.15, (1.00, 0.97, 0.95), 'small'),
        (0.72, 0.50, 17.0, 1.15, (1.00, 0.97, 0.95), 'medium'),
        (0.72, 0.83, 30.0, 1.15, (1.00, 0.97, 0.95), 'large'),
    ]
    gt = base.copy()
    regions = []
    for cy, cx, sigma, peak, hue, size in specs:
        cy, cx, hue = cy * H, cx * W, np.array(hue)
        core = gauss(cy, cx, sigma)
        gt += (peak * core)[..., None] * hue[None, None, :]
        regions.append((core > 0.5, size))                          # footprint = bump core
    return base, gt, regions


def rmse(a, b, m):
    d = (a - b)[m]
    return float(np.sqrt(np.mean(d ** 2))) if d.size else float('nan')


def main():
    H = W = 256
    base, gt, regions = make_scene(H, W)
    clipped = np.minimum(gt, WHITE[None, None, :])              # per-channel sensor clip
    recon, scales = reconstruct(clipped, WHITE, iterations=4, diameter_px=256)

    thr = 0.995 * WHITE
    clip_mask = (gt > thr).any(axis=-1)
    print(f"image {H}x{W}, downsampled {H//DS_FACTOR}x{W//DS_FACTOR}, {scales} wavelet scales")
    print(f"per-channel white {WHITE.tolist()}; clipped pixels {clip_mask.sum()} "
          f"({100*clip_mask.mean():.1f}%)\n")
    hdr = f"{'region':22s}{'px':>7s}{'RMSE clip':>11s}{'RMSE recon':>12s}{'improv':>9s}"
    print(hdr); print("-" * len(hdr))
    for foot, size in regions:
        m = foot & clip_mask
        nclip = sum(int((gt[..., c][foot] > thr[c]).any()) for c in range(3))
        cat = f"{nclip}-chan / {size}"
        M = np.broadcast_to(m[..., None], gt.shape)
        r0, r1 = rmse(clipped, gt, M), rmse(recon, gt, M)
        print(f"{cat:22s}{int(m.sum()):7d}{r0:11.4f}{r1:12.4f}{100*(1-r1/r0):8.1f}%")
    print("-" * len(hdr))
    M = np.broadcast_to(clip_mask[..., None], gt.shape)
    r0, r1 = rmse(clipped, gt, M), rmse(recon, gt, M)
    print(f"{'ALL clipped':22s}{int(clip_mask.sum()):7d}{r0:11.4f}{r1:12.4f}{100*(1-r1/r0):8.1f}%")

    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, arr in (('_gt', gt), ('_clip', clipped), ('_recon', recon)):
        np.save(os.path.join(here, name + '.npy'), arr)


if __name__ == '__main__':
    main()
