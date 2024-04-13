from src.class_api import *
from src.class_file import ClassFile
from src.class_vacancies import VacanciesHH
from src.utils import instance_vacancy_hh

def main():

    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = input('Введите название вакансии: ')
    ClassAPIHHR().get_api()
    name_region = input('\nВведите название id региона (по умолчанию Москва): \n')
    if not name_region:
        name_region = '1'
    vacancy_out_api = ClassAPIHH().get_api(name_vacancy, name_region)
    print(f"\nКоличество загруженных вакансий {len(vacancy_out_api)}")  # количество вакансий

    # сохранение в файл vacancies.json результата запроса c HH API
    ClassFile.save_to_file(vacancy_out_api)

    # загрузка из файла vacancies.json результата запроса
    json_to_vacancies = ClassFile.load_from_file()

    manager = VacanciesHH(json_to_vacancies)
    manager.validate_salary_from()
    sorted_vacancies = manager.sort_by_salary_from(5)
    print("Top 5 Vacancies by Minimum Salary:")
    for vacancy in sorted_vacancies:
        print(vacancy["name"], vacancy["salary"]["from"])

    salary_counts = manager.count_vacancies_by_salary(5)
    # print("\nVacancy Count by Salary:")
    filter_by_default = manager.filter_by_default_salary(120)

    # salary_counts.__repr__()
    print(manager.__dict__)


if __name__ == "__main__":
    main()
