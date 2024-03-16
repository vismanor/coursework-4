class Vacancy:
    def __init__(self, title: str, url: str, employer: str, requirement: str,
                 description: str, salary) -> None:
        self.title = title
        self.url = url
        self.employer = employer
        self.requirement = requirement
        self.description = description
        self.salary_min = None
        self.salary_max = None
        self.check_salary(salary)

    def __repr__(self):
        return f"{self.title}\n{self.employer}\n{self.salary_min}\n{self.description}\n{self.url}"

    def __str__(self) -> str:
        return (f"Вакансия: {self.title}\n"
                f"Работодатель: {self.employer}\n"
                f"Заработная плата: {self.get_salary_display()}\n"
                f"Требования: {self.requirement}\n"
                f"Описание: {self.description}\n"
                f"Ссылка на вакансию: {self.url}\n")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            if self.salary_min and other.salary_min:
                return self.salary_min > other.salary_min
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            if self.salary_min and other.salary_min:
                return self.salary_min < other.salary_min
            else:
                return False

    def get_salary_display(self) -> str:
        if self.salary_min is not None:  # если минималка есть
            if self.salary_max is not None:  # если максималка есть
                return f"от {self.salary_min} до {self.salary_max} руб."
            else:  # если максималки нет
                return f"от {self.salary_min} руб."
        if self.salary_max is not None:
            return f"до {self.salary_max} руб."
        return "данные о заработной плате отсутствуют"

    def check_salary(self, salary):
        if isinstance(salary, str) and '-' in salary:
            salary_parts = salary.split('-')
            self.salary_min = int(''.join(filter(str.isdigit, salary_parts[0])))
            self.salary_max = int(''.join(filter(str.isdigit, salary_parts[1])))
        elif isinstance(salary, int):
            self.salary_min = salary
            self.salary_max = salary
        elif isinstance(salary, dict):
            self.salary_min = salary.get('from')
            self.salary_max = salary.get('to')
        else:
            self.salary_min = None
            self.salary_max = None
