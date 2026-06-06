import os
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import style

# 获取包的根目录
_PACKAGE_DIR = Path(__file__).parent


def _auto_discover_styles():
    """自动发现所有 .mplstyle 文件"""
    styles = {}
    
    for style_file in _PACKAGE_DIR.rglob('*.mplstyle'):
        style_name = style_file.stem  # 文件名不含扩展名
        styles[style_name] = str(style_file)
    
    return styles

# 样式文件路径，自动发现
STYLES = _auto_discover_styles()
print(f"Discovered styles: {list(STYLES.keys())}")

# 将所有样式注册到 matplotlib 的样式库中
for style_name, style_path in STYLES.items():
    style.library[style_name] = style_path
    if style_name not in style.available:
        style.available.append(style_name)

# 加载默认样式（base）
plt.style.use('lyrabase')

# 导入绘图工具函数
from .plotting import savefig, setup_minor_ticks

__all__ = ['STYLES', 'savefig', 'setup_minor_ticks']
