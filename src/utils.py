import json

import requests

from src.class_vacancies_collection import VacanciesCollection
from src.class_vacancieshh import VacanciesHH
from src.class_api import ClassAPIHHR


def create_vacancies(vacancies_data):
    """
    Создает и возвращает список экземпляров класса VacanciesHH на основе данных вакансий.

    :param vacancies_data: Список данных вакансий в формате JSON.
    :return: Список экземпляров класса VacanciesHH.
    """
    collection = VacanciesCollection()
    # vacancies = []
    for vacancy_info in vacancies_data:
        name = vacancy_info.get("name")
        area_name = vacancy_info.get("area").get("name")
        salary_from = vacancy_info.get("salary").get("from")
        salary_to = vacancy_info.get("salary").get("to")
        salary_currency = vacancy_info.get("salary").get("currency")
        snippet_requirement = vacancy_info.get("snippet").get("requirement")
        snippet_responsibility = vacancy_info.get("snippet").get("responsibility")
        url = vacancy_info.get("alternate_url")
        vacancy = VacanciesHH(name, area_name, salary_from, salary_to, salary_currency,
                              snippet_requirement, snippet_responsibility, url)
        collection.__add__(vacancy)
        # vacancies.append(vacancy)
    return collection


def form_region_113(region_text):
    get_api_region = ClassAPIHHR.get_api_region()
    return get_api_region.get(region_text)


def validate_input_int(user_input: str) -> int:
    """ Валидация введенного пользователем числа """

    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        user_input = input('Неверный ввод, попробуйте еще раз ввести цифру: ')
        return validate_input_int(user_input)

def get_api_reg(side="113"):
    url = 'https://api.hh.ru/areas/' + side
    response = requests.get(url)
    resp = response.json().get('areas')
    dict_regions = {}
    for i in resp:
        dict_regions[i.get('name')] = i.get('id')
    return dict_regions


def search_word(word):

    dictionary = get_api_reg()
    word = word.capitalize()  # Преобразование в верхний регистр
    print(word)
    # Проверяем, есть ли слово в качестве ключа в словаре
    if word in dictionary:
        return dictionary[word]
    else:
        # Если слова нет в качестве ключа, ищем совпадения
        matches = [key for key in dictionary.keys() if word in key]

        # Если есть совпадения, выводим их в терминал и предлагаем пользователю выбрать
        if matches:
            print("Найдены совпадения:")
            for i, match in enumerate(matches):
                print(f"{i + 1}. {match}")

            while True:
                choice = input("Выберите номер соответствия (00 для нового поиска ): ")
                if choice == '00':
                    return None
                try:
                    choice = int(choice)
                    if choice > 0 and choice <= len(matches):
                        return dictionary[matches[choice - 1]]
                    else:
                        print("Некорректный выбор.")
                except ValueError:
                    print("Введите число.")
        else:
            print("Слово не найдено в словаре.")
            return None


# Пример использования функции в бесконечном цикле
my_dictionary = {"apple": "яблоко", "banana": "банан", "orange": "апельсин"}

# while True:
#     word_to_search = input("Введите слово для поиска (или введите 0 для выхода): ")
#     if word_to_search == '0':
#         print("Выход из программы.")
#         break
#     result = search_word(word_to_search)
#     if result:
#         print(f"Результат: {result}")

def save_to_json_file(vacancies, file_path):
    """
    Сохраняет данные о вакансиях в JSON файл.

    :param file_path: Путь к JSON файлу.
    """
    print("save_to_json")
    vacancies_data = []
    for vacancy in vacancies:
        vacancy_info = {
            "name": vacancy.name,
            "area": {"name": vacancy.area_name},
            "salary": {"from": vacancy.salary_from, "to": vacancy.salary_to, "currency": vacancy.salary_currency},
            "snippet": {"requirement": vacancy.snippet_requirement,
                        "responsibility": vacancy.snippet_responsibility},
            "alternate_url": vacancy.url
        }
        vacancies_data.append(vacancy_info)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(vacancies_data, file, ensure_ascii=False, indent=4)


# for i, v in get_api_reg().items():
#     print(i, v)
