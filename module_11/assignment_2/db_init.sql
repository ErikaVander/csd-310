DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

DROP DATABASE IF EXISTS whatabook;
CREATE DATABASE whatabook;

USE whatabook;

CREATE TABLE user(
	user_id INT NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(75) NOT NULL, 
    last_name VARCHAR(75) NOT NULL, 
    PRIMARY KEY(user_id)
);

CREATE TABLE book(
	book_id INT NOT NULL AUTO_INCREMENT, 
    PRIMARY KEY(book_id), 
    book_name VARCHAR(200) NOT NULL, 
    description VARCHAR(500), 
    author VARCHAR(200) NOT NULL
);

CREATE TABLE wishlist(
	wishlist_id INT NOT NULL AUTO_INCREMENT, 
    PRIMARY KEY(wishlist_id), 
    user_id INT NOT NULL, 
    CONSTRAINT fk_user FOREIGN KEY(user_id) 
		REFERENCES user(user_id), 
	book_id INT NOT NULL, 
    CONSTRAINT fk_book FOREIGN KEY(book_id) 
		REFERENCES book(book_id)
);

CREATE TABLE store(
	store_id INT NOT NULL,
    PRIMARY KEY (store_id),
    locale_first_line VARCHAR(500) NOT NULL,
    locale_second_line VARCHAR(500) NOT NULL,
    hours VARCHAR(200) NOT NULL
);

INSERT INTO store(store_id, locale_first_line, locale_second_line, hours) 
	VALUES ('1', '0001 NE 100 Pl.', 'Shire, Middle Earch 98001', 'Mon-Fri, 9:00-5:00');
    
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('1000', 'Hobbit', 'An adventure book with elves, hobbits, and dwarves, a prequal to Lord of the Rings.', 'J.R.R. Tolkein');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('2000', 'Lord of the Rings', 'An adventure book with elves, hobbits, kings, and dwarves.', 'J.R.R. Tolkein');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('3000', 'Fellowship of the Ring', 'An adventure book with elves, hobbits, kings, and dwarves, second book of the series.', 'J.R.R. Tolkein');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('4000', 'Return of the King', 'An adventure book with elves, hobbits, kings, and dwarves, third book of the series.', 'J.R.R. Tolkein');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('5000', 'The Magicians Nephew', 'An adventure book about two children discovering new worlds and getting to take part of the creation and protection of a new one.', 'C.S. Lewis');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('6000', 'The Lion the Witch and the Wardrobe', 'An adventure book about four children discovering new world in which they meet Aslan, the Lion above all Lions who will help them save that world from a century old evil.', 'C.S. Lewis');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('7000', 'The Horse and His Boy', 'An adventure book about a boy who must discover who he truely is by trusting a horse who can, of all the unlikelythings, talk.', 'C.S. Lewis');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('8000', 'Prince Caspian', 'A young prince must gain the trust of creatures and his people have tourmented for years, and four legendary young rulers from another world, in order to save all from his evil uncle.', 'C.S. Lewis');
INSERT INTO book(book_id, book_name, description, author) 
	VALUES ('9000', 'The Voyage of the Dawn Treader', 'A young king has won peace for Narnia, or so he thinks until he discovers an evil presence growing stronger at the border islands of his kingdom. A young legendary queen, a young legendary king, and a stuck up boy, all from the mysterious world of England will be necessary to solve and reverse the evil curse.', 'C.S. Lewis');
    
INSERT INTO user(user_id, first_name, last_name) 
	VALUES('1', 'Lucy', 'Pevensie');
INSERT INTO user(first_name, last_name) 
	VALUES('Samwise', 'Gamgee');
INSERT INTO user(first_name, last_name) 
	VALUES('Reepicheep', 'Mouse');

INSERT INTO wishlist(wishlist_id, user_id, book_id) 
	VALUES('1', '1', '9000');
INSERT INTO wishlist(user_id, book_id) 
	VALUES('2', '6000');
INSERT INTO wishlist(user_id, book_id) 
	VALUES('3', '2000');