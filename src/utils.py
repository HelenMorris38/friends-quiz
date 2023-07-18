import pandas as pd
import psycopg2


def connect_to_db():
    try:
        conn = psycopg2.connect("dbname=friends_quiz user=helenmorris")
        return conn
    except:
        return 'unable to connect to database'


def load_data_frame_from_csv(filepath):
    return pd.read_csv(f'{filepath}')

def df_to_list_of_row_values(data_frame):
    return data_frame.values.tolist()

def insert_data(conn, data):
    pass