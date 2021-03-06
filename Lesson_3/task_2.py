"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456

"""
name = input('Введите имя: ')
s_name = input('Введите фамилию: ')
b_date = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите номер телефона: ')


def card(name, s_name, b_date, town, email, tel):
    """
    Ф-я для вывода данных пользователя
    :param name: Имя
    :param s_name: Фамилия
    :param b_date: Год рождения
    :param town: Город проживания
    :param email: эл почта
    :param tel: телефон
    :return: карточка с данными пользователя
    """
    return (f'{name} {s_name} {b_date} года рождения, '
            f'проживает в городе {town}, email: {email},'
            f' телефон: {tel}')


print(str(card(name, s_name, b_date, town, email, tel)))
