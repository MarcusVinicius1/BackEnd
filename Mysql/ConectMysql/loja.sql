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

INSERT INTO cadastroproduto(Nome, Qtd, Preco) 
VALUES ("Pera", 100, 12.5),
	   ("Maca", 50, 7);
       
INSERT INTO cadastrouser(Nome, Sobrenome)
VALUES ("Marcus", "Barbosa"),
	   ("Vinicius", "Nascimento"),
       ("Caio", "Justino");
       
SELECT * FROM cadastroproduto;