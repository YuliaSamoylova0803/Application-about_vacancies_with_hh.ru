from src.headhunter_api import HeadHunterAPI
from src.saver import JSONSaver


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
            return f'Требования не указаны'
        else:
            return f'{value}'

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
            return 0

    @classmethod
    def getting_vacancy_data(cls, data_from_hh: list):
        """Метод получения данных о вакансии их JSON-ответа в список объекта"""

        if isinstance(data_from_hh, list):

            vacancies_list = []
            for i in data_from_hh:
                if i["salary"] is None:
                    currency = ''
                else:
                    currency = i["salary"]["currency"]

                vacancies_list.append(cls(name=i["name"],
                                          city=i["area"]["name"],
                                          responsibility=i["snippet"]["responsibility"],
                                          salary=i["salary"],
                                          currency=currency,
                                          url=i["alternate_url"]))

            if len(vacancies_list) == 0 or vacancies_list is None:
                return f"Неверный формат данных"

            return vacancies_list
        else:
            return f"Неверный формат данных"

    def __eq__(self, other):
        """Магический метод сравнения ="""
        return self.salary == other.salary

    def __lt__(self, other):
        """ Магический метод сравнения <"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод сравнения >"""

        return self.salary > other.salary

    def __str__(self):
        if self.salary == 0:
            self.salary = f"Зарплата не указана"
        return (f"Название вакансии: {self.name}\n"
                f"Город: {self.city}\n"
                f"Обязанности: {self.responsibility}\n"
                f"Зарплата: {self.salary} {self.currency}\n"
                f"Ссылка: {self._url}\n")

    def __repr__(self):
        """
        Отображение информации о класса для разработчика
        :return:
        """
        return (
            f'Имя класса: {self.__class__.__name__}. Атрибуты класса: ({self.name}, {self.city}, '
            f'{self.responsibility}, {self.salary}, {self._url})\n')


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancy = Vacancy("Python Developer", "Moscom" ,  "100 000-150 000 руб.", hh_api.vacancies, )
    print(vacancy)

    #print(hh_api)
    # Получение вакансий с hh.ru в формате JSON
    data_from_hh = hh_api._load_vacancies("Python")
    print(type(data_from_hh))
    json_saver = JSONSaver("data/vacancy_list_json.json")
    json_saver.add_vacancies_to_file()
    #print(hh_vacancies)
    print(vacancy.__getting_vacancy_data(data_from_hh))





























