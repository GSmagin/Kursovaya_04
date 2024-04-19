from abc import ABC, abstractmethod


class AbstractClassVacanciesHH(ABC):

    @abstractmethod
    def validate_salary_from(self):
        pass

    @abstractmethod
    def validate_salary_to(self):
        pass


class AbstractClassAPI(ABC):

    @abstractmethod
    def api_get_pages(self, word_search, region, num_pages) -> dict[list]:
        pass


class AbstractClassClassAPIHHR(ABC):

    @staticmethod
    @abstractmethod
    def get_api_region() -> dict:
        pass


class AbstractClassFile(ABC):

    @staticmethod
    @abstractmethod
    def save_to_file(vacancies, filename) -> None:
        pass

    @staticmethod
    @abstractmethod
    def save_to_file_txt(vacancies, filename) -> None:
        pass

    @staticmethod
    @abstractmethod
    def load_from_file(filename) -> list:
        pass

    @staticmethod
    @abstractmethod
    def delete_from_file(filename) -> None:
        pass
