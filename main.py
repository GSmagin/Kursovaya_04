from src.class_api import *
from src.class_file import ClassFile
from src.class_vacancies_hh import VacanciesHH
from src.utils import instance_class

def main():

    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = input('Введите название вакансии: ')
    ClassAPIHHR().get_api()
    name_region = input('\nВведите название id региона (по умолчанию Москва): \n')
    if not name_region:
        name_region = '1'
    vacancy = ClassAPIHH().get_api(name_vacancy, name_region)
    print(f"\nКоличество загруженных вакансий {len(vacancy)}")  # количество вакансий
    # сохранение в файл результата запроса
    ClassFile.save_to_file(vacancy)

    instance_vacancy = instance_class()

    # min_salary = 0  # Минимальная зарплата для фильтрации
    #
    # instance_vacancy = []
    # for i in ClassFile.load_from_file():
    #     salary_to = i.get('salary').get('to')
    #     if salary_to is not None and salary_to >= min_salary:
    #         instance_vacancy.append(VacanciesHH(
    #             i.get('name'),  # Вакансия
    #             i.get('area').get('name'),  # Регион
    #             i.get('salary').get('from'),  # Зарплата от
    #             salary_to,  # Зарплата до
    #             i.get('salary').get('currency'),  # Валюта зарплаты
    #             i.get('snippet').get('requirement'),  # Комментарий
    #             i.get('snippet').get('responsibility'),  # Обязанности
    #             i.get('employer').get('vacancies_url')))  # Ссылка на вакансию



                # print(
                #     i.get('name'),  # Вакансия
                #     i.get('area').get('name'),  # Регион
                #     i.get('salary').get('from'),  # Зарплата от
                #     i.get('salary').get('to'),  # Зарплата до
                #     i.get('salary').get('currency'),  # Валюта зарплаты
                #     i.get('snippet').get('requirement'),  # Комментарий
                #     i.get('snippet').get('responsibility'),  # Обязанности
                #     i.get('employer').get('vacancies_url'))  # Ссылка на ваканси

    print(f"\nКоличество отфильтрованных вакансий {len(instance_vacancy)}")  # количество вакансий
        #print(f"{i.get('area').get('name')}, {i.get('name')}")
    for i in instance_vacancy:
        print(i.__repr__())
    #print(instance_vacancy[1].__dict__)





    # print(ClassFile.load_from_file().get("items"))
    # for i in ClassFile.load_from_file():
    #     print(f"{i.get('area').get('name')}, {i.get('name')}")
    # print(f"количество вакансий {len(vacancy)}")  # количество вакансий


if __name__ == "__main__":
    main()
