def filter_vacancies(vacancies_list, filter_words):
    """
    Функция для фильтрации вакансий
    :param vacancies_list: список вакансий
    :param filter_words: ключ по которому идет фильтрация
    :return:
    """
    if not isinstance(vacancies_list, list):
        return "Вакансии не найдены"

    elif not filter_words:
        return vacancies_list

    filtered_vacancies = []
    for vacancy in vacancies_list:
        count = 0  # Счетчик итерраций для исключения повторений вакансий в полученном списке

        for word in filter_words:
            if word in vacancy.name or word in vacancy.responsibility:
                count += 1
                if count > 1:
                    continue
                filtered_vacancies.append(vacancy)

    if len(filtered_vacancies) == 0 or filtered_vacancies is None:
        return "Вакансии не найдены"
    else:
        return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Функция для получения вакансий по зарплате
    :param filtered_vacancies: список вакансий
    :param salary_range: диапазон зарплаты
    :return:
    """
    if isinstance(filtered_vacancies, (int, str)):
        return "Вакансии не найдены"

    try:
        if not salary_range:
            return filtered_vacancies
        else:
            try:
                from_salary, to_salary, currency = salary_range.split(",")

                ranged_vacancies = []
                for vacancy in filtered_vacancies:
                    if int(from_salary) <= int(vacancy.salary) <= int(to_salary) and vacancy.currency == currency:
                        ranged_vacancies.append(vacancy)
                return ranged_vacancies

            except AttributeError:
                return "Вакансии не найдены"
    except ValueError:
        return "Измените формат ввода диапазона зарплат"


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Функция для получения топовых вакансий
    :param sorted_vacancies: список вакансий
    :param top_n: количество топовых вакансий
    :return:
    """
    if not top_n:
        top_n = len(sorted_vacancies)
        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies

    try:
        top_n = int(top_n)
        if len(sorted_vacancies) < top_n:
            top_n = len(sorted_vacancies)

        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies

    except ValueError:
        return "Ошибка ввода топа N. Введите число"
