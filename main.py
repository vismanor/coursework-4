from src.classes.api_connect_class import ConnectAPI
from src.classes.new_vacancy_format import NewVacancyFormat
from src.classes.json_file_manager import JSONFileManager


def filter_vacancies(vacancies_list, filter_words):
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if vacancy.description is not None:
            exclude = False
            for word in filter_words:
                if word.lower() in vacancy.title.lower() or word.lower() in vacancy.description.lower():
                    exclude = True
                    break
            if not exclude:
                filtered_vacancies.append(vacancy)
    return filtered_vacancies


def user_interactions():

    """
        Интерактив с пользователем:
        1) Создание экземпляра класса для работы с API сайта hh.ru с вакансиями
        2) создаем экземпляр класса для действий с данными вакансий в JSON-файле
        3) Получаем поисковый запрос пользователя
        4) Создаем экземпляр класса NewVacancyFormat,
           передавая в него экземпляр класса ConnectAPI и ключевое слово
        5) Помещаем в список вакансии, приведенные к общему заданному виду
        6) Получаем от пользователя слова для исключения вакансии из поиска
        7) Фильтруем вакансии по словам для исключения, определяем их в переменную
        8) Принтуем пронумерованные отфильтрованные вакансии
        9) Получаем число для составления топа вакансий по зарплате
           или 0 — для отказа от составления топа
        10) Отбираем вакансии с указанной зп, ранжируем эти вакансии и принтим пронумерованно
        11) Получаем ввод о дальнейших действиях: либо завершаемся, либо рестартим
    :return:
    """

    # 1 — Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = ConnectAPI()

    # 2 — Создаем экземпляр класса для действий с данными вакансий в JSON-файле
    json_file_manager = JSONFileManager('data/vacancies.json')
    json_file_manager.del_data_dict()

    # 3 — Получаем поисковый запрос пользователя
    key_word = str(input("Введите ключевое слово для поиска: "))

    # 4 — Создаем экземпляр класса NewVacancyFormat,
    # передавая в него экземпляр класса ConnectAPI и ключевое слово
    vacancy_formatter = NewVacancyFormat(hh_api)

    # 5 — Помещаем в список вакансии, приведенные к общему заданному виду
    vacancies_list = vacancy_formatter.switch_to_new_format(key_word)

    # 6 — Получаем от пользователя слова для исключения вакансии из поиска
    filter_words = input('Введите слова, которые нужно исключить, через запятую: \n').split()

    # filtered_vacancies = [vacancy for vacancy in vacancies_list if vacancy.description is not None
    #                       and (not any(word.lower() in vacancy.description.lower() for word in filter_words)
    #                            and not any(word.lower() in vacancy.title.lower() for word in filter_words))]

    # 7 — Фильтруем вакансии по словам для исключения, определяем их в переменную
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # 8 — Принтуем пронумерованные отфильтрованные вакансии
    print("Найденные вакансии: \n")
    for idx, vacancy in enumerate(filtered_vacancies, start=1):
        print(f"{idx}. {vacancy}")
        json_file_manager.add_data_to_dict(vacancy)

    # 9 — Получаем число для составления топа вакансий по зарплате
    # или 0 — для отказа от составления топа
    top_n = int(input("Хотите получить топ N вакансий по заработной плате?\n"
                      "Введите введите число N, если 'да'. Иначе — 0: "))

    # 10 — Отбираем вакансии с указанной зп, ранжируем эти вакансии и принтим пронумерованно
    if top_n > 0:
        vacancies_with_salary = [vacancy for vacancy in filtered_vacancies if vacancy.salary_min is not None
                                 or vacancy.salary_max is not None]
        ranged_vacancies = sorted(vacancies_with_salary, key=lambda x: x.salary_min
                                  if x.salary_min is not None else float('inf'), reverse=True)
        print(f"\n Топ-{top_n} вакансий по зарплате: \n")
        for idx, vacancy in enumerate(ranged_vacancies[:top_n], start=1):
            print(f"{idx}. {vacancy}")

    # 11 — Получаем ввод о дальнейших действиях: либо завершаемся, либо рестартим
    end_input = int(input("Завершаем поиск? \nВведите 1, если 'да'; введите 2, если начинаем новый: "))
    if end_input == 1:
        exit()
    elif end_input == 2:
        user_interactions()


if __name__ == "__main__":
    print('Приветствую! \nПомогу найти работу мечты :)')
    user_interactions()
