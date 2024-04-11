class VacanciesHH:
    """
    Класс для представления вакансий
    """

    def __init__(self, name, area_name, salary_from, salary_to, salary_currency,
                 snippet_requirement, snippet_responsibility, url):
        """
        :param name Вакансия
        :param area_name Регион
        :param salary_from Зарплата от
        :param salary_to Зарплата до
        :param salary_currency Валюта зарплаты
        :param snippet_requirement Комментарий
        :param snippet_responsibility Обязанности
        :param url Ссылка на вакансию
        """

        self.name = name
        self.area_name = area_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.snippet_requirement = snippet_requirement
        self.snippet_responsibility = snippet_responsibility
        self.url = url

        self.validate_salary()

    def validate_salary(self):
        """
        Валидация данный о вакансии
        :return: Если зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_from:
            self.salary_from = 0

    def __repr__(self):
        """Строковое представление объекта"""
        return (f'{self.name} {self.area_name} {self.salary_from} {self.salary_to} {self.salary_currency}'
                f' {self.snippet_requirement} {self.snippet_responsibility} {self.url}')

    def __str__(self):
        """Строковое представление объекта"""
        return (f'{self.name} {self.area_name} {self.salary_from} {self.salary_to} {self.salary_currency}'
                f' {self.snippet_requirement} {self.snippet_responsibility} {self.url}')

    def __eq__(self, other):
        """Сравнение двух объектов"""
        return self.name == other.name and self.area_name == other.area_name and self.salary_from == other.salary_from \
               and self.salary_to == other.salary_to and self.salary_currency == other.salary_currency \
               and self.snippet_requirement == other.snippet_requirement \
               and self.snippet_responsibility == other.snippet_responsibility and self.url == other.url

    def filter_vacancies_by_salary(self, min_salary):
        """Фильтрация вакансий по минимальной зарплате"""
        return [vacancy for vacancy in sorted(self.salary_from, key=lambda vacancy: self.salary_from) if
                min_salary <= self.salary_from]


