from src.headhunter_api import HeadHunterAPI
from src.saver import JSONSaver
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary
from src.vacancy import Vacancy


def user_interaction():
    """Функция для работы с соискателем"""

    # Получаем данные от пользователя
    search_query = input("Введите поисковый запрос: ").lower()
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").capitalize().split()
    salary_range = input(
        "Введите диапазон зарплат и валюту, через запятую. Пример: 1000,150000,RUB (USD,EUR,KZT) "
        "по умолчанию поиск без указания зарплаты: \n"
    ).upper()
    # print("Ваш запрос обрабатывается, записывается файл")
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON по запросу
    hh_vacancies = hh_api._load_vacancies(search_query)
    # print(hh_vacancies)

    print("Ваш запрос обрабатывается, записывается файл")
    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver("data/vacancy_data.json")  # Инициализация менеджера загрузки
    json_saver.add_vacancies_to_file(hh_vacancies)  # Сохранение информации в файл

    # json_saver.delete_vacancy()

    # Открытие файла (интерпретатор создаст его сам, если файла нет)
    data = json_saver.read_data_json()
    # print(data)
    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.getting_vacancy_data(data_from_hh=data)
    print(len(vacancies_list))
    print(vacancies_list[0])

    # Фильтрация вакансий

    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)  # Фильтрация по диапазону зарплат
    # print(type(ranged_vacancies))
    filtered_vacancies = filter_vacancies(ranged_vacancies, filter_words)  # Фильтация по ключам
    # print(type(filtered_vacancies))
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)  # Фильтрация по количеству вакансий
    print(top_vacancies)
    # # Вывод вакансий в топ N
    # for vacancy in top_vacancies:
    #      print(f"{vacancy}\n")

    # Удаляем файл
    # json_saver.delete_vacancy()


if __name__ == "__main__":
    user_interaction()
