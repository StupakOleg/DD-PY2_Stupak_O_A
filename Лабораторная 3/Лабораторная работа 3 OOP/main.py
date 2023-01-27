class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Устанавливает название книги."""
        if not isinstance(new_name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = new_name

    @property
    def author(self) -> str:
        """Возвращает имя автора книги."""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Устанавливает имя автора книги."""
        if not isinstance(new_author, str):
            raise TypeError("Имя автора книги должно быть типа str")
        self._author = new_author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int.")
        if new_pages <= 0:
            raise ValueError("Количество страниц в книге должно быть строго положительным числом.")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        """Возвращает длительность книги в минутах."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает длительность книги в минутах."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float.")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть строго положительным числом.")
        self._duration = new_duration


book1 = PaperBook('Книга о вкусной и здоровой пище', "Н.П. Могильный", 440)
book2 = AudioBook('Книга о вкусной и здоровой пище', "Н.П. Могильный", 253.44)
print(book1)
print(repr(book1))
print(book2)
print(repr(book2))
