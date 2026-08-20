from src.data_visualizer import init_plot_style, plot_monthly_sales, plot_order_products_amount_scatter, \
    plot_customer_amount_hist
from src.data_loader import load_ecommerce_data
from src.data_processor import preprocess_data

FILE_PATH = 'data/ecommerce_transactions.txt'


def main():
    # 1.初始化绘图风格+中文字体显示
    init_plot_style()
    # 2.加载文件
    raw_df = load_ecommerce_data(FILE_PATH)
    # 3.字段格式转换
    df = preprocess_data(raw_df)
    # 4.画图
    plot_monthly_sales(df)
    plot_order_products_amount_scatter(df)
    plot_customer_amount_hist(df)


if __name__ == '__main__':
    main()
