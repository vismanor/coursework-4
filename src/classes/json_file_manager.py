import json
from src.classes.abstract_work_with_vacancy_class import AbstractVacancyWorker
from src.classes.vacancy import Vacancy


class JSONFileManager(AbstractVacancyWorker):

    def __init__(self, filename: str):
        self.filename = filename

    def add_data_to_dict(self, vacancy: Vacancy):
        with open(self.filename, 'a', encoding='UTF-8') as file:
            json.dump(vacancy.__dict__, file)
            file.write('\n')

    def get_data_from_dict(self, filter_words):
        with open(self.filename, 'r', encoding='UTF-8') as file:
            vacancies = [json.loads(line) for line in file.readlines()]
        return vacancies

    def del_data_dict(self):
        open(self.filename, 'w').close()
