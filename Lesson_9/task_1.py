"""
Задание 1.

Реализовать класс «Дата», конструктор которого должен принимать дату
в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return 'Дата корректна'
                else:
                    return 'Неправильный год'
            else:
                return 'Неправильный месяц'
        else:
            return 'Неправильный день'

    def __str__(self):
        return f'{Date.extract(self.day_month_year)}'


today = Date('11 - 11 - 2020')
print(today)
print(Date.valid(11, 11, 2022))
print(today.valid(11, 13, 2020))
print(Date.extract('11 - 11 - 2019'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(1, 7, 1996))
