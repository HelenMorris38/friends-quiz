import pandas as pd


def load_data_frame_from_csv(filepath):
    return pd.read_csv(f'{filepath}')

def df_to_list_of_row_values(data_frame):
    return data_frame.values.tolist()

def insert_data(conn, data):
    pass