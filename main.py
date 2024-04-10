from src.class_api import *
from src.class_file import ClassFile


def main():

    # Запрос информации для отправки запроса на сервер HH API
    name_vacancy = input('Введите название вакансии: ')
    ClassAPIHHR().get_api()
    name_region = input('\nВведите название id региона (по умолчанию Москва): \n')
    if not name_region:
        name_region = '1'
    vacancy = ClassAPIHH().get_api(name_vacancy, name_region)
    # сохранение в файл результата запроса
    ClassFile.save_to_file(vacancy)



    # print(ClassFile.load_from_file().get("items"))
    for i in ClassFile.load_from_file():
        print(f"{i.get('area').get('name')}, {i.get('name')}")


if __name__ == "__main__":
    main()
