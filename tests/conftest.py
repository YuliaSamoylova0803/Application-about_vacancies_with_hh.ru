import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_test():
    return Vacancy(
        "Менеджер по логистике",
        "Алматы",
        "325000",
        "KZT",
        "Работа с клиентами и поиск новых заказчиков",
        "<https://hh.ru/vacancy/115760953>",
    )
