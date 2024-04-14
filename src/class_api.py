from typing import List, Any, Dict

import requests


# from abc import ABC, abstractmethod
# from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT
#
#
# class ClassAPI(ABC):
#     @abstractmethod
#     def get_api(self, word_search) -> dict:
#         pass
#
#     @abstractmethod
#     def get_api_2(self, word_search, region, sort) -> dict:
#         pass
#


class ClassAPIHH:
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
            'per_page': 100,  # количество результатов на странице;
            'page': 1,  # номер страницы
            # 'order_by':  order_by,  # Сортировка по зарплате
            'only_with_salary': 'true'  # Возвращать только вакансии с заработной платой
        }
        response = requests.get(url, params=params)
        return response.json()

    def get_api_2(self, word_search, region, num_pages=1) -> dict[str, list[Any]]:
        """
        Получает вакансии по ключевому слову из API сервиса hh.ru
        :param word_search: Ключевое слово для поиска вакансий
        :param region: Регион
        :param num_pages: Количество страниц для загрузки
        :return: JSON-данные с информацией о вакансиях
        """
        url = 'https://api.hh.ru/vacancies'
        all_vacancies = {"items": []}

        for page_num in range(1, num_pages + 1):
            params = {
                'text': word_search,  # Ключевое слово
                'area': region,  # Регион
                'per_page': 100,  # количество результатов на странице;
                'page': page_num,  # номер страницы
                'only_with_salary': 'true'  # Возвращать только вакансии с заработной платой
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                vacancies_data = response.json()
                all_vacancies["items"].extend(vacancies_data['items'])
            else:
                print(f"Failed to fetch data from page {page_num}")

        return all_vacancies


class ClassAPIHHR:
    """Подключается к api.hh.ru и получает id регионов"""

    def get_api(self, side="113") -> dict:
        url = 'https://api.hh.ru/areas/' + side
        response = requests.get(url)
        for i in response.json().get('areas'):
            print(f"id={i.get('id')} {i.get('name')} ")

        return response.json()
