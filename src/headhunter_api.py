from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _load_vacancies(self):
        """Метод отправки get-запроса на сайт Head Hunter"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        """Магический метод инициализаций объектов для отправки get-запроса"""
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def _load_vacancies(self, keyword) -> Any:
        """Метод отправки get-запроса на сайт Head Hunter"""
        self.params["text"] = keyword
        while self.params.get("page") != 10:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    print(hh_api)
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api._load_vacancies("Python")
    print(hh_vacancies)
