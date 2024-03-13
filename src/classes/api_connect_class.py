import requests
from src.classes.abstract_api_class import AbstractAPIWorker

url_get = "https://api.hh.ru/vacancies/"


class ConnectAPI(AbstractAPIWorker):
    """
        Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru
    """
    def __init__(self, area=113) -> None:
        """
        # :param vacancy_list: список вакансий
        """
        self.url = url_get
        self.area = area

    def get_vacancies(self, key_word: str):
        """
        Умеет подключаться к API и получать вакансии
        """
        response = requests.get(self.url, params={"text": key_word, "area": self.area})
        response_dict = response.json()

        return response_dict['items']
