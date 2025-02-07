import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_test():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>" ,  "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")