from src.classes.api_connect_class import ConnectAPI
from src.classes.vacancy import Vacancy


class NewVacancyFormat:

    def __init__(self, api: ConnectAPI):
        self.api = api

    def switch_to_new_format(self, key_word: str):
        vacancies_data = self.api.get_vacancies(key_word)
        vacancies = []
        for vacancy_data in vacancies_data:
            snippet = vacancy_data['snippet']
            salary = vacancy_data['salary']
            if salary:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                salary_range = f"{salary_from}-{salary_to}" if salary_from and salary_to else None
            else:
                salary_range = "Данные отсутствуют"

            vacancy = Vacancy(
                title=vacancy_data['name'],
                url=vacancy_data['alternate_url'],
                employer=vacancy_data['employer']['name'],
                requirement=snippet.get('requirement', ''),
                description=snippet.get('responsibility', ''),
                salary=salary_range
            )
            vacancies.append(vacancy)
        return vacancies
