Criando o banco de dados de uma escola:

CREATE DATABASE ESCOLA;

Usando o banco de dados recém-criado:

USE ESCOLA;

Criando a tabela ALUNO e a chave primária:

CREATE TABLE ALUNO (
    ID SERIAL PRIMARY KEY,
    nome VARCHAR(60),
    email VARCHAR(115),
    endereco VARCHAR(185)
);