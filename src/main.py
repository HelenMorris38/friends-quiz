import psycopg2
from src.utils import load_data_frame_from_csv, df_to_list_of_row_values
from dotenv import load_dotenv
from os import environ

load_dotenv()

questions_df = load_data_frame_from_csv('friends_questions.csv')
data = df_to_list_of_row_values(questions_df)
username = environ.get('PG_USERNAME')
conn = psycopg2.connect(dbname="friends_quiz", user=username)

cur = conn.cursor()

cur.executemany("INSERT INTO questions (question, answer) VALUES (%s, %s);", data)


conn.commit()
conn.close()

