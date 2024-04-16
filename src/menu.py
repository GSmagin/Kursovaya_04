from src.class_api import ClassAPIHH
from src.class_file import ClassFile
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT, DIR_JSON_VACANCIES_SORT_TXT
from src.utils import *
from src.class_vacancies_collection import VacanciesCollection


class InteractiveMenu:
    def __init__(self):
        self.vacancy_title = "python"
        self.min_salary = 300000
        self.region = 'москва'
        self.pages_to_parse = 2
        self.collection = VacanciesCollection()

    def show_menu(self):
        print("\nГлавное меню:")
        print("1. Задать параметры для парсинга")
        print("2. Запустить парсинг")
        print("3. Отобразить результат")
        print("4. Отсортировать зарплаты по убыванию")
        print("5. Сколько из ТОП вакансий вывести")
        print("6. Сохранить результат поиска в файл")
        print("7. Выход")

# ==подменю==
    def set_vacancy_title(self):
        # 1. Задать название вакансии
        self.vacancy_title = input("Введите название вакансии: ")

    def set_min_salary(self):
        # 2. Задать минимальную ЗП для парсинга
        self.min_salary = input("Введите минимальную зарплату: ")

    def set_region(self):
        # 3. Задать регион
        # self.region = input("Введите регион: ")
        while True:
            word_to_search = input("Введите название региона (или введите 0 для выхода): ")
            if word_to_search == '0':
                print("Выход из программы.")
                quit()
            else:
                result = search_word(word_to_search)
            if result:
                self.region = result
                break

    def set_pages_to_parse(self):
        # 4. Задать количество страниц для парсинга
        self.pages_to_parse = int(input("Введите количество страниц для парсинга: "))

    def start_parsing(self):
        # 2. Начать парсинг
        # 2. Запустить парсинг
        print("Парсинг запущен...")
        vacancy_out_api = ClassAPIHH().api_get_pages(self.vacancy_title, self.region, self.pages_to_parse)
        ClassFile().save_to_file(vacancy_out_api, DIR_JSON_VACANCIES)  # Сохранение в файл
        load_from_file = ClassFile().load_from_file(DIR_JSON_VACANCIES)  # Загрузка из файла
        # Создание экземпляров вакансий и добавление в коллекцию
        self.collection = create_vacancies(load_from_file)
        print(f"Собрано вакансий: {self.collection.__len__()}")

    # ==подменю конец==

    def display_results(self):
        # 3. Отобразить результат
        print("Результаты парсинга:")
        for vacancy in self.collection.__repr__():
            print(vacancy)
        print(f"В коллекции вакансий: {self.collection.__len__()}")

    def sort_salaries(self):
        # 4. Отсортировать зарплаты по убыванию
        print("Сортировка зарплат по убыванию...")
        self.collection.sort_vacancies_by_salary()

    def show_vacancy_count(self):
        # 5. Сколько из ТОП вакансий вывести
        print(f"В коллекции вакансий: {self.collection.__len__()}")

        n = int(input("Сколько из ТОП вакансий вывести: "))
        self.collection.number_of_selected(n)
        print(f"В коллекции вакансий: {self.collection.__len__()}")

    def save_results_to_file(self):
        # 6. Сохранить результат поиска в файл
        # print("Сохранение результата в файл...")
        # ClassFile().save_to_file(self.collection, DIR_JSON_VACANCIES_SORT)
        print("Результаты сохранены в файл и выйти из программы.")
        print(self.collection.__repr__())
        self.collection.save_to_json(DIR_JSON_VACANCIES_SORT)
        self.collection.save_to_txt(DIR_JSON_VACANCIES_SORT_TXT)
        quit()

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.set_parameters_menu()
            elif choice == '2':
                self.start_parsing()
            elif choice == '3':
                self.display_results()
            elif choice == '4':
                self.sort_salaries()
            elif choice == '5':
                self.show_vacancy_count()
            elif choice == '6':
                self.save_results_to_file()
            elif choice == '7':
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите пункт меню снова.")

    def set_parameters_menu(self):
        while True:
            print("\nМеню параметров для парсинга:")
            print("1. Задать название вакансии")
            print("2. Задать минимальную ЗП")
            print("3. Задать регион")
            print("4. Задать количество страниц для парсинга (на 1ой странице будет 100 вакансий)")
            print("5. Начать парсинг")
            print("6. Выход в главное меню")

            sub_choice = input("Выберите пункт меню: ")

            if sub_choice == '1':
                self.set_vacancy_title()
            elif sub_choice == '2':
                self.set_min_salary()
            elif sub_choice == '3':
                self.set_region()
            elif sub_choice == '4':
                self.set_pages_to_parse()
            elif sub_choice == '5':
                self.start_parsing()
            elif sub_choice == '6':
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите пункт меню снова.")


if __name__ == "__main__":
    menu = InteractiveMenu()
    menu.run()
