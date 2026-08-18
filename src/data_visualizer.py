import matplotlib.pyplot as plt


def init_plot_style(style_name: str = 'ggplot'):
    """初始化绘图风格"""
    plt.style.use(style_name)
