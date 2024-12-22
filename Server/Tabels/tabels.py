from abc import abstractmethod, ABC

class Tabel(ABC):
    def __init__(self, period):
        self.period = period

class DayTabel(Tabel):
    def __init__(self,
                 period,
                 timeStartWork,
                 timeEndWork,
                 startAbsence,
                 endAbsence,
                 startLunchTime,
                 endLunchTime):
        self.period = period
        self.timeStartWork = timeStartWork
        self.timeEndWork = timeEndWork
        self.startAbsence = startAbsence
        self.endAbsence = endAbsence
        self.startLunchTime = startLunchTime
        self.endLunchTime = endLunchTime

    def __str__(self):
        return f"""
                Отчет за день: {self.period}
                Рабочее время: {self.timeStartWork} - {self.timeEndWork}
                Отсутствие: {self.startAbsence} - {self.endAbsence}
                Обеденное время: {self.startLunchTime} - {self.endLunchTime}
                """

class MonthTabel(Tabel):
    def __init__(self,
                 period,
                 timeWork,
                 timeAbsense,
                 timeLunch):
        self.period = period
        self.timeWork = timeWork
        self.timeAbsense = timeAbsense
        self.timeLunch = timeLunch

    def __str__(self):
        return f"""
                Отчет за месяц: {self.period}
                Общее рабочее время: {self.timeWork}
                Общее отсутствие: {self.timeAbsense}
                Общее обеденное время: {self.timeLunch}
                """