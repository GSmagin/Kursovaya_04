import re
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
    for vacancy_info in vacancies_data:
        name = vacancy_info.get("name")
        area_name = vacancy_info.get("area").get("name")
        salary_from = vacancy_info.get("salary").get("from")
        salary_to = vacancy_info.get("salary").get("to")
        salary_currency = vacancy_info.get("salary").get("currency")
        snippet_requirement = vacancy_info.get("snippet").get("requirement")
        snippet_responsibility = vacancy_info.get("snippet").get("responsibility")
        published_at = vacancy_info.get("published_at")
        schedule_name = vacancy_info.get("schedule").get("name")
        experience_name = vacancy_info.get("experience").get("name")
        url = vacancy_info.get("alternate_url")
        vacancy = VacanciesHH(name, area_name, salary_from, salary_to, salary_currency,
                              snippet_requirement, snippet_responsibility, published_at,
                              schedule_name, experience_name, url)
        collection.__add__(vacancy)
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


def validate_input_str():
    """ Валидация введенных пользователем строк """
    pattern = re.compile(r'^[a-zA-Zа-яА-Я\']+')
    while True:
        user_input = input("Введите название вакансии: ")
        if any(char.isdigit() for char in user_input):
            print("Пожалуйста, введите только слова, без цифр.")
        elif not re.match(pattern, user_input):
            print("Пожалуйста, введите только слова.")
        else:
            filtered_words = [word.group(0) for word in re.finditer(pattern, user_input)]
            return filtered_words


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
