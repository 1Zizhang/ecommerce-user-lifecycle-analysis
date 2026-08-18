import matplotlib.pyplot as plt


def init_plot_style(style_name: str = 'ggplot'):
    """初始化绘图风格"""
    plt.style.use(style_name)
    plt.rcParams['font.sans-serif'] = ['SimHei']


def plot_monthly_sales(df):
    '''
    月产品销售数量图
    :param df: DataFrame
    :return: 无
    '''
    month_sale = df.groupby(by='month')['order_products'].sum()
    fig, ax = plt.subplots(figsize=(10, 4))
    month_sale.plot(ax=ax)
    ax.set_title("每月商品总销量")
    ax.set_xlabel("月份")
    ax.set_ylabel("商品总销量")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
