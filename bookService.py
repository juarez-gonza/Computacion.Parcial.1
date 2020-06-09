from repository import Repository


class BookService:

    id_counter = 1

    def __init__(self):
        pass

    def add_book(self, book):
        book.id = BookService.id_counter
        Repository.booksList[BookService.id_counter] = book.__dict__
        BookService.id_counter += 1
        return book.id

    def update_book(self, book_key, updatedBook):
        try:
            if book_key == 0 or book_key > BookService.id_counter:
                raise KeyError
            Repository.booksList[book_key] = updatedBook.__dict__
        except KeyError:
            raise ValueError

    def assign_book(self, book_key, member_id):
        try:
            if book_key == 0 or book_key > BookService.id_counter:
                raise KeyError
            book = Repository.booksList[book_key]
            book["memberLegajo"] = member_id
        except KeyError:
            raise ValueError
