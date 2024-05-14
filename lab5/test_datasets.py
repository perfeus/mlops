import pandas as pd
df = pd.read_csv("insurance/insurance.csv")


def check_missing_values(df):
    return df.isnull().sum().sum()

def test_check_missing_values():
    assert check_missing_values(df) == 0

def get_column_names(df):
    return df.columns.to_list()

def test_get_column_names():
    assert get_column_names(df) == ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

def get_data_types(df):
    return [dtype.name for dtype in df.dtypes]

def test_check_data_type():
    assert get_data_types(df) == ['int64', 'object', 'float64', 'int64', 'object', 'object', 'float64']

def check_duplicates(df):
    return df.duplicated().sum()

def test_check_duplicates():
    assert check_duplicates(df) == 1
