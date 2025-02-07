
class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("name", "url", "salary", "description")
    name: str
    url: str
    salary: str
    description: str

    def __init__(self, name, url, salary, description):

        # Атрибуты класса Vacancy
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description


    def validate_salary(self, salary):
        """Метод валидации зарплаты(проверка на None из апи запроса HeadHunter)"""
        if salary is None:
            return "Зарплата не указана"
        return 0


    def __str__(self):
        """Вывод строки """
        return f"{self.name}, {self.url}, заработная плата от {self.salary}"

    def __eq__(self, other):
        """Магический метод сравнения ="""
        return self.salary == other.salary

    def __lt__(self, other):
        """ Магический метод сравнения <"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод сравнения >"""

        return self.salary > other.salary

    def cast_to_object_list(self):
        pass


if __name__ == "__main__":
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>" ,  "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    print(vacancy)



























