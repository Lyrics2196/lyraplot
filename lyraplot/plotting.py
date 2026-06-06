"""
lyraplot 绘图工具函数模块
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def savefig(fname, **kwargs):
    plt.savefig(fname, format='svg', pad_inches=0, **kwargs)


def setup_minor_ticks(ax=None):
    if ax is None:
        ax = plt.gca()
    
    # AutoMinorLocator(2) 表示在两个major tick之间放置1个minor tick
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))


__all__ = ['savefig', 'setup_minor_ticks']
