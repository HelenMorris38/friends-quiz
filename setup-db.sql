--- create database

DROP DATABASE IF EXISTS friends_quiz;
CREATE DATABASE friends_quiz;

\c friends_quiz

DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
    question_id SERIAL PRIMARY KEY,
    question VARCHAR,
    answer VARCHAR
);

COPY questions(question,answer)
FROM '/Users/helenmorris/Documents/personal-projects/friends-quiz/friends_questions - Sheet1.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM questions;
