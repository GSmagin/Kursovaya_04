from confing import dir_json_vacancies, dir_json_vacancies_sort
import json


class ClassFile:

    @staticmethod
    def save_to_file(vacancies, filename=dir_json_vacancies):
        """Запись списка вакансий в файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            f.write(vacancies_json)

    @staticmethod
    def load_from_file(filename=dir_json_vacancies):
        with open(filename, "r", encoding="utf8") as f:
            vacancies = json.load(f)
        return vacancies

    def delete_from_file(self, filename=dir_json_vacancies_sort):
        pass
