import pandas as pd

CW_DATA_FILENAME = 'cw_dataset.csv'
CW_MYDATA_FILENAME = 'my_borough.csv'
MY_LOCAL_AUTHORITY_HIGHWAY = 'E09000024'
COL_TO_FILTER_WITH = 'Local_Authority_Highway'

def dataframe_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def create_my_dataset_csv():
    df_all_data = dataframe_from_csv(CW_DATA_FILENAME)
    df_my_data = df_all_data[df_all_data[COL_TO_FILTER_WITH] == MY_LOCAL_AUTHORITY_HIGHWAY].copy()
    df_my_data.to_csv(CW_MYDATA_FILENAME, index=False)

def get_my_dataset() -> pd.DataFrame:
    return dataframe_from_csv(CW_MYDATA_FILENAME)