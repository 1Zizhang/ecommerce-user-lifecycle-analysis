import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    日期转换函数
    :param df:待处理的日期字段
    :return: DataFrame
    """
    df['order_date'] = pd.to_datetime(df['order_dt'], format='%Y%m%d')
    df['month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    return df
