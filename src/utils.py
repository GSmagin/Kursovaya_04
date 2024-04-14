
from src.class_vacancies_hh import VacanciesHH

# def recording_file(filename):
#     with open('../data/vacancies.json', 'w') as file:
#         json.dump(good_vacancy, file, ensure_ascii=False, default=lambda x: x.__dict__)

def instance_vacancy_hh(data):
    instance_vacancy = []
    for i in data:
        instance_vacancy.append(VacanciesHH(
            i.get('name'),  # Вакансия
            i.get('area').get('name'),  # Регион
            i.get('salary').get('from'),  # Зарплата от
            i.get('salary').get('to'),  # Зарплата до
            i.get('salary').get('currency'),  # Валюта зарплаты
            i.get('snippet').get('requirement'),  # Комментарий
            i.get('snippet').get('responsibility'),  # Обязанности
            i.get('employer').get('vacancies_url')))  # Ссылка на вакансию
        return instance_vacancy

