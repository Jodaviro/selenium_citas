--- Para ejercicio sql que no tiene nada que ver con el ejercicio con selenium

CREATE TABLE IF NOT EXISTS books (
	book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	author_id INTEGER UNSIGNED,
	tittle VARCHAR(100) NOT NULL,
	year INTEGER UNSIGNED NOT NULL DEFAULT 1900,
	language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 639-1 Language',	
	cover_url VARCHAR(500),
	price DOUBLE NOT NULL DEFAULT 10.0,
	sellable TINYINT DEFAULT 1,
	copies INTEGER NOT NULL DEFAULT 1,
	description TEXT
);

CREATE TABLE IF NOT EXISTS authors (
	author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	nationality VARCHAR(3)
);

CREATE TABLE clients(
	client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR (50) NOT NULL, 
	email VARCHAR (100) NOT NULL UNIQUE,
	birthdate DATETIME,
	gender ENUM('M','F','ND') NOT NULL,
	active TINYINT NOT NULL DEFAULT 1,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS operation (
	operation_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
	book_id INTEGER UNSIGNED NOT NULL,
	client_id INTEGER UNSIGNED NOT NULL,
	`type` ENUM ('S', 'B', 'R') NOT NULL COMMENT 'S= Sold, B= Borrowed, R= Returned',
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	finished TINYINT NOT NULL DEFAULT 0
);

INSERT INTO authors (author_id, name, nationality)
VALUES ( NULL,'Juan Rulfo', 'MEX');

INSERT INTO authors (name, nationality)
VALUES ('Gabriel Garcia Marquez', 'COL' );

INSERT INTO authors VALUES (0, 'Juan Gabriel Vasquez', 'COL');

INSERT INTO books ()

SELECT name, email, YEAR(NOW())- YEAR(birthdate) AS edad, gender 
FROM clients
WHERE gender='F'
	AND name LIKE '%Lop%'

SELECT b.book_id,a.name, a.author_id, b.title
FROM books AS b
JOIN authors as a 
	on a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 and 5;

SELECT t.type, b.title, c.name
FROM transactions AS t
JOIN books as b 
	on t.book_id = b.book_id
JOIN clients AS c 
	on t.client_id = c.client_id 

--mismo query con mas opciones
SELECT t.type, b.title,a.name AS author, c.name
FROM transactions AS t
JOIN books as b 
	on t.book_id = b.book_id
JOIN clients AS c 
	on t.client_id = c.client_id 
JOIN authors AS a 
	on b.author_id= a.author_id
WHERE C.gender='M' 
AND t.type IN ('sell', 'lend');

---
SELECT b.title, a.name
FROM authors AS a, books AS b 
WHERE a.author_id = b.author_id
LIMIT 10

SELECT b.title, a.name
FROM books AS b  
JOIN authors as A
	on a.author_id = b.author_id
;

SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a 
JOIN books AS b 
	on a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 and 5
ORDER BY a.name DESC;

--- Left join ejemplo. trae los autores que no tengan libros asociados.
SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a 
LEFT JOIN books AS b 
	on a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 and 5
ORDER BY a.author_id;
----funcion count() y GROUP BY
SELECT a.author_id, a.name, a.nationality, COUNT(b.book_id) AS obras
FROM authors AS a 
LEFT JOIN books AS b 
	on a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 and 5
GROUP BY a.author_id
ORDER BY a.author_id;
----experimento propio con COUNT() para conocer la cantidad de nacionalidades de authores
---- asociada a los libros existentes
SELECT a.nationality, COUNT(a.nationality) as cantidad
FROM authors AS a 
LEFT JOIN books AS b
	ON b.author_id = a.author_id
GROUP BY a.nationality
ORDER BY a.nationality DESC;
---ejerciicio de la clase cuantos libros hay de cada nacionalidad
SELECT a.nationality, COUNT(a.nationality) as cantidad
FROM books AS b  
JOIN authors AS a
	ON b.author_id = a.author_id
GROUP BY a.nationality
ORDER BY a.nationality DESC;
---contar todas las nacionalidades de la tabla authors
SELECT a.nationality, COUNT(a.author_id) AS cantidad
FROM authors AS a 
GROUP BY a.nationality
ORDER BY cantidad DESC, a.nationality ASC;
--- misma tabla pero con datos mas o menos especificos
SELECT a.nationality, COUNT(a.author_id) AS cantidad
FROM authors AS a 
WHERE a.nationality IN ('USA', 'RUS') --- tambien puede ser IS NOT para filtrar datos especificos
GROUP BY a.nationality
ORDER BY cantidad DESC, a.nationality ASC;
--el DISTINC es una opcion para agrupar similares
SELECT DISTINCT price 
FROM books
ORDER by price DESC;
--- El AVG() es una funcion permite traer el promedio de precios
SELECT AVG (price) 
FROM books
--- El STDDEV() estandard deviation no n
SELECT a.nationality, 
	COUNT(b.book_id) AS libros, 
	AVG(b.price) AS promedio, 
	STDDEV(b.price) AS std
FROM books as b 
JOIN authors as a
	on a.author_id = b.author_id
GROUP BY a.nationality
ORDER BY libros DESC;
---MAX() Y MIN() son funciones
SELECT nationality, MAX(price), MIN(price)
FROM books AS b
JOIN authors AS a 
	ON a.author_id = b.author_id
GROUP BY nationality;
--- CONCAT Y TO_DAYS
SELECT c.name, t.type, b.title, 
	CONCAT( a.name, " (", a.nationality, ")") AS author,
	TO_DAYS(NOW()) - TO_DAYS(t.created_at) AS ago
FROM transactions AS t 
LEFT JOIN clients AS c 
	ON t.client_id = c.client_id
LEFT JOIN books as b 
	ON b.book_id= t.book_id
LEFT JOIN authors AS a 
	ON b.author_id = a.author_id
---
-- ------------------------------------------------------


