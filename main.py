from src.utils import create_vacancies
from src.class_api import ClassAPIHH, ClassAPIHHR
from src.class_file import ClassFile
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT, DIR_JSON_VACANCIES_SORT_TXT


def main():
    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = str(input('Введите название вакансии: '))
    name_region = str(input('Введите название id региона (по умолчанию Москва)\n'
                            'N вызвать список регионов с ID: '))

    if not name_region:
        name_region = '1'
    elif name_region == 'N':
        ClassAPIHHR.get_api_region()
        name_region = str(input('Введите название id региона (по умолчанию Москва): \n'))

    number_page = int(input('Введите сколько страниц загрузить (в одной странице 100 вакансий): '))
    if number_page is None:
        number_page = 1

    vacancy_out_api = ClassAPIHH().api_get_pages(name_vacancy, name_region, number_page)

    # Сохранение в файл JSON
    ClassFile().save_to_file(vacancy_out_api, DIR_JSON_VACANCIES)

    # Загрузка из файла JSON
    load_from_file = ClassFile().load_from_file(DIR_JSON_VACANCIES)

    # Создание экземпляров вакансий и добавление в коллекцию
    collection = create_vacancies(load_from_file)
    print(f"В коллекции загружено вакансий: {collection.__len__()}")

    collection.sort_vacancies_by_salary()

    min_salary = int(input('Введите минимальную зарплату вакансии: '))
    if not min_salary:
        min_salary = 0

    collection.filter_salary_from(min_salary)

    print(f"В коллекции вакансий: {collection.__len__()}")

    n = int(input('Введите сколько вакансий выбрать: '))

    collection.number_of_selected(n)
    print(f"В коллекции выбрано вакансий: {collection.__len__()}")
    for vacancy in collection.__repr__():
        print(vacancy)

    collection.save_to_json(DIR_JSON_VACANCIES_SORT)
    collection.save_to_txt(DIR_JSON_VACANCIES_SORT_TXT)


if __name__ == "__main__":
    main()
