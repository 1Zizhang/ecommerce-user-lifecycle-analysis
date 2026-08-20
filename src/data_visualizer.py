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


def plot_order_products_amount_scatter(df):
    """
    用户购买数量与订单金额散点图
    :param df:DataFrame
    :return:无
    """
    df.plot(kind='scatter', x='order_products', y='order_amount', figsize=(14, 10))
    plt.xlabel("下单商品数量")
    plt.ylabel("订单金额")
    plt.title("商品数量‑订单金额散点图")
    plt.grid(True)
    plt.show()
    plt.close()


def plot_customer_amount_hist(df):
    """
    用户消费分布图
    :param df: DataFrame
    :return: 无
    """
    # 定义画布
    fig, axes = plt.subplots(2, 3, figsize=(14, 10))
    ax = axes[0, 0]
    df['order_amount'].plot(kind='hist', ax=ax, bins=50)
    ax.set_xlabel('用户消费金额')
    ax.set_ylabel('用户人数')
    ax.set_title('用户消费金额 - 人数直方图')
    ax = axes[0, 1]
    df.groupby(by=['user_id'])['order_products'].sum().plot(kind='hist', ax=ax, bins=50)
    ax.set_xlabel('用户购买数量')
    ax.set_ylabel('产品总金额')
    ax.set_title('用户购买数量 - 产品金额直方图')
    ax = axes[0, 2]
    user_cum_sum = df.groupby(by=['user_id'])['order_amount'].sum().sort_values(ascending=True).reset_index()
    user_cum_sum['amount_cum_sum'] = user_cum_sum['order_amount'].cumsum()
    amount_total = user_cum_sum['amount_cum_sum'].max()
    user_cum_sum['prop'] = user_cum_sum.apply(lambda x: x['amount_cum_sum'] / amount_total, axis=1)
    user_cum_sum['prop'].plot(ax=ax)
    ax.set_xlabel('用户量')
    ax.set_ylabel('消费占比')
    ax.set_title('用户消费金额占比分析 - ')
    plt.tight_layout()
    plt.show()
    plt.close()
