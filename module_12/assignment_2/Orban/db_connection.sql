/*
    Title: whatabook_init.sql
    Author: Ben Orban
    Date: 29 April 2022
    Description: whatabook database initialization script.
*/


DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

--Insert Store
INSERT INTO store(locale)
    VALUES('123 Elm, Brighton, IL 62012');

INSERT INTO book(book_name, author, details)
    VALUES('The Shining', 'Stephen King', 'A scary story about ghosts');

INSERT INTO book(book_name, author, details)
    VALUES('Doctor Sleep', 'Stephen King', 'The sequel to The Shining');

INSERT INTO book(book_name, author, details)
    VALUES('The Green Mile', 'Stephen King', "A sad story about Jon Coffey");

INSERT INTO book(book_name, author)
    VALUES('Zen and the Art of Motorcycle Maintenance', 'Pirsig');

INSERT INTO book(book_name, author)
    VALUES('Dune', 'Frank Herbert');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');



INSERT INTO user(first_name, last_name) 
    VALUES('Danny', 'Torrance');

INSERT INTO user(first_name, last_name)
    VALUES('Harry', 'Potter');

INSERT INTO user(first_name, last_name)
    VALUES('Paul', 'Atreides');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Danny'), 
        (SELECT book_id FROM book WHERE book_name = 'The Shining')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'),
        (SELECT book_id FROM book WHERE book_name = 'Harry Potter')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Paul'),
        (SELECT book_id FROM book WHERE book_name = 'Dune')
    );