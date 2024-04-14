class VacanciesCollection:
    """
    Класс для хранения и работы с коллекцией вакансий.
    """

    def __init__(self):
        """
        Инициализирует пустую коллекцию вакансий.
        """
        self.vacancies = set()

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в коллекцию.

        :param vacancy: Экземпляр класса VacanciesHH.
        """
        self.vacancies.add(vacancy)

    def remove_vacancy(self, vacancy):
        """
        Удаляет вакансию из коллекции.

        :param vacancy: Экземпляр класса VacanciesHH.
        """
        self.vacancies.remove(vacancy)

    def get_vacancies_by_region(self, region_name):
        """
        Возвращает список вакансий для указанного региона.

        :param region_name: Название региона.
        :return: Список вакансий для указанного региона.
        """
        return [v for v in self.vacancies if v.area_name == region_name]

    def get_vacancies_with_salary_above(self, salary_threshold):
        """
        Возвращает список вакансий с зарплатой выше указанного порога.

        :param salary_threshold: Пороговая зарплата.
        :return: Список вакансий с зарплатой выше указанного порога.
        """
        return [v for v in self.vacancies if v.salary_from > salary_threshold]

    def get_vacancies_with_salary_below(self, salary_threshold):
        """
        Возвращает список вакансий с зарплатой ниже указанного порога.

        :param salary_threshold: Пороговая зарплата.
        :return: Список вакансий с зарплатой ниже указанного порога.
        """
        return [v for v in self.vacancies if v.salary_to < salary_threshold]
