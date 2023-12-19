1. Criando um banco de dados:

CREATE DATABASE Newbank;

2. Conectando-se ao banco de dados:

USE Newbank;

3. Criando a tabela:

CREATE TABLE Produtos (
    produto_id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    preço DECIMAL(10, 2)
);

4. Criando a tabela de Histórico:
CREATE TABLE Historico (
    ação VARCHAR(10),
    produto_id INT,
    nome_anterior VARCHAR(50),
    preço_anterior DECIMAL(10, 2),
    data_registro TIMESTAMP
);

5. Criando um trigger:

CREATE OR REPLACE FUNCTION registrar_mudanca_produto()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Historico (ação, produto_id, nome_anterior, preço_anterior, data_registro)
    VALUES (
        'Inserção',
        NEW.produto_id,
        NULL,
        NULL,
        NOW()
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_registro_produto
AFTER INSERT
ON Produtos
FOR EACH ROW
EXECUTE FUNCTION registrar_mudanca_produto();

6. Inserir um novo produto:

INSERT INTO Produtos (nome, preço) VALUES ('Vestido', 35.00);