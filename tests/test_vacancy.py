import pytest
from src.classes.vacancy import Vacancy


@pytest.fixture
def test_vacancy():
    vacancies = [
        Vacancy(title="Test Title", url="test_url", employer="Test Employer",
                requirement="Test Requirement", description="Test Description",
                salary=""),
        Vacancy(title="Junior программист Python", employer='ПерилаГлавСнаб',
                salary="60 000-80 000 руб.", url='https://hh.ru/vacancy/93804724',
                requirement='Уверенное знание Python. Уверенное знание SQL(PSQL, MSSQL).',
                description='Поддержка микросервисов. Разработка интеграций.'),
        Vacancy(title="Python Developer", url="Google", employer="Test Employer",
                requirement="Python", description="Write tests",
                salary="от 120000 руб."),

    ]
    return vacancies


def test_init_vacancy(test_vacancy):
    vacancy_2 = test_vacancy[1]
    assert vacancy_2.title == 'Junior программист Python'
    assert vacancy_2.employer == 'ПерилаГлавСнаб'
    assert vacancy_2.salary_min == 60000
    assert vacancy_2.salary_max == 80000
    assert vacancy_2.url == 'https://hh.ru/vacancy/93804724'
    assert vacancy_2.requirement == 'Уверенное знание Python. Уверенное знание SQL(PSQL, MSSQL).'
    assert vacancy_2.description == 'Поддержка микросервисов. Разработка интеграций.'


def test_get_salary_display(test_vacancy):
    vacancy_1 = test_vacancy[0]
    vacancy_2 = test_vacancy[1]
    vacancy_3 = test_vacancy[2]

    assert vacancy_1.get_salary_display() == "данные о заработной плате отсутствуют"
    assert vacancy_2.get_salary_display() == "от 60000 до 80000 руб."
    assert vacancy_3.get_salary_display() == "от 120000 руб."


def test_check_salary_str(test_vacancy):
    vacancy_2 = test_vacancy[1]
    assert vacancy_2.salary_min == 60000
    assert vacancy_2.salary_max == 80000

