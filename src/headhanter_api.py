from abc import ABC, abstractmethod

class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def load_vacancies(self):
        pass

class HeadHunterAPI(Parser):
    pass

    def get_vacancies(self):
        pass



