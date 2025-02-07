import pytest

from src.vacancy import Vacancy


def test_init(vacancy_test):
    assert vacancy_test.name == "Python Developer"
    assert vacancy_test.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy_test.salary == "100 000-150 000 руб."
    assert vacancy_test.description == "Требования: опыт работы от 3 лет..."


def test_vacancy_str(vacancy_test):
    assert str(vacancy_test).strip().split(",") == ['Python Developer', ' <https://hh.ru/vacancy/123456>', ' заработная плата от 100 000-150 000 руб.']