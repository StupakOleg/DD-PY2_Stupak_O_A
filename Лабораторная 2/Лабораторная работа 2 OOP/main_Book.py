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
    def __init__(self, book_id: int, book_name: str, book_pages: int):
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [Book(book_id=book_dict["id"], book_name=book_dict["name"], book_pages=book_dict["pages"])
                  for book_dict in BOOKS_DATABASE]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
