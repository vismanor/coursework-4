from abc import ABC, abstractmethod
from src.classes.vacancy import Vacancy


class AbstractVacancyWorker(ABC):
    """
        Абстрактный класс который обязывает реализовать методы
        для добавления вакансий в файл, получения данных из файла
        по указанным критериям и удаления информации о вакансиях
    """
    @abstractmethod
    def add_data_to_dict(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_data_from_dict(self, keys):
        pass

    @abstractmethod
    def del_data_dict(self):
        pass
