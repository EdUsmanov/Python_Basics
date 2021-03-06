"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class IfError:
    def __init__(self, *args):
        self.num_list = []

    def input_num(self):

        while True:
            try:
                num = int(input('Введите число: '))
                self.num_list.append(num)
                print(f'Текущий список: {self.num_list} \n')
            except:
                print('Введено недопустимое значение. Введите число.')


if_error = IfError('2')
print(if_error.input_num())
