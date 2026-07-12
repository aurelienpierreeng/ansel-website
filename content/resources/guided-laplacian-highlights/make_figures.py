"""
Generate every synthetic figure used in the article, with its RMSE/SSIM metrics.

Panels are always: ground truth | clipped (sensor) | current implementation | corrected method.
- current implementation = reconstruct_highlights.reconstruct  (the shipped HF-only method)
- corrected method       = fix_prototype.recon_fixed           (full-value guided + gated chroma
                                                                + biharmonic magnitude dome)

Run: `python3.12 make_figures.py`  (needs numpy, scipy, Pillow; see reconstruct_highlights.py
and fix_prototype.py in this bundle). Writes the PNGs referenced by index.md.
"""
import numpy as np
from PIL import Image, ImageDraw
import reconstruct_highlights as R
import fix_prototype as F

R.RADIUS_MODE = 'faithful'
WHITE = [1.0, 1.0, 1.0]

# Underexpose the display by ~2/3 stop so bright fills sit clearly below peak white/primaries;
# otherwise clipped and reconstructed highlights both saturate the display and become
# indistinguishable. This is a display-only tone map — the metrics run on the linear data.
DISPLAY_EV = -0.66
DISPLAY_GAIN = 2.0 ** DISPLAY_EV


def panel(named_imgs, vmax, fname):
    """Tone-map (normalize by vmax, underexpose, gamma 2.2) and lay panels out horizontally."""
    H, W = named_imgs[0][1].shape[:2]
    gap, lab = 8, 22
    cv = Image.new('RGB', (len(named_imgs) * W + (len(named_imgs) - 1) * gap, H + lab), (250, 250, 248))
    d = ImageDraw.Draw(cv)
    disp = lambda im: (np.clip(DISPLAY_GAIN * im / vmax, 0, 1) ** (1 / 2.2) * 255 + 0.5).astype(np.uint8)
    for i, (nm, im) in enumerate(named_imgs):
        x = i * (W + gap)
        cv.paste(Image.fromarray(disp(im)), (x, lab))
        d.text((x + 3, 6), nm, fill=(20, 20, 20))
    cv.save(fname)


def metrics(clip, st, fx, gt, white=WHITE):
    cm = (gt > 0.995 * np.asarray(white)).any(-1)
    Lr = float(gt.max())
    M = np.broadcast_to(cm[..., None], gt.shape)
    rm = lambda a: float(np.sqrt(((a - gt)[M] ** 2).mean()))
    return dict(clipped_pct=100 * cm.mean(),
                rmse=(rm(clip), rm(st), rm(fx)),
                ssim=(F.ssim_region(clip, gt, cm, Lr), F.ssim_region(st, gt, cm, Lr), F.ssim_region(fx, gt, cm, Lr)))


def _gauss(H, W, cy, cx, s):
    yy, xx = np.mgrid[0:H, 0:W]
    return np.exp(-(((yy - cy) ** 2 + (xx - cx) ** 2) / (2.0 * s * s)))


def scene_bubbles(H=256, W=256, seed=5):
    """Hero scene: R/G/B single-channel disks + one bright near-neutral (all-clip) disk,
    on a dark near-neutral gradient. Each disk = a coloured Gaussian bump on a faint
    same-hue pedestal (so the surviving channels carry the colour-line)."""
    rng = np.random.default_rng(seed)
    L = 0.06 + 0.20 * R._multiscale_field(H, W, rng)
    base = L[..., None] * np.stack([1 + 0.20 * (F._lowfreq(H, W, rng, 5) - 0.5) for _ in range(3)], -1)
    specs = [(0.30, 0.20, 15, (1.45, 0.55, 0.48)), (0.30, 0.52, 15, (0.55, 1.42, 0.55)),
             (0.30, 0.83, 15, (0.50, 0.58, 1.45)), (0.70, 0.28, 26, (1.42, 0.60, 0.50)),
             (0.70, 0.70, 20, (1.30, 1.22, 1.15))]
    gt = base.copy()
    for cy, cx, s, g in specs:
        shape = 0.18 * _gauss(H, W, cy * H, cx * W, 2.2 * s) + _gauss(H, W, cy * H, cx * W, s)
        gt = gt + shape[..., None] * np.array(g)
    return gt


def scene_magenta_sun(H=256, W=256, seed=3):
    """A bright near-neutral sun over an orange sky, with per-channel white levels
    (green clips lowest) so the blown sun records as magenta."""
    white = [1.00, 0.72, 0.95]
    rng = np.random.default_rng(seed)
    g = R._multiscale_field(H, W, rng)
    sky = np.stack([0.45 + 0.15 * g, 0.28 + 0.10 * g, 0.10 + 0.05 * g], -1)
    sun = _gauss(H, W, H * 0.42, W * 0.55, 26)
    gt = sky + (2.6 * sun)[..., None] * np.array([1.0, 1.0, 1.0])
    return gt, white


def _grid(rng):
    return [((gy + .5) / 4 + rng.uniform(-.05, .05), (gx + .5) / 4 + rng.uniform(-.05, .05),
             rng.choice([7, 12, 18, 26]), rng.choice([1.6, 2.4, 3.2])) for gy in range(4) for gx in range(4)]


def main():
    # --- hero: R/G/B/neutral bubbles ---
    gt = scene_bubbles()
    clip = np.minimum(gt, np.array(WHITE))
    st = R.reconstruct(clip, WHITE, iterations=4, diameter_px=256)[0]
    fx = F.recon_fixed(clip, WHITE, ds=1)
    panel([('ground truth', gt), ('clipped (sensor)', clip),
           ('current implementation', st), ('corrected method', fx)], 1.35, 'synthetic-bug-fix.png')

    # --- validation scene families (source of the RMSE/SSIM table) ---
    for tag, gen in [('correlated', F.scene_correlated), ('random', F.scene_random)]:
        rng = np.random.default_rng(2)
        gt, _ = F.add_bumps(gen(320, 320, rng), _grid(rng), 320, 320)
        clip = np.minimum(gt, np.array(WHITE))
        st = R.reconstruct(clip, WHITE, iterations=4, diameter_px=320)[0]
        fx = F.recon_fixed(clip, WHITE, ds=1)
        panel([('ground truth', gt), ('clipped', clip),
               ('current implementation', st), ('corrected method', fx)], 2.0, f'{tag}-validation.png')
        print(tag, metrics(clip, st, fx, gt))

    # --- magenta sun over orange sky (chroma + biharmonic dome) ---
    gt, white = scene_magenta_sun()
    clip = np.minimum(gt, np.array(white))
    st = R.reconstruct(clip, white, iterations=4, diameter_px=256)[0]
    fx = F.recon_fixed(clip, white, ds=1)
    panel([('ground truth', gt), ('clipped: magenta sun', clip),
           ('current implementation', st), ('corrected method', fx)], 2.4, 'magenta-sun.png')
    print('magenta-sun', metrics(clip, st, fx, gt, white))


if __name__ == '__main__':
    main()
