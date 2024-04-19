import os
import json
from src.absclasses import AbstractClassFile
from src.class_vacancies_collection import VacanciesCollection


class ClassFile(AbstractClassFile):

    @staticmethod
    def save_to_file(vacancies, filename) -> None:
        """Запись списка вакансий в файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            f.write(vacancies_json)

    @staticmethod
    def save_to_file_txt(vacancies, file_path) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            for vacancy in vacancies:
                file.write(f"Вакансия: {vacancy.name},\n"
                           f"Город: {vacancy.area_name},\n"
                           f"Зарплата от: {vacancy.salary_from},\n"
                           f"Зарплата до: {vacancy.salary_to},\n"
                           f"Валюта зарплаты: {vacancy.salary_currency},\n"
                           f"Комментарий: {vacancy.snippet_requirement},\n"
                           f"Обязанности: {vacancy.snippet_responsibility},\n"
                           f"Дата публикации: {VacanciesCollection.convert_date(vacancy.published_at)},\n"
                           f"График работы: {vacancy.schedule_name},\n"
                           f"Опыт работы: {vacancy.experience_name}\n"
                           f"Ссылка: {vacancy.url}\n\n")

    @staticmethod
    def load_from_file(filename) -> list:
        with open(filename, "r", encoding="utf8") as f:
            vacancies = json.load(f)
        return vacancies

    @staticmethod
    def delete_from_file(filename) -> None:
        if os.path.exists(filename):
            os.remove(filename)
