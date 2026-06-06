"""
lyraplot - 个人绘图包，提供预设的 matplotlib 样式和导出配置
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt

# 获取包的根目录
_PACKAGE_DIR = Path(__file__).parent

def _auto_discover_styles():
    """自动发现 template 和 color 目录中的所有 .mplstyle 文件"""
    styles = {}
    
    for category in ['template', 'color']:
        category_dir = _PACKAGE_DIR / category
        if category_dir.exists():
            styles[category] = {}
            for style_file in category_dir.glob('*.mplstyle'):
                style_name = style_file.stem  # 文件名不含扩展名
                styles[category][style_name] = str(style_file)
    
    return styles

# 样式文件路径，自动发现
STYLES = _auto_discover_styles()

# 默认加载的样式配置
_DEFAULT_STYLES = [
    ('template', 'line'),
    ('color', 'engineering_frontiers'),
]

# savefig 参数预设
from .savefig_config import SAVEFIG_PARAMS

def load_style(style_type, style_name):
    """
    加载指定的预设样式
    
    Parameters:
    -----------
    style_type : str
        样式类型，如：'template', 'color'
    style_name : str
        样式名称
    
    Examples:
    ---------
    >>> import lyraplot
    >>> lyraplot.load_style('template', 'line')
    >>> lyraplot.load_style('color', 'nature_red_blue')
    """
    if style_type not in STYLES:
        raise ValueError(f"样式类型 '{style_type}' 不存在。可选类型：{list(STYLES.keys())}")
    if style_name not in STYLES[style_type]:
        raise ValueError(f"样式 '{style_name}' 不存在于 '{style_type}' 中。可选样式：{list(STYLES[style_type].keys())}")
    style_path = STYLES[style_type][style_name]
    if not os.path.exists(style_path):
        raise FileNotFoundError(f"样式文件不存在：{style_path}")
    plt.style.use(style_path)

def savefig(fname, **kwargs):
    """
    保存图像，应用预设的 savefig 参数
    
    Parameters:
    -----------
    fname : str
        保存文件的路径
    **kwargs : dict
        额外的 matplotlib savefig 参数，会覆盖预设值
    
    Examples:
    ---------
    >>> import matplotlib.pyplot as plt
    >>> import lyraplot
    >>> plt.plot([1, 2, 3])
    >>> lyraplot.savefig('plot.svg')
    >>> lyraplot.savefig('plot.png', dpi=150)  # 覆盖预设的 dpi
    """
    # 合并预设参数和用户传入的参数
    save_params = SAVEFIG_PARAMS.copy()
    save_params.update(kwargs)
    plt.savefig(fname, **save_params)

# 加载默认样式
for style_type, style_name in _DEFAULT_STYLES:
    load_style(style_type, style_name)

__all__ = ['STYLES', 'SAVEFIG_PARAMS', 'load_style', 'savefig']
