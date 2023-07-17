import pandas as pd

def load_data_frame_from_csv(filepath):
    return pd.read_csv(f'{filepath}')