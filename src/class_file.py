import os
from confing import DIR_JSON_VACANCIES, DIR_JSON_VACANCIES_SORT ,DIR_JSON_VACANCIES_SORT_TXT
import json


class ClassFile:

    @staticmethod
    def save_to_file(vacancies, filename=DIR_JSON_VACANCIES) -> None:
        """Запись списка вакансий в файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            f.write(vacancies_json)

    @staticmethod
    def save_to_file_txt(vacancies, filename=DIR_JSON_VACANCIES_SORT_TXT):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(vacancies))

    @staticmethod
    def save_to_file_append(vacancies, filename=DIR_JSON_VACANCIES):
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
                f.write(vacancies_json)
        else:
            with open(filename, "a", encoding="utf8") as f:
                vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
                f.write(vacancies_json)

    @staticmethod
    def load_from_file(filename=DIR_JSON_VACANCIES) -> list:
        with open(filename, "r", encoding="utf8") as f:
            vacancies = json.load(f)
        return vacancies

    @staticmethod
    def delete_from_file(filename=DIR_JSON_VACANCIES) -> None:
        if os.path.exists(filename):
            os.remove(filename)


