from src.utils import create_vacancies
from src.class_api import ClassAPIHH, ClassAPIHHR
from src.class_file import ClassFile
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT, DIR_JSON_VACANCIES_SORT_TXT
from src.utils import *


def main():
    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = str(input('Введите название вакансии: '))

    while True:
        word_to_search = input("Введите название региона (или введите 0 для выхода): ")
        if word_to_search == '0':
            print("Выход из программы.")
            quit()
        else:
            result = search_word(word_to_search)
        if result:
            name_region = result
            break



    print('Введите сколько страниц загрузить (в одной странице 100 вакансий)\n'
                        'максимум 20 страниц: ')
    number_page = validate_input_int(input())

    vacancy_out_api = ClassAPIHH().api_get_pages(name_vacancy, name_region, number_page)

    # Сохранение в файл JSON
    ClassFile().save_to_file(vacancy_out_api, DIR_JSON_VACANCIES)

    # Загрузка из файла JSON
    load_from_file = ClassFile().load_from_file(DIR_JSON_VACANCIES)

    # Создание экземпляров вакансий и добавление в коллекцию
    collection = create_vacancies(load_from_file)
    print(f"В коллекции загружено вакансий: {collection.__len__()}")

    collection.sort_vacancies_by_salary()

    print('Введите минимальную зарплату вакансии: ')
    min_salary = validate_input_int(input())

    if min_salary is None:
        print('Введите минимальную зарплату вакансии: ')

        min_salary = 0

    collection.filter_salary_from(min_salary)

    print(f"В коллекции вакансий: {collection.__len__()}")

    print('Введите сколько вакансий вывести: ')
    n = validate_input_int(input())
    if n is None:
        n = 1
    collection.number_of_selected(n)
    print(f"В коллекции выбрано вакансий: {collection.__len__()}")
    for vacancy in collection.__repr__():
        print(vacancy)

    collection.save_to_json(DIR_JSON_VACANCIES_SORT)
    collection.save_to_txt(DIR_JSON_VACANCIES_SORT_TXT)


if __name__ == "__main__":
    main()
