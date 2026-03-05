DROP DATABASE bcd_musica;

CREATE DATABASE IF NOT EXISTS bcd_musica;

USE bcd_musica;

CREATE TABLE IF NOT EXISTS categoria (
 nome_genero VARCHAR(50) NOT NULL PRIMARY KEY,
 caminho_icone VARCHAR(255),
 cor VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 atividade BOOLEAN,
 nome_musica VARCHAR(50),
 caminho_capa VARCHAR(255),
 nome_genero VARCHAR(50),
 CONSTRAINT fk_categoria_musica FOREIGN KEY (nome_genero) REFERENCES categoria (nome_genero)
)

CREATE TABLE IF NOT EXISTS usuario (
 usuario VARCHAR(50) PRIMARY KEY,
 senha VARCHAR(50)
)
