from src.class_api import *
from src.class_file import ClassFile


def main():

    # print(ClassAPIHH().get_api("системный администратор", "1"))
    vacancy = ClassAPIHH().get_api("системный администратор", "2")
    ClassFile.save_to_file(vacancy)

    ClassAPIHHR().get_api()

    # print(ClassFile.load_from_file().get("items"))
    for i in ClassFile.load_from_file():
        print(i.get("name"))


if __name__ == "__main__":
    main()
