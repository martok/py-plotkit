from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator

from .const import GOLDEN_RATIO
from .file import get_invoker_dir, expand_relative
from .style import set_style

# apply default rcParams right after loading
set_style()

output_mode = "auto"
"""
"file"        : only produce files
"interactive" : show all plots, including those with filename, produce no files
"both"        : produce files if requested, show all
"auto"        : save if file name given, show if not
"""

output_location = get_invoker_dir()
"""
base for relative file paths on output
"""

sizes = {
    "regular": (150 * GOLDEN_RATIO, 150),
    "wide": (150 * GOLDEN_RATIO, 150)
}
"""
some template sizes for use with new_*, given in millimeters
"""


# Units in matplotlib:
#   figure size       : inches
#   font size         : pt-72
#   linewidth         : pt-72
#   savefig           : actually "oversampled"
# -> make sure to create plots with figure.dpi=72 or layout breaks!

def subplots(*args, **kwargs):
    return plt.subplots(*args, **kwargs, dpi=72)


def default_dpi(save=False):
    if save and mpl.rcParams["savefig.dpi"] != "figure":
        return mpl.rcParams["savefig.dpi"]
    return mpl.rcParams["figure.dpi"]


def new_mm(*args, figsize, **kwargs):
    return subplots(*args, figsize=(figsize[0] / 25.4, figsize[1] / 25.4), **kwargs)


def new_regular(*args, **kwargs):
    return new_mm(*args, figsize=sizes["regular"], **kwargs)


def new_wide(*args, **kwargs):
    return new_mm(*args, figsize=sizes["wide"], **kwargs)


def auto_minor_ticks(axs: Axes, x=True, y=True):
    if x:
        axs.xaxis.set_minor_locator(AutoMinorLocator())
    if y:
        axs.yaxis.set_minor_locator(AutoMinorLocator())


def autogrid(axs: Axes):
    axs.grid(which="major", linestyle="-")
    axs.grid(which="minor", linestyle=":", linewidth=mpl.rcParams["grid.linewidth"] * 0.5,
             alpha=mpl.rcParams["grid.alpha"] * 0.8)


def finalize(fig: Figure, filename: Optional[str] = None):
    if output_mode == "both":
        raise NotImplementedError(f"Unsupported due to errors with tight_layout")
    do_save = filename and (output_mode == "auto" or output_mode == "file")
    do_show = output_mode == "interactive" or (output_mode == "auto" and not filename)
    if do_show:
        fig.show()
    if do_save:
        filename = expand_relative(filename, output_location)
        fig.savefig(filename)
    return filename

