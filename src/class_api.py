from src.absclasses import AbstractClassAPI, AbstractClassClassAPIHHR
import requests


class ClassAPIHH(AbstractClassAPI):
    """Подключается к api.hh.ru и получает вакансии по ключевому слову"""

    def api_get_pages(self, word_search, region, num_pages) -> list:
        """
        Получает вакансии по ключевому слову из API сервиса hh.ru
        :param word_search: Ключевое слово для поиска вакансий
        :param region: Регион
        :param num_pages: Количество страниц для загрузки
        :return: JSON-данные с информацией о вакансиях
        """
        url = 'https://api.hh.ru/vacancies'
        all_vacancies = []

        if num_pages is None:
            num_pages = 1

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
                all_vacancies.extend(vacancies_data['items'])
            else:
                print(f"Не удалось получить данные со страницы {page_num}")

        return all_vacancies


class ClassAPIHHR(AbstractClassClassAPIHHR):
    """Подключается к api.hh.ru и получает id регионов"""

    @staticmethod
    def get_api_region() -> dict:
        url = 'https://api.hh.ru/areas/113'
        response = requests.get(url)
        for i in response.json().get('areas'):
            print(f"id={i.get('id')} {i.get('name')} ")
        resp = response.json().get('areas')
        dict_regions = {}
        for i in resp:
            dict_regions[i.get('name')] = i.get('id')
        return dict_regions
