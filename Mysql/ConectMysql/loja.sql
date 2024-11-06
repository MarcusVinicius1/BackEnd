USE loja;

CREATE TABLE cadastroproduto (
    Idproduto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Qtd INT NOT NULL,
    Preco DOUBLE NOT NULL
);

CREATE TABLE cadastrouser (
    Iduser INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Sobrenome VARCHAR(45) NOT NULL
);

CREATE TABLE admin (
    IdAdmin INT NOT NULL AUTO_INCREMENT,
    Cpf VARCHAR(11) UNIQUE PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Sobrenome VARCHAR(45) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Senha VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO cadastroproduto(Nome, Qtd, Preco) 
VALUES ("Pera", 100, 12.5),
	   ("Maca", 50, 7);
       
INSERT INTO cadastrouser(Nome, Sobrenome)
VALUES ("Marcus", "Barbosa"),
	   ("Vinicius", "Nascimento"),
       ("Caio", "Justino");
       
SELECT * FROM cadastroproduto;
