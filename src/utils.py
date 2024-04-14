from src.class_vacancies_collection import VacanciesCollection
from src.class_vacancieshh import VacanciesHH


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
