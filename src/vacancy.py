class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "city", "salary", "currency", "responsibility", "_url")

    def __init__(self, name, city, salary, currency, responsibility, url):

        # Атрибуты класса Vacancy
        self.name = name
        self.city = city
        self.salary = self.check_salary(salary)
        self.currency = currency
        self.responsibility = self.check(responsibility)
        self._url = url

    @staticmethod
    def check(value):
        """
        Проверка значений атрибутов класса на None
        :param value:
        :return:
        """
        if value is None:
            return f"Требования по {value} не указаны"
        else:
            return f"{value}"

    @staticmethod
    def check_salary(value):
        """
        Функция используется для проверки значений атрибута класса salary на None
        :param value:
        :return:
        """
        if isinstance(value, dict):
            if value["from"] is None:
                return int(value["to"])

            elif value["to"] is None:
                return int(value["from"])
            else:
                return (int(value["from"]) + int(value["to"])) / 2
        else:
            return value

    @classmethod
    def getting_vacancy_data(cls, data_from_hh: list):
        """Метод получения данных о вакансии их JSON-ответа в список объекта"""

        if isinstance(data_from_hh, list):

            vacancies_list = []
            for i in data_from_hh:
                if i["salary"] is None:
                    currency = ""
                else:
                    currency = i["salary"]["currency"]

                vacancies_list.append(
                    cls(
                        name=i["name"],
                        city=i["area"]["name"],
                        responsibility=i["snippet"]["responsibility"],
                        salary=i["salary"],
                        currency=currency,
                        url=i["alternate_url"],
                    )
                )

            if len(vacancies_list) == 0 or vacancies_list is None:
                return "Неверный формат данных"

            return vacancies_list
        else:
            return "Неверный формат данных"

    def __eq__(self, other):
        """Магический метод сравнения ="""
        return self.salary == other.salary

    def __lt__(self, other):
        """Магический метод сравнения <"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод сравнения >"""
        return self.salary > other.salary

    def __str__(self):
        if self.salary == 0:
            self.salary = "Зарплата не указана"
        return (
            f"Название вакансии: {self.name}\n"
            f"Город: {self.city}\n"
            f"Обязанности: {self.responsibility}\n"
            f"Зарплата: {self.salary} {self.currency}\n"
            f"Ссылка: {self._url}\n"
        )

    def __repr__(self):
        """
        Отображение информации о класса для разработчика
        :return:
        """
        return (
            f"Имя класса: {self.__class__.__name__}. Атрибуты класса: Название:({self.name}, Город:{self.city}, "
            f"Обязанности: {self.responsibility},  Зарплата: {self.salary}, Ссылка: {self._url})\n"
        )
