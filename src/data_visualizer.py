import matplotlib.pyplot as plt


def init_plot_style(style_name: str = 'ggplot'):
    """
    初始化绘图风格
    """
    plt.style.use(style_name)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False


def plot_monthly_sales(df):
    """
    月产品销售数量，消费金额，次数，消费人数图
    :param df: DataFrame
    :return: 无
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1.每月产品购买数量
    ax = axes[0, 0]
    df.groupby('month')['order_products'].sum().plot(ax=ax, kind='line', marker='o')
    ax.set_title('月度产品购买总数量趋势')
    ax.set_xlabel('月份')
    ax.set_ylabel('购买总数量')

    # 2.每月消费金额
    ax = axes[0, 1]
    df.groupby('month')['order_amount'].sum().plot(ax=ax, kind='line', marker='o')
    ax.set_title('月度累计消费金额趋势')
    ax.set_xlabel('月份')
    ax.set_ylabel('消费总金额')

    # 3.每月消费次数
    ax = axes[1, 0]
    df.groupby('month')['user_id'].count().plot(ax=ax, kind='line', marker='o')
    ax.set_title('月度订单次数趋势')
    ax.set_xlabel('月份')
    ax.set_ylabel('订单次数')

    # 4.每月消费人数
    ax = axes[1, 1]
    df.groupby('month')['user_id'].nunique().plot(ax=ax, kind='line', marker='o')
    ax.set_title('月度活跃消费人数趋势')
    ax.set_xlabel('月份')
    ax.set_ylabel('独立消费人数')

    plt.tight_layout()
    plt.show()
    plt.close()
