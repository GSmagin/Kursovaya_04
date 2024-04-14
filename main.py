from src.class_api import *
from src.class_file import ClassFile
from src.class_vacancies_collection import *

from src.class_vacancies_hh import VacanciesHH


def main():
    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = input('Введите название вакансии: ')
    ClassAPIHHR().get_api()
    name_region = input('\nВведите название id региона (по умолчанию Москва): \n')
    if not name_region:
        name_region = '1'
    vacancy_out_api = ClassAPIHH().get_api(name_vacancy, name_region)
    # print(f"\nКоличество загруженных вакансий {len(vacancy_out_api.get('name'))}")  # количество вакансий
    # удаление файла vacancies.json
    # ClassFile.delete_from_file()

    # сохранение в файл vacancies.json результата запроса c HH API
    ClassFile.save_to_file(vacancy_out_api)

    # загрузка из файла vacancies.json результата запроса
    json_to_vacancies = ClassFile.load_from_file()
    # Пример использования:

    # Создание экземпляров вакансий
    vacancy1 = VacanciesHH("Python Developer", "Moscow", 100000, 150000, "RUB", "Experience with Python is required.", "Developing Python applications.", "https://example.com/vacancy1")
    vacancy2 = VacanciesHH("Java Developer", "St. Petersburg", 90000, 140000, "RUB", "Java skills are necessary.", "Java development tasks.", "https://example.com/vacancy2")

    # Создание коллекции и добавление вакансий
    collection = VacanciesCollection()
    collection.add_vacancy(vacancy1)
    collection.add_vacancy(vacancy2)

    # Получение списка вакансий для конкретного региона
    moscow_vacancies = collection.get_vacancies_by_region("Moscow")
    print("Вакансии в регионе Moscow:", moscow_vacancies)

    # Получение списка вакансий с зарплатой выше определенного порога
    high_salary_vacancies = collection.get_vacancies_with_salary_above(120)
    print(f"\nВакансии с зарплатой выше 120: {high_salary_vacancies}")








if __name__ == "__main__":
    main()
