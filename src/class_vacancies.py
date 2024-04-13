import json


class VacanciesHH:
    def __init__(self, filename):
        # with open(filename, 'r', encoding='utf-8') as file:
        self.items = filename.get('items')

    def __repr__(self):
        vacancy_names = [vacancy['name'] for vacancy in self.items]
        return str(vacancy_names)

    def __str__(self):
        vacancy_info = "\n".join([
                                     f"Vacancy: {vacancy['name']},"
                                     f" Salary from: {vacancy['salary']['from']},"
                                     f" Salary to: {vacancy['salary']['to']},"
                                     f" Currency: {vacancy['salary']['currency']}"
                                     for vacancy in self.items])
        return vacancy_info

    def validate_salary_from(self):
        for vacancy in self.items:
            if vacancy["salary"]["from"] is None:
                vacancy["salary"]["from"] = 0

    def sort_by_salary_from(self, n=None):
        sorted_vacancies = sorted(self.items,
                                  key=lambda x: x["salary"]["from"] if x["salary"]["from"] is not None else float(
                                      'inf'))
        if n is not None:
            sorted_vacancies = sorted_vacancies[:n]
        return sorted_vacancies

    def count_vacancies_by_salary(self, n):
        salary_counts = {}
        for vacancy in self.items:
            salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] is not None else 0
            if salary_from in salary_counts:
                salary_counts[salary_from] += 1
            else:
                salary_counts[salary_from] = 1
        sorted_counts = sorted(salary_counts.items(), key=lambda x: x[0])
        return sorted_counts[:n]

    def filter_by_default_salary(self, min_salary):
        filtered_vacancies = [vacancy for vacancy in self.items if
                              vacancy["salary"]["from"] is not None and vacancy["salary"]["from"] > min_salary]
        return filtered_vacancies


# Example usage:
# manager = VacanciesHH("../data/vacancies.json")
# manager.validate_salary_from()
# sorted_vacancies = manager.sort_by_salary_from(5)
# print("Top 5 Vacancies by Minimum Salary:")
# for vacancy in sorted_vacancies:
#     print(vacancy["name"], vacancy["salary"]["from"])
#
# salary_counts = manager.count_vacancies_by_salary(5)
# # print("\nVacancy Count by Salary:")
# filter_by_default = manager.filter_by_default_salary(120)
#
# #salary_counts.__repr__()
# print(manager.__dict__)
