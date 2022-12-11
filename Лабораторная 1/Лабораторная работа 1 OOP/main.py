import doctest
from typing import Union


class Assortment:
    def __init__(self, category_name: str, product_name: str,
                 product_quantity: Union[int, float], product_measurement: str):
        """
        Создание и подготовка к работе объекта "Ассортимент"
        :param category_name: Категория товара
        :param product_name: Наименование товара
        :param product_quantity : Количество товара в наличии
        :param product_measurement : Единица измерения количества товара(т, кг, л, шт и т.д.).
         Названия единиц измерения можно не сокращать.
        Примеры:
        >>> product = Assortment('Овощи', 'Помидоры', 1.5, 'тонна')
        """
        if not isinstance(category_name, str):
            raise TypeError("Категория товара должна быть типа str")
        self.category = category_name
        if not isinstance(product_name, str):
            raise TypeError("Наименование товара должно быть типа str")
        self.product = product_name
        if not isinstance(product_quantity, (int, float)):
            raise TypeError("Количество товара должно быть типа int или float")
        if product_quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        self.quantity = product_quantity
        if not isinstance(product_measurement, str):
            raise TypeError("Единица измерения количества товара должна быть типа str")
        self.measurement = product_measurement

    def sale(self, quantity_of_sales: Union[int, float], sale_measurement: str) -> None:
        """
        Функция, которая вычитает количество проданного товара из количества товара в наличии.
        :param quantity_of_sales: Количество проданного товара
        :param sale_measurement: Единица измерения количества проданного товара
        Примеры:
        >>> product = Assortment('Крупы', 'Гречка', 1500, 'упаковка 900г')
        >>> product.sale(679, 'упаковка 900г')
        """
        if not isinstance(quantity_of_sales, (int, float)):
            raise TypeError("Количество проданного товара должно быть типа int или float")
        if quantity_of_sales < 0:
            raise ValueError("Количество проданного товара не может быть отрицательным")
        if not isinstance(sale_measurement, str):
            raise TypeError("Единица измерения количества проданного товара должна быть типа str")
        if sale_measurement != self.measurement:
            raise ValueError("Единицы измерения количества проданного товара и количества в наличии должны совпадать")
        ...

    def shipment(self, shipment_quantity: Union[int, float], shipment_measurement: str) -> None:
        """
        Функция, которая прибавляет количество закупленного товара к количеству товара в наличии.
        :param shipment_quantity: Количество закупленного товара
        :param shipment_measurement: Единица измерения количества закупленного товара
        Примеры:
        >>> product = Assortment('Молочка', 'Кефир', 890, 'упаковка 1л')
        >>> product.shipment(130, 'упаковка 1л')
        """
        if not isinstance(shipment_quantity, (int, float)):
            raise TypeError("Количество закупленного товара должно быть типа int или float")
        if shipment_quantity < 0:
            raise ValueError("Количество закупленного товара не может быть отрицательным")
        if not isinstance(shipment_measurement, str):
            raise TypeError("Единица измерения количества закупленного товара должна быть типа str")
        if shipment_measurement != self.measurement:
            raise ValueError("Единицы измерения количества закупленного товара и количества в наличии должны совпадать")
        ...


class Staff:
    def __init__(self, employee_job: str, employee_name: str,
                 employee_age: int, employee_work_experience: int, employee_education: str):
        """
        Создание и подготовка к работе объекта "Персонал"
        :param employee_job: Профессия
        :param employee_name: Имя
        :param employee_age : Возраст
        :param employee_work_experience : Стаж работы
        :param employee_education : Сведения об образовании
        Примеры:
        >>> employee = Staff('Кассир', 'Галина', 57, 18, 'Среднее специальное')
        """
        if not isinstance(employee_job, str):
            raise TypeError("Название профессии должно быть типа str")
        self.job = employee_job
        if not isinstance(employee_name, str):
            raise TypeError("Имя сотрудника должно быть типа str")
        self.name = employee_name
        if not isinstance(employee_age, int):
            raise TypeError("Возраст должен быть типа int")
        if employee_age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = employee_age
        if not isinstance(employee_work_experience, int):
            raise TypeError("Стаж должен быть типа int")
        if employee_work_experience < 0:
            raise ValueError("Стаж не может быть отрицательным")
        self.work_experience = employee_work_experience
        if not isinstance(employee_education, str):
            raise TypeError("Сведения об образовании должны быть типа str")
        self.education = employee_education

    def recruitment(self) -> None:
        """
        Функция, которая добавляет сотрудника в список персонала(создать заранее)
        Примеры:
        >>> employee = Staff('Электрик', 'Тимофей', 39, 8, 'Среднее специальное')
        >>> employee.recruitment()
        """
        ...

    def dismissal(self) -> None:
        """
        Функция, которая удаляет сотрудника из списка персонала
        Примеры:
        >>> employee = Staff('Грузчик', 'Игнат', 20, 2, 'Среднее общее образование')
        >>> employee.dismissal()
        """
        ...


class AccountsDepartment:
    def __init__(self, shop_revenue: Union[int, float],
                 shop_expenses: Union[int, float], revenue_growth: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Бухгалтерия"
        :param shop_revenue: Выручка за месяц
        :param shop_expenses: Расходы за месяц
        :param revenue_growth : Рост выручки в месяц
        Примеры:
        >>> count = AccountsDepartment(137500, 120689.8, 0.05)
        """
        if not isinstance(shop_revenue, (int, float)):
            raise TypeError("Выручка должна быть типа int или float")
        if shop_revenue < 0:
            raise ValueError("Выручка не может быть отрицательной")
        self.revenue = shop_revenue
        if not isinstance(shop_expenses, (int, float)):
            raise TypeError("Расходы должны быть типа int или float")
        if shop_expenses < 0:
            raise ValueError("Расходы не могут быть отрицательными")
        self.expenses = shop_expenses
        if not isinstance(revenue_growth, (int, float)):
            raise TypeError("Рост выручки в месяц должен быть типа int или float")
        self.growth = revenue_growth

    def shop_profit(self) -> Union[int, float]:
        """
        Функция, которая высчитывает прибыль за месяц
        :return: Прибыль за месяц
        Примеры:
        >>> count = AccountsDepartment(110568, 136000, 0.15)
        >>> count.shop_profit()
        """
        ...

    def growth_profit(self) -> Union[int, float]:
        """
        Функция, которая высчитывает рост прибыли в месяц
        :return: Рост прибыли в месяц
        Примеры:
        >>> count = AccountsDepartment(125879, 250879, 0.15)
        >>> count.shop_profit()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
