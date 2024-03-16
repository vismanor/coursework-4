import pytest
from main import filter_vacancies, user_interactions
from src.classes.vacancy import Vacancy


def test_filter_vacancies():
    vacancies_list = [
        Vacancy(title="Junior Python backend developer", employer='Google',
                salary="60000-80000", url='',
                requirement='Для этого мы ищем начинающего, сообразительного, шустрого, '
                            'амбициозного интерна-джуна питониста. Опыт в коммерческой '
                            'разработке не требуется',
                description='Писать тесты. Писать фичи. Писать фронт. Диплоить проекты.'),
        Vacancy(title="Middle Python Frontend Developer", employer='Geeky', salary="60000",
                requirement='Вы пробовали что-то писать на любом языке программирования и '
                            'вам это понравилось.', url='',
                description='Разработка совместно с командой')
    ]

    filtered_vacancies = filter_vacancies(vacancies_list, ['frontend'])
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].title == 'Junior Python backend developer'


def test_user_interactions():
    vacancies_list = [
        Vacancy(title="Junior Python backend developer", employer='Google',
                salary="60000-80000", url='',
                requirement='Для этого мы ищем начинающего, сообразительного, шустрого, '
                            'амбициозного интерна-джуна питониста. Опыт в коммерческой '
                            'разработке не требуется',
                description='Писать тесты. Писать фичи. Писать фронт. Диплоить проекты.'),
        Vacancy(title="Junior Python developer", employer='Geegle',
                salary="50000-70000", url='',
                requirement='Ищем начинающего интерна-джуна питониста. Опыт в коммерческой '
                            'разработке не обязателен. Высшее необязательно.',
                description='Писать тесты. Писать фичи. Писать код.'),
        Vacancy(title="Junior Python developer", employer='Eagle',
                salary="50000-70000", url='',
                requirement='Ищем начинающего интерна-джуна питониста. Опыт в коммерческой '
                            'разработке обязателен. Высшее обязательно.',
                description='Писать тесты. Писать фичи. Писать frontend. Писать код.'),
        Vacancy(title="Middle Python Frontend Developer", employer='Geeky', salary="100000",
                requirement='Вы пробовали что-то писать на любом языке программирования и '
                            'вам это понравилось.', url='',
                description='Разработка совместно с командой'),
        Vacancy(title="Lead Python Backend Developer", employer='GBInternational', salary="160000",
                requirement='Вы гуру программирования, несколько крупных проектов в портфолио.',
                url='', description='Разработка совместно с командой')
    ]

    key_word = 'junior python backend developer'

    filter_words = 'frontend, lead, middle'
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

