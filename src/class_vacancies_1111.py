import json
import re


class VacanciesHH:
    """docstring for VacanciesHH"""

    def __init__(self, filename):
        # with open(filename, 'r', encoding='utf-8') as file:
        self.items = filename.get('items')

        self.validate_salary_from()
        self.validate_salary_to()
        self.validate_snippet_requirement()
        self.validate_snippet_responsibility()

    def __repr__(self):
        # vacancy_names = [vacancy['salary']['from'] for vacancy in self.items]
        # return str(vacancy_names)
        vacancy_info = "\n".join([
            f"Вакансия: {vacancy['name']},"
            f" Зарплата от: {vacancy['salary']['from']},"
            f" Зарплата до: {vacancy['salary']['to']}"
            f" Валюта зарплаты: {vacancy['salary']['currency']}"
            for vacancy in self.items])
        return vacancy_info

    def __str__(self):
        vacancy_info = "\n".join([
            f"Вакансия: {vacancy['name']},"
            f" Регион: {vacancy['area']['name']},"
            f" Зарплата от: {vacancy['salary']['from']},"
            f" Зарплата до: {vacancy['salary']['to']},"
            f" Валюта зарплаты: {vacancy['salary']['currency']},"
            f" Комментарий: {vacancy['snippet']['requirement']},"
            f" Обязанности: {vacancy['snippet']['responsibility']},"
            f" Ссылка: {vacancy['url']}"
            for vacancy in self.items])
        return vacancy_info

    def __len__(self):
        items_vacancy_name = [vacancy for vacancy in self.items if vacancy['name']]
        return len(items_vacancy_name)

    def print_vacancies(self):
        words_to_replace = ['<highlighttext>', '</highlighttext>']
        print("\n".join([
            f"Вакансия: {vacancy['name']}\n"
            f"Регион: {vacancy['area']['name']}\n"
            f"Зарплата от: {vacancy['salary']['from']}\n"
            f"Зарплата до: {vacancy['salary']['to']}\n"
            f"Валюта зарплаты: {vacancy['salary']['currency']}\n"
            f"Комментарий: {self.remove_words(vacancy['snippet']['requirement'], words_to_replace)}\n"
            f"Обязанности: {self.remove_words(vacancy['snippet']['responsibility'], words_to_replace)}\n"
            f"Ссылка: {vacancy['url']}\n"
            for vacancy in self.items]))


    def save_vacancies_json(self):
        # with open('vacancies.txt', 'w', encoding='utf-8') as file:
        #     file.write(str(self))
        save_items = []
        for vacancy in self.items:
            dict_sample = {}
            dict_sample["Вакансия"] = vacancy['name']
            dict_sample["Регион"] = vacancy['area']['name']
            dict_sample["Зарплата от"] = vacancy['salary']['from']
            dict_sample["Зарплата до"] = vacancy['salary']['to']
            dict_sample["Валюта зарплаты"] = vacancy['salary']['currency']
            dict_sample["Комментарий"] = vacancy['snippet']['requirement']
            dict_sample["Обязанности"] = vacancy['snippet']['responsibility']
            dict_sample["Ссылка"] = vacancy['url']
            save_items.append(dict_sample)
        return save_items

    def save_vacancies_txt(self):
        # with open('vacancies.txt', 'w', encoding='utf-8') as file:
        #     file.write(str(self))
        save_items = ("\n".join([
            f"Вакансия: {vacancy['name']}\n"
            f"Регион: {vacancy['area']['name']}\n"
            f"Зарплата от: {vacancy['salary']['from']}\n"
            f"Зарплата до: {vacancy['salary']['to']}\n"
            f"Валюта зарплаты: {vacancy['salary']['currency']}\n"
            f"Комментарий: {vacancy['snippet']['requirement']}\n"
            f"Обязанности: {vacancy['snippet']['responsibility']}\n"
            f"Ссылка: {vacancy['url']}\n"
            for vacancy in self.items]))

        return save_items

    def validate_salary_from(self):
        for vacancy in self.items:
            if vacancy["salary"]["from"] is None:
                vacancy["salary"]["from"] = 0

    def validate_salary_to(self):
        for vacancy in self.items:
            if vacancy["salary"]["to"] is None:
                vacancy["salary"]["to"] = "0"

    def validate_snippet_requirement(self):
        for vacancy in self.items:
            if vacancy['snippet']['requirement'] is None:
                vacancy['snippet']['requirement'] = "Не указано"

    def validate_snippet_responsibility(self):
        for vacancy in self.items:
            if vacancy['snippet']['responsibility'] is None:
                vacancy['snippet']['responsibility'] = "Не указано"

    def number_of_selected(self, n=None):
        # self.items = sorted(self.items,
        #                     key=lambda x: x["salary"]["from"] if x["salary"]["from"] is not None else
        #                     float('inf'))
        # if n is not None:
        self.items = self.items[0:n]
        return self.items

    def sort_by_salary_desc(self):
        self.items = sorted(self.items,
                            key=lambda x: x["salary"]["from"] if x["salary"]["from"] is not None else float(
                                '-inf'), reverse=True)
        return self.items

    def filter_salary_from(self, min_salary):
        """Фильтровать вакансии по зарплате от"""
        self.items = [vacancy for vacancy in self.items if vacancy["salary"]["from"] > min_salary]
        return self.items

    def filter_salary_to(self, max_salary):
        """Фильтровать вакансии по зарплате до"""
        self.items = [vacancy for vacancy in self.items if vacancy["salary"]["to"] < max_salary]
        return self.items

    @staticmethod
    def remove_words(text, words_to_remove):
        if text is None:
            return None

        for word in words_to_remove:
            if text is not None:
                text = text.replace(word, "")
        return text