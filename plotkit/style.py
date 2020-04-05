from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt

# https://matplotlib.org/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files
styles = {
    'default': {
        'pk_use': 'default',
        'figure.dpi': 72,
        'savefig.dpi': 144,
        'figure.autolayout': True,
        # 'figure.constrained_layout.use': True,
        'lines.linewidth': 1.5,
        'lines.linestyle': '-',
        'grid.color': 'silver',
        'grid.linewidth': 0.75,
        # svg.fonttype : 'path'         # How to handle SVG fonts:
        #    'none': Assume fonts are installed on the machine where the SVG will be viewed.
        #    'path': Embed characters as paths -- supported by most SVG renderers
        #    'svgfont': Embed characters as SVG fonts -- supported only by Chrome,
        #               Opera and Safari
        'svg.fonttype': 'none'
    },
    'print': {
        'pk_pre': 'default',
        'savefig.dpi': 600,
    },
    'poster': {
        'pk_pre': 'print',
        'font.size': 18
    }
}


def apply_styledef(pk_use=None, pk_pre=None, **rc):
    if pk_use:
        plt.style.use(pk_use)
    if pk_pre:
        if isinstance(pk_pre, list):
            for p in pk_pre:
                apply_styledef(**styles[p])
        else:
            apply_styledef(**styles[pk_pre])
    mpl.rcParams.update(rc)


def set_style(target: Optional[str] = None):
    if not target:
        apply_styledef(**styles['default'])
    else:
        apply_styledef(**styles[target])
