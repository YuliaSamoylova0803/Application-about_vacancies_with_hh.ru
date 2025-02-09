import json
from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл"""

    @abstractmethod
    def add_vacancies_to_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

class JSONSaver(Saver):
    """ Класс для работы с файлами (vacancy_list из класса HeadHunterAPI) """
    def __init__(self, path: str = "data/vacancy_list_json.json"):
        self.__path = path
        self.info_about_vacancies = []

    # блок функций для добавления в файлы
    def add_vacancies_to_file(self, vacancies: list[dict]):
        """ Функция добавляет данные формата json в файл"""

        with open(self.__path, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=4)

    # блок функций для чтения из файла

    def read_data_json(self):
        """ Чтение json файла """
        with open(self.__path, 'r', encoding='utf-8') as json_file:
            data_from_hh = json.load(json_file)
            return data_from_hh



    def delete_vacancy(self):
        pass


if __name__ == "__main__":
    # Сохранение информации о вакансиях в файл
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                      "Требования: опыт работы от 3 лет...")

    json_saver = JSONSaver("save_vacancy.json")
    json_saver.add_vacancies_to_file(vacancy)
    print(json_saver.read_data_json())