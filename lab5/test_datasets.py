import pandas as pd # to work with tabular data
df = pd.read_csv("insurance/insurance.csv") # to load the dataset


def check_missing_values(df):
    """
    Check the number of missing values in the dataset
    """
    return df.isnull().sum().sum()

def test_check_missing_values():
    """
    Test the check_missing_values function
    """
    assert check_missing_values(df) == 0

def get_column_names(df):
    """
    Get the names of the columns in the dataset
    """
    return df.columns.to_list()

def test_get_column_names():
    """
    Test the get_column_names function
    """
    assert get_column_names(df) == ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

def get_data_types(df):
    """
    Get the data types of the columns in the dataset
    """
    return [dtype.name for dtype in df.dtypes]

def test_check_data_type():
    """
    Test the get_data_types function
    """
    assert get_data_types(df) == ['int64', 'object', 'float64', 'int64', 'object', 'object', 'float64']

def check_duplicates(df):
    """
    Check the number of duplicate rows in the dataset
    """
    return df.duplicated().sum()

def test_check_duplicates():
    """
    Test the check_duplicates function
    """
    assert check_duplicates(df) == 1
