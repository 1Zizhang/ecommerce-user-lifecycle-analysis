from src.data_visualizer import init_plot_style
from src.data_loader import load_ecommerce_data
from src.data_processor import preprocess_data
from src.data_visualizer import plot_monthly_sales
file_path = 'data/ecommerce_transactions.txt'


def main():
    # 初始化绘图风格
    init_plot_style()
    # 日期转换
    df =  preprocess_data(load_ecommerce_data(file_path))
    # 画图
    plot_monthly_sales(df)

if __name__ == '__main__':
    main()
