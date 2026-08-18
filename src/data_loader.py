import pandas as pd


def load_ecommerce_data(file_path: str) -> pd.DataFrame:
    """
    读取电商交易数据集
    :param file_path:数据文件路径
    :return:加载完成的DataFrame
    """
    columns = ['user_id', 'order_dt', 'order_products', 'order_amount']
    df = pd.read_csv(file_path, names=columns, sep=r'\s+', header=None)
    return df
