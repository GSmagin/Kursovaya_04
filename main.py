from src.class_api import *
from src.class_file import ClassFile
from src.class_vacancies import VacanciesHH
from confing import DIR_JSON_VACANCIES_SORT_TXT, DIR_JSON_VACANCIES_SORT


def main():

    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = input('Введите название вакансии: ')
    ClassAPIHHR().get_api()
    # if not name_vacancy:
    #     name_vacancy = 'python'
    name_region = input('\nВведите название id региона (по умолчанию Москва): \n')
    if not name_region:
        name_region = '1'
    vacancy_out_api = ClassAPIHH().get_api_2(name_vacancy, name_region, 1)
    # print(f"\nКоличество загруженных вакансий {len(vacancy_out_api.get('name'))}")  # количество вакансий

    # удаление файла vacancies.json
    ClassFile.delete_from_file()

    # сохранение в файл vacancies.json результата запроса c HH API
    ClassFile.save_to_file_append(vacancy_out_api)


    # загрузка из файла vacancies.json результата запроса
    json_to_vacancies = ClassFile.load_from_file()

    # создание объекта класса VacanciesHH
    manager = VacanciesHH(json_to_vacancies)
    print(f"Количество всего загруженных вакансий {manager.__len__()}\n")
    # фильтрация по зарплате
    manager.filter_salary_from(100000)

    print(f"\nКоличество отсортированных вакансий {manager.__len__()}\n")

    manager.sort_by_salary_desc()
    #print("\n")
    #print(manager.__repr__())
    #print("\n")
    manager.number_of_selected(10)
    #print(manager.__repr__())
    #print("\n")
    manager.print_vacancies()
    rtrtr = manager.print_vacancies()
    print(f"\nКоличество выведенных вакансий {manager.__len__()}\n")

    #print(manager)
    ClassFile.save_to_file(manager.save_vacancies_json(), DIR_JSON_VACANCIES_SORT)
    ClassFile.save_to_file_txt(manager.save_vacancies_txt(), DIR_JSON_VACANCIES_SORT_TXT)



if __name__ == "__main__":
    main()
