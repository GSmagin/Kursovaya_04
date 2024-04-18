import json
from datetime import datetime


class VacanciesCollection:
    """
    Класс для хранения и работы с коллекцией вакансий.
    """

    def __init__(self):
        """
        Инициализирует пустую коллекцию вакансий.
        """
        self.vacancies = list()

    def __add__(self, vacancy):
        """
        Добавляет вакансию в коллекцию.
        """
        self.vacancies.append(vacancy)

    def __repr__(self):
        """
        Возвращает строку с текущим состоянием коллекции вакансий.
        """
        # return f"{self.vacancies}"
        region_vacancies = [f"Вакансия: {vacancy.name},\n"
                            f"Город: {vacancy.area_name},\n"
                            f"Зарплата от: {vacancy.salary_from},\n"
                            f"Зарплата до: {vacancy.salary_to},\n"
                            f"Валюта зарплаты: {vacancy.salary_currency},\n"
                            f"Комментарий: {vacancy.snippet_requirement},\n"
                            f"Обязанности: {vacancy.snippet_responsibility},\n"
                            f"Дата публикации: {self.convert_date(vacancy.published_at)},\n"
                            f"График работы: {vacancy.schedule_name},\n"
                            f"Опыт работы: {vacancy.experience_name}\n"
                            f"Ссылка: {vacancy.url}\n"
                            for vacancy in self.vacancies]
        return region_vacancies

    def __len__(self):
        """
        Возвращает количество вакансий в коллекции.
        """
        return len(self.vacancies)

    def remove_vacancy(self, vacancy):
        """
        Удаляет вакансию из коллекции.

        :param vacancy: Экземпляр класса VacanciesHH.
        """
        self.vacancies.remove(vacancy)

    def filter_salary_from(self, min_salary):
        """
        Фильтрует вакансии по минимальной зарплате.
        """
        self.vacancies = [v for v in self.vacancies if v.salary_from >= min_salary]

    def filter_salary_from_and_to(self, max_salary):
        """
       Фильтрует вакансии по максимальной зарплате.
        """
        # self.vacancies = [v for v in self.vacancies if v.salary_to <= max_salary]
        # self.vacancies = [v for v in self.vacancies if v.salary_to is None or int(v.salary_to) <= max_salary]
        self.vacancies = [v for v in self.vacancies if v.salary_from <= max_salary]

    def sort_vacancies_by_salary(self):
        """
        Сортирует вакансии в коллекции.
        """
        self.vacancies.sort(key=lambda v: v.salary_from if v.salary_from is not None else float('inf'), reverse=True)

    def get_vacancies_print(self) -> list:
        """
        Возвращает список информацию о вакансиях.
        """
        region_vacancies = [f"Вакансия: {vacancy.name},\n"
                            f"Город: {vacancy.area_name},\n"
                            f"Зарплата от: {vacancy.salary_from},\n"
                            f"Зарплата до: {vacancy.salary_to},\n"
                            f"Валюта зарплаты: {vacancy.salary_currency},\n"
                            f"Комментарий: {vacancy.snippet_requirement},\n"
                            f"Обязанности: {vacancy.snippet_responsibility},\n"
                            f"Дата публикации: {self.convert_date(vacancy.published_at)},\n"
                            f"График работы: {vacancy.schedule_name},\n"
                            f"Опыт работы: {vacancy.experience_name}\n"
                            f"Ссылка: {vacancy.url}\n"
                            for vacancy in self.vacancies]
        return region_vacancies

    def number_of_selected(self, n=None):
        """
        Возвращает количество выбранных вакансий.
        """
        self.vacancies = self.vacancies[0:n]
        return self.vacancies

    def save_to_json(self, file_path) -> None:
        """
        Сохраняет данные о вакансиях в JSON файл.

        :param file_path: Путь к JSON файлу.
        """
        vacancies_data = []
        with open(file_path, 'w', encoding='utf-8') as file:
            for vacancy in self.vacancies:
                vacancies_data.append(vacancy.__dict__)
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)

    def save_to_txt(self, file_path) -> None:
        """
        Сохраняет данные о вакансиях в текстовый файл.

        :param file_path: Путь к текстовому файлу.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for vacancy in self.vacancies:
                file.write(f"Вакансия: {vacancy.name},\n"
                           f"Город: {vacancy.area_name},\n"
                           f"Зарплата от: {vacancy.salary_from},\n"
                           f"Зарплата до: {vacancy.salary_to},\n"
                           f"Валюта зарплаты: {vacancy.salary_currency},\n"
                           f"Комментарий: {vacancy.snippet_requirement},\n"
                           f"Обязанности: {vacancy.snippet_responsibility},\n"
                           f"Дата публикации: {self.convert_date(vacancy.published_at)},\n"
                           f"График работы: {vacancy.schedule_name},\n"
                           f"Опыт работы: {vacancy.experience_name}\n"
                           f"Ссылка: {vacancy.url}\n\n")

    @staticmethod
    def convert_date(date_str):
        # Преобразование строки в объект datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        # Форматирование даты в требуемый вид
        formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
        return formatted_date
