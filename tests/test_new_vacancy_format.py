import pytest
from src.classes.api_connect_class import ConnectAPI
from src.classes.new_vacancy_format import NewVacancyFormat


@pytest.fixture
def api_instance():
    """
        Создаем экземпляр класса ConnectAPI для тестирования
    """
    return ConnectAPI()


@pytest.fixture
def formatter_instance(api_instance):
    """
        Возвращаем экземпляр класса NewVacancyFormat, используя api_instance.
    :param api_instance:
    :return:
    """
    return NewVacancyFormat(api_instance)


def test_switch_to_new_format(formatter_instance):
    """
        Проверяется, что возвращенные значения в новом формате
    :param formatter_instance:
    :return:
    """
    key_word = 'python junior'
    vacancies = formatter_instance.switch_to_new_format(key_word)
    assert isinstance(vacancies, list)
