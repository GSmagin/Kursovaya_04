
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
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0

