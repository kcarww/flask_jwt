CREATE DATABASE db__flask;
USE db__flask;
CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(150) NOT NULL,
    password VARCHAR(50) NOT NULL,
    balance FLOAT NOT NULL DEFAULT 0
);