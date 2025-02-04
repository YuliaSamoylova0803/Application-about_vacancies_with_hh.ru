
class Vacancy:
    """Класс для работы с вакансиями"""

    name: str
    url: str
    pay: str
    description: str


    def __init__(self, name, description, url, pay):
        self.name = name
        self.url = url
        self.pay = pay
        self.description = description

    def cast_to_object_list(self):
        pass