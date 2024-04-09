import requests
from abc import ABC, abstractmethod


class ClassAPI(ABC):
    @abstractmethod
    def get_vacancies(self, word_search):
        pass


class ClassAPIHH(ClassAPI):
    """Подключается к api.hh.ru и получает вакансии по ключевому слову"""

    def get_vacancies(self, word_search, region=1):
        """
             Получает вакансии по ключевому слову из API сервиса hh.ru
             :param word_search: Ключевое слово для поиска вакансий
             :param region: Регион по умолчанию Москва
             :return: JSON-данные с информацией о вакансиях
             """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': word_search,  # Ключевое слово
            'area': region,  # Регион
            'per_page': 100,  # количество результатов на странице;
            'page': 1,  # номер страницы
            'only_with_salary': 'true'  # Возвращать только вакансии с заработной платой
        }
        response = requests.get(url, params=params)
        return response.json()


class ClassAPIHHR(ClassAPI):
    """Подключается к api.hh.ru и получает id регионов"""

    def get_vacancies(self, side="113"):
        url = 'https://api.hh.ru/areas/'+side
        response = requests.get(url)
        for i in response.json().get('areas'):
            print(f"id={i.get('id')} {i.get('name')} ")

        return response.json()


# print(ClassAPI().get_vacancies("python"))
# print(ClassAPIR().get_vacancies("python"))
rt = input("Введите слово для поиска ")
id = input("Введите id региона если id не известен то нажмите enter для отображения списка регионов ")
if id:
    ClassAPIHH().get_vacancies(rt, id)
else:
    ClassAPIHHR().get_vacancies()
    id = input("Введите id региона ")

print(ClassAPIHH().get_vacancies(rt, id))
