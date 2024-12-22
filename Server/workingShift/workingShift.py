from abc import abstractmethod, ABC

class WorkShift(ABC):
    def __init__(self,
                 worker,
                 date,
                 timeStartWork,
                 timeEndWork):
        self.worker = worker
        self.date = date
        self.timeStartWork = timeStartWork
        self.timeEndWork = timeEndWork
    def __str__(self):
        return f"""
        Работник: {self.worker}
        Дата смены: {self.date}
        Начало смен: {self.timeStartWork}
        Конец смены: {self.timeEndWork}
        """

class WorkShift1(WorkShift):
    def __init__(self,
                 worker,
                 date,
                 timeStartWork,
                 timeEndWork):
        self.worker = worker
        self.date = date
        self.timeStartWork = timeStartWork
        self.timeEndWork = timeEndWork
    def __str__(self):
        return f"""
        Работник: {self.worker}
        Дата смены: {self.date}
        Начало смен: {self.timeStartWork}
        Конец смены: {self.timeEndWork}
        """