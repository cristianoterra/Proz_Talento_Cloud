1. Criando um banco de dados em PostgreSQL:

CREATE DATABASE ExemploDB;

2. Conectando-se ao banco de dados recém-criado:

USE ExemploDB;

3. Criando tabelas e adicione atributos:

CREATE TABLE Pessoas (
    pessoa_id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    idade INT
);

CREATE TABLE Pedidos (
    pedido_id SERIAL PRIMARY KEY,
    pessoa_id INT,
    produto VARCHAR(50),
    valor DECIMAL(10, 2),
    FOREIGN KEY (pessoa_id) REFERENCES Pessoas(pessoa_id)
);

4. Insirindo dados nas tabelas:

INSERT INTO Pessoas (nome, idade) VALUES
('Isabella', 5),
('Lucas', 1);

INSERT INTO Pedidos (pessoa_id, produto, valor) VALUES
(1, 'Vestido', 35.00),
(1, 'Calcinha', 20.00),
(2, 'Cueca', 15.00);

5. Usando comandos JOIN para realizar consultas nas tabelas:

As consultas em PostgreSQL:

- Para obter informações de pedidos de pessoas:

SELECT Pessoas.nome, Pedidos.produto, Pedidos.valor
FROM Pessoas
INNER JOIN Pedidos ON Pessoas.pessoa_id = Pedidos.pessoa_id;

- Para calcular o total de gastos de cada pessoa:

SELECT Pessoas.nome, SUM(Pedidos.valor) AS total_gasto
FROM Pessoas
LEFT JOIN Pedidos ON Pessoas.pessoa_id = Pedidos.pessoa_id
GROUP BY Pessoas.nome;