from typing import Union


class Pinnipeds:
    """Базовый класс, описывающий малый отряд ластоногих класса млекопитающих."""
    def __init__(self, name: str, mustache_length: Union[int, float], wool_length: str, wool_density: str,
                 body_length: Union[int, float], body_weight: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ластоногие"
        :param name: Название вида
        :param mustache_length: Длина усов в сантиметрах
        :param wool_length: Длина шерсти(качественная характеристика)
        :param wool_density: Густота шерсти(качественная характеристика)
        :param body_length: Длина тела в метрах
        :param body_weight: Масса тела в килограммах
        Примеры:
        #>>> pinniped = Pinnipeds('Морской котик', 33, 'длинная', 'густая', 2, 122)
        """
        self.name = name
        self.mustache_length = mustache_length
        self._wool_length = wool_length        # Сделан приватным для защиты неизменяемых данных о длине шерсти
        self._wool_density = wool_density      # Сделан приватным для защиты неизменяемых данных о густоте шерсти
        self.body_length = body_length
        self.body_weight = body_weight

    def __str__(self) -> str:
        return f'Ластоногое вида {self.name}, длина тела которого {self.body_length} м, а его масса {self.body_weight} кг'

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}(name={self.name!r}, mustache_length={self.mustache_length},
                wool_length={self.wool_length}, wool_density={self.wool_density}, body_length={self.body_length},
                body_weight={self.body_weight})"""

    @property
    def wool_length(self) -> str:
        """Возвращает качественную характеристику длины шерсти. Метод инкапсулирован с целью ограничить доступ
        пользователя к изменению приватного атрибута _wool_length, который отвечает за неизменную для вида качественную
        характеристику, и сохранить функционал вне класса."""
        return self._wool_length

    @property
    def wool_density(self) -> str:
        """Возвращает качественную характеристику густоты шерсти. Метод инкапсулирован с целью ограничить доступ
        пользователя к изменению приватного атрибута _wool_density, который отвечает за неизменную для вида качественную
        характеристику, и сохранить функционал вне класса."""
        return self._wool_density

    def body_index(self) -> Union[int, float]:
        """Высчитывает индекс массы тела для ластоногих. Метод придётся перегружать, так как длина и масса тела для
        каждого вида животных находятся в своих диапазонах. Сл-но, напутственный комментарий к ошибке значения нужен
        уникальный для каждого класса."""
        if not isinstance(self.body_length, (int, float)) or not isinstance(self.body_weight, (int, float)):
            raise TypeError("Длина и масса тела должны быть типа int или float.")
        if self.body_length <= 0 or self.body_weight <= 0:
            raise ValueError("Длина и масса тела должны быть строго положительными числами.")
        return self.body_weight/self.body_length**2


class NavySeals(Pinnipeds):
    """Класс, описывающий морских котиков"""
    MIN_LENGTH = 0.6
    MAX_LENGTH = 2.2
    MIN_WEIGHT = 5
    MAX_WEIGHT = 320

    def __init__(self, name: str, mustache_length: Union[int, float], wool_length: str, wool_density: str,
                 body_length: Union[int, float], body_weight: Union[int, float], diameter_auricle: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Морские котики"
        :param diameter_auricle: Диаметр ушной раковины в сантиметрах
        Примеры:
        #>>> pinniped = NavySeals('Арктический морской котик', 25, 'длинная', 'густая', 2, 289, 1)
        """
        super().__init__(name, mustache_length, wool_length, wool_density, body_length, body_weight)
        self.diameter_auricle = diameter_auricle

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}(name={self.name!r}, mustache_length={self.mustache_length!r},
                wool_length={self.wool_length!r}, wool_density={self.wool_density!r}, body_length={self.body_length!r},
                body_weight={self.body_weight!r}, diameter_auricle={self.diameter_auricle!r})"""

    def body_index(self) -> Union[int, float]:
        if not isinstance(self.body_length, (int, float)) or not isinstance(self.body_weight, (int, float)):
            raise TypeError("Длина и масса тела должны быть типа int или float.")
        if self.MAX_LENGTH < self.body_length < self.MIN_LENGTH or self.MAX_WEIGHT < self.body_weight < self.MIN_WEIGHT:
            raise ValueError("Длина морского котика варьируется от 0.6 до 2.2 м, а масса от 5 до 320 кг.")
        return self.body_weight/self.body_length**2


class SeaElephants(Pinnipeds):
    """Класс, описывающий морских слонов"""
    MIN_LENGTH = 1.25
    MAX_LENGTH = 6.5
    MIN_WEIGHT = 50
    MAX_WEIGHT = 5000

    def __init__(self, name: str, mustache_length: Union[int, float], wool_length: str, wool_density: str,
                 body_length: Union[int, float], body_weight: Union[int, float], trunk_length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Морские слоны"
        :param trunk_length: Длина хобота в сантиметрах
        Примеры:
        #>>> pinniped = SeaElephants('Южный морской слон', 10, 'короткая', 'густая', 5, 4200, 50)
        """
        super().__init__(name, mustache_length, wool_length, wool_density, body_length, body_weight)
        self.trunk_length = trunk_length

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}(name={self.name!r}, mustache_length={self.mustache_length!r}, 
                wool_length={self.wool_length!r}, wool_density={self.wool_density!r}, body_length={self.body_length!r}, 
                body_weight={self.body_weight!r}, trunk_length={self.trunk_length!r})"""

    def body_index(self) -> Union[int, float]:
        if not isinstance(self.body_length, (int, float)) or not isinstance(self.body_weight, (int, float)):
            raise TypeError("Длина и масса тела должны быть типа int или float.")
        if self.MAX_LENGTH < self.body_length < self.MIN_LENGTH or self.MAX_WEIGHT < self.body_weight < self.MIN_WEIGHT:
            raise ValueError("Длина морского слона варьируется от 1.25 до 6.5 м, а масса от 50 до 5000 кг.")
        return self.body_weight/self.body_length**2


class Walruses(Pinnipeds):
    """Класс, описывающий моржей"""
    MIN_LENGTH = 1.2
    MAX_LENGTH = 4.5
    MIN_WEIGHT = 70
    MAX_WEIGHT = 2000

    def __init__(self, name: str, mustache_length: Union[int, float], wool_length: str, wool_density: str,
                 body_length: Union[int, float], body_weight: Union[int, float], tusks_length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Моржи"
        :param tusks_length: Длина бивней в сантиметрах
        Примеры:
        #>>> pinniped = Walruses('Морж', 29, 'короткая', 'редкая', 3, 1800, 80)
        """
        super().__init__(name, mustache_length, wool_length, wool_density, body_length, body_weight)
        self.tusks_length = tusks_length

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}(name={self.name!r}, mustache_length={self.mustache_length!r},
                wool_length={self.wool_length!r}, wool_density={self.wool_density!r}, body_length={self.body_length!r}, 
                body_weight={self.body_weight!r}, tusks_length={self.tusks_length!r})"""

    def body_index(self) -> Union[int, float]:
        if not isinstance(self.body_length, (int, float)) or not isinstance(self.body_weight, (int, float)):
            raise TypeError("Длина и масса тела должны быть типа int или float.")
        if self.MAX_LENGTH < self.body_length < self.MIN_LENGTH or self.MAX_WEIGHT < self.body_weight < self.MIN_WEIGHT:
            raise ValueError("Длина моржа варьируется от 1.2 до 4.5 м, а масса от 70 до 2000 кг.")
        return self.body_weight/self.body_length**2


if __name__ == "__main__":
    kotik = NavySeals('Индийский морской котик', 33, 'длинная', 'густая', 1.5, 95, 1.2)
    print(kotik)
    print(repr(kotik))
    print(kotik.body_index())
    slon = SeaElephants('Американский морской слон', 10, 'короткая', 'густая', 3.8, 2500, 36)
    print(slon)
    print(repr(slon))
    print(slon.body_index())
    morj = Walruses('Морж', 25, 'короткая', 'редкая', 2.6, 1000, 56)
    print(morj)
    print(repr(morj))
    print(morj.body_index())
    pass
