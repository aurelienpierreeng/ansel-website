"""
Bug-hunt diagnostics for the guided-laplacian highlight reconstruction.

Finding: Ansel's `guide_laplacians` operates on the à-trous HF (detail) bands,
which are mean-subtracted, so the guided-filter intercept b carries no DC. The
clipped channel's LF residual is added unmodified. => the transfer moves texture
between channels but NEVER extrapolates a clipped channel's magnitude from the
cross-channel colour-line. A full-value guided filter recovers it (single-channel
clips ~40x lower RMSE).

Run with python3.12 (numpy + scipy). Imports the faithful port from
reconstruct_highlights.py in the same directory.
"""
import numpy as np
from scipy.ndimage import uniform_filter
import reconstruct_highlights as R


def boxm(a, r):
    return uniform_filter(a, size=2 * r + 1, mode='nearest')


def guided_fullvalue(clip, white, r=28, eps=1e-4):
    """He guided filter on VALUES (not HF): for each clipped channel, fit
    channel = a*guide + b from samples where BOTH are unclipped, then set the
    clipped pixels to a*guide + b.  guide = the higher-variance unclipped channel."""
    thr = 0.995 * np.asarray(white)
    out = clip.copy()
    validc = [(clip[..., c] < thr[c]).astype(float) for c in range(3)]
    var = []
    for c in range(3):
        n = np.maximum(boxm(validc[c], r), 1e-6)
        m = boxm(clip[..., c] * validc[c], r) / n
        var.append(boxm(clip[..., c] ** 2 * validc[c], r) / n - m * m)
    for c in range(3):
        clipped = clip[..., c] >= thr[c]
        if not clipped.any():
            continue
        others = [o for o in range(3) if o != c]
        gsel = np.where(var[others[0]] >= var[others[1]], others[0], others[1])
        rec = out[..., c].copy()
        for go in others:
            g = clip[..., go]
            w = validc[c] * validc[go]
            n = np.maximum(boxm(w, r), 1e-6)
            mg = boxm(g * w, r) / n
            mc = boxm(clip[..., c] * w, r) / n
            a = np.maximum((boxm(g * clip[..., c] * w, r) / n - mg * mc)
                           / (boxm(g * g * w, r) / n - mg * mg + eps), 0.0)
            b = mc - a * mg
            a, b = boxm(a, r), boxm(b, r)
            rec = np.where(clipped & (gsel == go), a * g + b, rec)
        out[..., c] = rec
    return out


def bump_scene(sigma, hue, amp_ped, amp_bump, seed=1, H=256, W=256):
    yy, xx = np.mgrid[0:H, 0:W]
    g = lambda s: np.exp(-(((yy - H * .5) ** 2 + (xx - W * .5) ** 2) / (2 * s * s)))
    base = 0.10 + 0.06 * R._multiscale_field(H, W, np.random.default_rng(seed))
    gt = np.stack([base] * 3, -1) + (amp_ped * g(2.6 * sigma) + amp_bump * g(sigma))[..., None] * np.array(hue)
    return gt, g(sigma) > 0.6


def main():
    white = [1.0, 1.0, 1.0]
    cases = [('single/small',  6, (1.0, 0.45, 0.40), 0.45, 0.95),
             ('single/med',   12, (1.0, 0.45, 0.40), 0.45, 0.95),
             ('single/large', 24, (1.0, 0.45, 0.40), 0.45, 0.95),
             ('all/small',     6, (1.0, 0.93, 0.88), 0.40, 0.95),
             ('all/med',      12, (1.0, 0.93, 0.88), 0.40, 0.95),
             ('all/large',    24, (1.0, 0.93, 0.88), 0.40, 0.95)]
    R.RADIUS_MODE = 'faithful'
    print(f"{'case':14s}{'#clip':>6s}{'true(RGB)':>20s}{'stock recon':>22s}"
          f"{'fullval recon':>22s}{'RMSE stock':>11s}{'RMSE fv':>9s}")
    for name, sig, hue, ap, ab in cases:
        gt, core = bump_scene(sig, hue, ap, ab)
        clip = np.minimum(gt, np.array(white))
        nclip = sum(int((gt[core, c] > 0.995).any()) for c in range(3))
        st = R.reconstruct(clip, white, iterations=4, diameter_px=256)[0]
        fv = guided_fullvalue(clip, white, r=max(2 * sig, 16))
        cm = (gt > 0.995).any(-1)
        m = np.broadcast_to((core & cm)[..., None], gt.shape)
        rs = np.sqrt(((st - gt)[m] ** 2).mean())
        rf = np.sqrt(((fv - gt)[m] ** 2).mean())
        print(f"{name:14s}{nclip:6d}{str(gt[core].mean(0).round(2)):>20s}"
              f"{str(st[core].mean(0).round(2)):>22s}{str(fv[core].mean(0).round(2)):>22s}"
              f"{rs:11.4f}{rf:9.4f}")


if __name__ == '__main__':
    main()
