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
