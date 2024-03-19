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
            print(salary)
            if salary:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                if salary_from is not None:  # {'from': 10000, 'to': 60000}
                    if salary_to is not None:  # {'from': 10000, 'to': 60000}
                        salary_range = f'{salary_from}-{salary_to} руб.'
                    else:  # {'from': 10000, 'to': null}
                        salary_range = f'от {salary_from} руб.'
                else:  # {'from': null, 'to': 60000}
                    if salary_to is not None:  # {'from': null, 'to': 60000}
                        salary_range = f'до {salary_to} руб.'
                    else:  # {'from': null, 'to': null}
                        salary_range = 'данные о заработной плате отсутствуют'

            #     if salary_from is not None:  # {'from': 10000, 'to': 60000, 'currency': 'RUR', 'gross': True}
            #         if salary_to is not None:  # {'from': 10000, 'to': 60000, 'currency': 'RUR', 'gross': True}
            #             salary_range = f"{salary_from}-{salary_to}"
            #         else:  # {'from': 10000, 'to': None, 'currency': 'RUR', 'gross': False}
            #             salary_range = f"от {salary_from} руб."
            #     else:  # {'from': None, 'to': 50000, 'currency': 'RUR', 'gross': True}
            #         salary_range = f"до {salary_to} руб."
            # else:
            #     salary_range = salary_range_default

            #     if salary_from is not None and salary_to is not None:
            #         salary_range = f"{salary_from}-{salary_to}"
            #     elif salary_from is not None:
            #         salary_range = f"от {salary_from}"
            #     elif salary_to is not None:
            #         salary_range = f"до {salary_to}"
            # else:
            #     salary_range = salary_range_default

                vacancy = Vacancy(
                    title=vacancy_data['name'],
                    url=vacancy_data['alternate_url'],
                    employer=vacancy_data['employer']['name'],
                    requirement=snippet.get('requirement', ''),
                    description=snippet.get('responsibility', ''),
                    salary=salary_range
                )
                vacancies.append(vacancy)
                print(vacancy)
        return vacancies
