from src.class_file import ClassFile
from src.class_vacancies_hh import VacanciesHH


# def recording_file(filename):
#     with open('../data/vacancies.json', 'w') as file:
#         json.dump(good_vacancy, file, ensure_ascii=False, default=lambda x: x.__dict__)

def instance_class():
    instance_vacancy = []
    for i in ClassFile.load_from_file():
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


