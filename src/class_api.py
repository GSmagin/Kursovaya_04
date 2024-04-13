import requests
from abc import ABC, abstractmethod
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT


class ClassAPI(ABC):
    @abstractmethod
    def get_api(self, word_search) -> dict:
        pass


class ClassAPIHH(ClassAPI):
    """Подключается к api.hh.ru и получает вакансии по ключевому слову"""

    def get_api(self, word_search, region) -> dict:
        # def get_api(self, word_search, order_by="salary_desc", region=1):
        """
             Получает вакансии по ключевому слову из API сервиса hh.ru
             :param word_search: Ключевое слово для поиска вакансий
             :param region: Регион
             :return: JSON-данные с информацией о вакансиях
             """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': word_search,  # Ключевое слово
            'area': region,  # Регион
            # 'per_page': 100,  # количество результатов на странице;
            # 'page': 2,  # номер страницы
            # 'order_by':  order_by,  # Сортировка по зарплате
            'only_with_salary': 'true'  # Возвращать только вакансии с заработной платой
        }
        response = requests.get(url, params=params)
        return response.json()


class ClassAPIHHR(ClassAPI):
    """Подключается к api.hh.ru и получает id регионов"""

    def get_api(self, side="113") -> dict:
        url = 'https://api.hh.ru/areas/' + side
        response = requests.get(url)
        for i in response.json().get('areas'):
            print(f"id={i.get('id')} {i.get('name')} ")

        return response.json()

# class ClassAPIHHSort(ClassAPI):
#     def get_api(self, vacancy_search_order="vacancy_search_order"):
#         url = 'https://api.hh.ru/dictionaries'
#         response = requests.get(url)
#         for i in response.json().get(vacancy_search_order):
#             print(f"id={i.get('id')} {i.get('name')} ")
#
#         return response.json()
#
#         # list_vacancy_search_order = []
#         # number = 1
#         # for i in response.json().get('vacancy_search_order'):
#         #     i["Number"] = number
#         #     list_vacancy_search_order.append(i)
#         #     print(f"{i.get('Number')} {i.get('name')}")
#         #     number += 1
#         # return list_vacancy_search_order


# rt = input("Введите слово для поиска ")
#
# ClassAPIHHR().get_api()
# id = input("Введите id региона ")

# ClassAPIHHSort().get_api()
# vacancy_search_order = input("Введите id сортировки ")


#
# dir_json = ClassAPIHH().get_api(rt, id)
# print(ClassAPIHH().get_api(rt, id))
