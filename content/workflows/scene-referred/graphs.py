#pip install colour-science
#pip install matplotlib

import colour
import colour.plotting
import numpy as np
import matplotlib.pyplot as plt

colour.plotting.plot_single_illuminant_sd("FL1")

LMS = colour.sd_to_XYZ(colour.SDS_ILLUMINANTS["FL1"], colour.colorimetry.MSDS_CMFS_LMS["Stockman & Sharpe 2 Degree Cone Fundamentals"])
plt.bar(["R", "G", "B"], LMS, color=["red", "green", "blue"])
plt.show()

RGB_sensor = colour.sd_to_XYZ(colour.SDS_ILLUMINANTS["FL1"], colour.MSDS_CAMERA_SENSITIVITIES["Nikon 5100 (NPL)"])
plt.bar(["R", "G", "B"], RGB_sensor, color=["red", "green", "blue"])
plt.show()

colour.plotting.plot_multi_sds(colour.MSDS_CAMERA_SENSITIVITIES["Nikon 5100 (NPL)"], tight_layout=True,)

# In practice, we would white-balance sensor RGB, then convert to XYZ using input color profile, then to sRGB
# Here we go directly from input spectrum to sRGB, which is the end-goal of the practical operation.
# Of course, it's idealized, but the point is not to illustrate the inaccuracies of the internal pipeline.
sRGB = colour.XYZ_to_sRGB(colour.sd_to_XYZ(colour.SDS_ILLUMINANTS["FL1"], colour.colorimetry.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]), apply_cctf_encoding=False)
plt.bar(["R", "G", "B"], sRGB, color=["red", "green", "blue"])
plt.show()

"""
cmfs = (
    colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
    .copy()
    .align(colour.recovery.SPECTRAL_SHAPE_sRGB_MALLETT2019)
)
illuminant = colour.SDS_ILLUMINANTS["D65"].copy().align(cmfs.shape)
"""

sRGB_spectrum = colour.recovery.RGB_to_sd_Mallett2019(sRGB)
colour.plotting.plot_single_sd(sRGB_spectrum, title="Light spectrum from FL1 illuminant as displayed on sRGB screen", tight_layout=True,)

colour.plotting.plot_single_sd_colour_rendition_report(colour.SDS_ILLUMINANTS["FL1"])

def plot(XYZ, title):
    xy = colour.xy_to_Luv_uv(colour.XYZ_to_xy(XYZ))
    x, y = xy
    print(xy)
    colour.plotting.plot_chromaticity_diagram_CIE1976UCS(standalone=False)
    plt.plot(x, y, "+", color="black", markersize=20)
    plt.annotate(
        "FL1",
        xy=xy,
        xytext=(-50, 30),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.2"),
    )
    colour.plotting.render(
        standalone=True,
        bounding_box=(-0.1, 0.7, -0.1, 0.7),
        tight_layout=True,
        title=title
    )
    plt.show()

    return xy

xy1 = plot(colour.sd_to_XYZ(colour.SDS_ILLUMINANTS["FL1"]), "Chromaticity coordinates in CIE L'u'v' 1976 (scene perception)")
xy2 = plot(colour.sRGB_to_XYZ(sRGB, apply_cctf_decoding=False), "Chromaticity coordinates in CIE L'u'v' 1976 (display)")

print(np.linalg.norm(xy1 - xy2) / (np.linalg.norm(xy1) + np.linalg.norm(xy2)) * 2)

print(colour.colour_rendering_index(colour.SDS_ILLUMINANTS["FL1"]))
