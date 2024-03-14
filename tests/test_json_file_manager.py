import os
import json
import os.path

import pytest
from src.classes.json_file_manager import JSONFileManager
from src.classes.vacancy import Vacancy


@pytest.fixture
def json_manager():

    return JSONFileManager('test_vacancies.json')


def test_add_data_to_dict(json_manager):

    vacancy = Vacancy("Test Title", "test_url", "Test Employer",
                      "Test Requirement","Test Description",
                      "1000-2000")
    json_manager.add_data_to_dict(vacancy)

    with open('test_vacancies.json', 'r', encoding='UTF-8') as test_file:
        vacancies = [json.loads(line) for line in test_file.readlines()]

    assert len(vacancies) == 1
    assert vacancies[0]['title'] == 'Test Title'


def test_get_data_from_dict(json_manager):
    vacancies = json_manager.get_data_from_dict([])
    assert len(vacancies) == 1
    assert vacancies[0]['title'] == 'Test Title'


def test_del_data_dict(json_manager):
    json_manager.del_data_dict()

    with open('test_vacancies.json', 'r', encoding='UTF-8') as test_file:
        vacancies = [json.loads(line) for line in test_file.readlines()]

    assert len(vacancies) == 0
    assert os.path.exists('test_vacancies.json')

    os.remove('test_vacancies.json')
