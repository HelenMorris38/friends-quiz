import psycopg2
from src.utils import connect_to_db, get_username
import pandas as pd


questions_df = pd.read_csv('friends_questions.csv')
data = questions_df.values.tolist()

username = get_username()
conn = connect_to_db(username)

cur = conn.cursor()

cur.executemany("INSERT INTO questions (question, answer) VALUES (%s, %s);", data)

conn.commit()
conn.close()

