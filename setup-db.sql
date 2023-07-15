--- create database

DROP DATABASE IF EXISTS friends_quiz;
CREATE DATABASE friends_quiz;

\c friends_quiz

CREATE TABLE questions (
    questions_id SERIAL PRIMARY KEY,
    question VARCHAR,
    answer VARCHAR
);


