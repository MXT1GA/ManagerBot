from abc import abstractmethod, ABC

class Worker(ABC):
    def __init__(self,
                 patronymic,
                 name,
                 lastname,
                 number):
        self.patronymic = patronymic
        self.name = name
        self.lastname = lastname
        self.number = number

    def __str__(self):
        return f"""
        Отчество: {self.patronymic}
        Имя: {self.name}
        Фамилия: {self.lastname}
        Номер телефона: {self.number}
        """