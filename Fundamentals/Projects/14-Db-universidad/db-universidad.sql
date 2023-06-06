CREATE DATABASE IF NOT EXISTS 	universidad;
USE universidad;

-- =DROP TABLE IF EXISTS universidad;

CREATE TABLE estudiantes (
estudiante_id INT AUTO_INCREMENT primary key,
nombre varchar(255),
apellido varchar(255),
carrera varchar(255),
edad int
);
