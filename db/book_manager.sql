DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    is_alive BOOLEAN

);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    author_id INT REFERENCES authors(id)
);

-- NOTE TO SELF!  ALWAYS USE   createdb database_name  in CONSOLE!  - to create the database before working on it
-- psql -d book_manager -f db/book_manager.sql in console to start