from src.absclasses import AbstractClassVacanciesHH


class VacanciesHH(AbstractClassVacanciesHH):
    """
    Класс для представления вакансий
    """

    def __init__(self, name, area_name, salary_from, salary_to, salary_currency,
                 snippet_requirement, snippet_responsibility, published_at,
                 schedule_name, experience_name, url):
        """
        Инициализирует объект класса VacanciesHH.

        :param name: Название вакансии.
        :param area_name: Название город.
        :param salary_from: Минимальная зарплата.
        :param salary_to: Максимальная зарплата.
        :param salary_currency: Валюта зарплаты.
        :param snippet_requirement: Требования к кандидату.
        :param snippet_responsibility: Обязанности.
        :param published_at: Дата публикации.
        :param schedule_name: График работы.
        :param experience_name: Опыт работы.
        :param url: Ссылка на вакансию.
        """
        self.name = name
        self.area_name = area_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.snippet_requirement = snippet_requirement
        self.snippet_responsibility = snippet_responsibility
        self.published_at = published_at
        self.schedule_name = schedule_name
        self.experience_name = experience_name
        self.url = url

        self.validate_salary_from()
        self.validate_salary_to()

    def validate_salary_from(self):
        """
        Валидация данный о вакансии
        :return: Если зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_from:
            self.salary_from = 0

    def validate_salary_to(self):
        """
        Валидация данный о вакансии
        :return: Если зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_to:
            self.salary_to = 0
