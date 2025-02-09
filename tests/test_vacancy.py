from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary
from src.vacancy import Vacancy


def test_init(vacancy_test):
    assert vacancy_test.name == "Менеджер по логистике"
    assert vacancy_test.city == "Алматы"
    assert vacancy_test.salary == "325000"
    assert vacancy_test.currency == "KZT"
    assert vacancy_test.responsibility == "Работа с клиентами и поиск новых заказчиков"
    assert vacancy_test._url == "<https://hh.ru/vacancy/115760953>"


def test_vacancy_str(vacancy_test):
    assert str(vacancy_test).strip().split(",") == [
        "Название вакансии: Менеджер по логистике\nГород: Алматы\nОбязанности: Работа с клиентами и поиск новых заказчиков\nЗарплата: 325000 KZT\nСсылка: <https://hh.ru/vacancy/115760953>"
    ]


vacancies_list = [
    {
        "name": "Вакансия 1",
        "area": {"name": "Москва"},
        "snippet": {"requirement": "Высшее образование", "responsibility": "Работать"},
        "salary": None,
        "alternate_url": "hh.ru",
    },
    {
        "name": "Вакансия 2",
        "area": {"name": "Ижевск"},
        "snippet": {"requirement": "Высшее образование", "responsibility": "Работать"},
        "salary": {"from": 30000, "to": None, "currency": "USD"},
        "alternate_url": "hh.ru",
    },
    {
        "name": "Вакансия 3",
        "area": {"name": "Новосибирск"},
        "snippet": {"requirement": "Базовое образование", "responsibility": "Работать"},
        "salary": {"from": None, "to": 40000, "currency": "USD"},
        "alternate_url": "hh.ru",
    },
]

filter_words = ["Москва", "Высшее образование"]

filtered_vacancy = Vacancy.getting_vacancy_data(vacancies_list)


def test_filter_vacancies():
    filtered_vacancies = filter_vacancies(filtered_vacancy, filter_words)
    assert filtered_vacancies == "Вакансии не найдены"
    filtered_vacancies = filter_vacancies(filtered_vacancy, [])
    assert filtered_vacancies == filtered_vacancies


def test_get_top_vacancies():
    filtered_vacancies = get_top_vacancies(filtered_vacancy, None)
    assert filtered_vacancies == filtered_vacancy[:3]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 2)
    assert filtered_vacancies == filtered_vacancy[:2]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 5)
    assert filtered_vacancies == filtered_vacancy[:3]


def test_get_vacancies_by_salary():
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, "")
    assert ranged_vacancies == filtered_vacancy[0:3]

    salary_range = "50000 USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == f"Измените формат ввода диапазона зарплат"
