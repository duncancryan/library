import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Frank Herbert", False)
author_repository.save(author1)

author2 = Author("J.R.R. Tolkien", False)
author_repository.save(author2)

author3 = Author("Andrzej Sapkowski", True)
author_repository.save(author3)

book1 = Book("The Fellowship of the Ring", author2, "Fantasy")
book2 = Book("Dune", author1, "Fantasy/SciFy")
book3 = Book("The Silmarillon", author2, "Fantasy")
book4 = Book("The Last Wish", author3, "Fantasy")
book5 = Book("Blood of Elves", author3, "Fantasy")
book6 = Book("Time of contempt", author3, "Fantasy")
book7 = Book("Lady of the Lake", author3, "Fantasy")
book8 = Book("Baptism of Fire", author3, "Fantasy")
book9 = Book("The tower of the Swallow", author3, "Fantasy")
book10 = Book("The Two Towers", author2, "Fantasy")
book11 = Book("The Return of the King", author2, "Fantasy")

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)
book_repository.save(book5)
book_repository.save(book6)
book_repository.save(book7)
book_repository.save(book8)
book_repository.save(book9)
book_repository.save(book10)
book_repository.save(book11)

pdb.set_trace()
