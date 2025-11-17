# SQL 데이터 생성 (db_init/init.sql)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
INSERT INTO users (name) VALUES ('Alice (From DB)');
INSERT INTO users (name) VALUES ('Bob (From DB)');
INSERT INTO users (name) VALUES ('Carol (From DB)');