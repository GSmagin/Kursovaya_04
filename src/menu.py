from src.class_api import ClassAPIHH
from src.class_file import ClassFile
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT, DIR_JSON_VACANCIES_SORT_TXT
from src.utils import validate_input_int, validate_input_str, create_vacancies, search_word
from src.class_vacancies_collection import VacanciesCollection


class InteractiveMenu:
    def __init__(self):
        self.vacancy_title = None
        self.min_salary = None
        self.max_salary = None
        self.region = None  # default Москва
        self.pages_to_parse = 1
        self.top_vacancies = None
        self.collection = VacanciesCollection()

    def set_parsing_parameters(self):
        print("\n1. Задать название вакансии")
        # Проверка на валидность вакансии
        self.vacancy_title = validate_input_str()[0]
        print("\n2. Задать регион")
        self.set_region()
        print("\n3. Задать количество страниц для парсинга(1 страница - 100 вакансий)")
        self.pages_to_parse = validate_input_int(input("Введите количество страниц: "))
        print("\n4. Начать парсинг")
        self.start_parsing()

    def start_parsing(self):
        # реализация начала парсинга
        print("Парсинг запущен...")
        vacancy_out_api = ClassAPIHH().api_get_pages(self.vacancy_title, self.region, self.pages_to_parse)
        ClassFile().save_to_file(vacancy_out_api, DIR_JSON_VACANCIES)  # Сохранение в файл
        load_from_file = ClassFile().load_from_file(DIR_JSON_VACANCIES)  # Загрузка из файла
        # Создание экземпляров вакансий и добавление в коллекцию
        self.collection = create_vacancies(load_from_file)
        print(f"\nСобрано вакансий: {self.collection.__len__()}")

    def set_region(self):
        # 4. регион
        while True:
            word_to_search = input("Введите название региона (или введите 0 для выхода): ")
            if word_to_search == "0":
                print("Выход из программы.")
                break
            else:
                result = search_word(word_to_search)
            if result:
                self.region = result
                break

    def filter_menu(self):
        while True:
            print("\nМеню фильтрации:")
            print("1. Задать минимальную ЗП от")
            print("2. Задать максимальную ЗП от")
            print("3. Отсортировать зарплаты по убыванию")
            print("4. Применить фильтр минимальной ЗП от")
            print("5. Применить фильтр максимальной ЗП от")
            print("6. Отобразить результат")
            print("7. Сколько из ТОП вакансий оставить")
            print("8. Выход в главное меню")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.set_min_salary()
            elif choice == "2":
                self.set_max_salary()
            elif choice == "3":
                self.sort_salaries()
            elif choice == "4":
                self.apply_min_salary_filter()
            elif choice == "5":
                self.apply_max_salary_filter()
            elif choice == "6":
                self.display_results()
            elif choice == "7":
                self.set_top_vacancies()
            elif choice == "8":
                print("Выход в главное меню.")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий пункт.")

    def set_min_salary(self):
        self.min_salary = validate_input_int(input("Введите минимальную ЗП: "))

    def set_max_salary(self):
        self.max_salary = validate_input_int(input("Введите максимальную ЗП: "))

    def sort_salaries(self):
        # Сортировка зарплат по убыванию
        print("Сортировка зарплат по убыванию...")
        self.collection.sort_vacancies_by_salary()

    def apply_min_salary_filter(self):
        # фильтр минимальной ЗП
        if self.min_salary:
            self.collection.filter_salary_from(self.min_salary)
            print(f"\nВ коллекции вакансий: {self.collection.__len__()}")
        else:
            print("\nНе задана минимальная ЗП. Задайте минимальную ЗП.")

    def apply_max_salary_filter(self):
        # фильтр максимальной ЗП
        if self.max_salary:
            self.collection.filter_salary_from_and_to(self.max_salary)
            print(f"\nВ коллекции вакансий: {self.collection.__len__()}")
        else:
            print("\nНе задана максимальная ЗП. Задайте максимальную ЗП.")

    def display_results(self):
        # отображение результатов
        print("Результаты парсинга:")
        for vacancy in self.collection.__repr__():
            print(vacancy)
        print(f"\nВ коллекции вакансий: {self.collection.__len__()}")

    def set_top_vacancies(self):
        # Сколько из ТОП вакансий оставить
        print(f"В коллекции вакансий: {self.collection.__len__()}")
        self.top_vacancies = validate_input_int(input("Сколько из ТОП вакансий оставить: "))
        self.collection.number_of_selected(self.top_vacancies)
        print(f"\nВ коллекции осталось вакансий: {self.collection.__len__()}")

    def main_menu(self):
        while True:
            print("\nГлавное меню:")
            print("1. Задать параметры для парсинга")
            print("2. Меню фильтрации")
            print("3. Отобразить результат")
            print("4. Сохранить результат в файл")
            print("5. Удалить файл")
            print("6. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.set_parsing_parameters()
            elif choice == "2":
                self.filter_menu()
            elif choice == "3":
                self.display_results()
            elif choice == "4":
                self.save_to_file()
            elif choice == "5":
                self.delete_file()
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий пункт.")

    def save_to_file(self):
        # сохранение результатов в файл
        print("Результаты сохранены, выход")
        self.collection.save_to_json(DIR_JSON_VACANCIES_SORT)
        self.collection.save_to_txt(DIR_JSON_VACANCIES_SORT_TXT)

    @staticmethod
    def delete_file():
        # удаление файла
        ClassFile.delete_from_file(DIR_JSON_VACANCIES_SORT)
        ClassFile.delete_from_file(DIR_JSON_VACANCIES_SORT_TXT)
