import psycopg2
from dotenv import load_dotenv
from os import environ

load_dotenv()

def get_username():
    try:
        username = environ.get('PG_USERNAME')
        return username
    except:
        return 'unable to get username'

def connect_to_db(username):
    try:
        conn = psycopg2.connect(dbname="friends_quiz", user=username)
        return conn
    except:
        return 'unable to connect to database'


# def load_data_frame_from_csv(filepath):
#     return pd.read_csv(f'{filepath}')

# def df_to_list_of_row_values(data_frame):
#     return data_frame.values.tolist()

def insert_data(conn, data):
    pass