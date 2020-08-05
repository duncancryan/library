from db.run_sql import run_sql
from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors (name, is_alive) VALUES (%s, %s) RETURNING *"
    values = [author.name, author.is_alive]
    results = run_sql(sql,values)
    id = results[0]['id']
    author.id = id
    return author


def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['is_alive'], row['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'],result['is_alive'],result['id'])
    return author


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM authors WHERE (id) = (%s)" # do we need () on single items ?
    values = [id]
    run_sql(sql,values)

def update(author):
    sql = "UPDATE authors SET (name, is_alive) = (%s, %s) WHERE id = %s"
    values = [author.name, author.is_alive, author.id]
    run_sql(sql, values)

def books(author):
    books =[]

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql,values)

    for row in results:
        book = Book(row['title'],row['author_id'],row['genre'],row['id']) # Why are we not using row['author'] ??? what is this sorcery? 
        books.append(book)
    return books

