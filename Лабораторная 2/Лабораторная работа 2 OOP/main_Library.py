BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, book_id: int = None, book_name: str = None, book_pages: int = None):
        """
        Создание и подготовка к работе объекта "Книга"
        :param book_id: Идентификатор книги
        :param book_name: Название книги
        :param book_pages: Количество страниц в книге
        """
        if not isinstance(book_id, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        self.id = book_id
        if not isinstance(book_name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = book_name
        if not isinstance(book_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        self.pages = book_pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, list_of_books: list = []):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param list_of_books: Список книг
        """
        if not isinstance(list_of_books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = list_of_books

    def get_next_book_id(self) -> int:
        if self.books == ():
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, our_book_id: int) -> int:
        if not isinstance(our_book_id, int):
            raise TypeError("Id книги должен быть типа int")
        if self.books[our_book_id - 1] is None:
            raise ValueError("Книги с запрашиваемым id не существует")
        return our_book_id - 1


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [Book(book_id=book_dict["id"], book_name=book_dict["name"], book_pages=book_dict["pages"])
                  for book_dict in BOOKS_DATABASE]
    library_with_books = Library(list_of_books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
