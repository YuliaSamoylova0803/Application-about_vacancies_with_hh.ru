from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл"""

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

