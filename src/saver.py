import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл"""

    @abstractmethod
    def add_vacancies_to_file(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Saver):
    """Класс для работы с файлами (vacancy_list из класса HeadHunterAPI)"""

    def __init__(self, filename):
        self.filename = filename
        self.info_about_vacancies = []

    # блок функций для добавления в файлы
    def add_vacancies_to_file(self, value):
        """Функция добавляет данные формата json в файл"""

        with open(self.filename, "a", encoding="utf-8") as file:
            json.dump(value, file, indent=4, ensure_ascii=False)
            file.write("\n")

        # блок функций для чтения из файла

    def read_data_json(self):
        """Чтение json файла"""
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def delete_vacancy(self):
        open(self.filename, "w").close()
        os.remove(self.filename)
