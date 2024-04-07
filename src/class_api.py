import requests


class ClassAPI:
    """Подключается к API и получает вакансии по ключевому слову"""

    def get_vacancies(self, word_search):
        """
             Получает вакансии по ключевому слову из API сервиса hh.ru
             :return:
             :param word_search: Ключевое слово для поиска вакансий
             :return: JSON-данные с информацией о вакансиях
             """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': word_search,
            'area': 1,
            'per_page': 100,
            'page': 1,
            'only_with_salary': 'true'
        }
        response = requests.get(url, params=params)
        return response.json()


