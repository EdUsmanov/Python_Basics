"""
Создать класс-сущность: ExamEGE. Сделать его заглушкой.

Создать класс-дескриптор Grade (оценка). Реализовать его по новому протоколу дескрипторов.

В классе-дескрипторе реализовать перегрузку:

1) __get__ - должно возвращаться значение атрибута плюс сообщение
print(f"Вы получили доступ к оценке за экзамен по предмету: '{self.name}'")

2) __set__ - если значение атрибута не вписалось в диапазон (1-100),
аозбуждать исключение ValueError с выводом соответствующего сообщения,
Если значение вписалось - присваивать его атрибуту.

Продолжить работу над классом ExamEGE.
Создать вместо заглушки атрибуты на уровне класса. Сделать их дескрипторами (экземплярами класса Grade).
В конструктор класса при этом передвать название предмета.
Например,
math_grade = Grade('Математика')
russian_grade = Grade('Русский язык')
history_grade = Grade('История')

Проверить работу проекта на разных ситуациях с помощью клиентского кода.

Например,
math_grade = Grade('Математика')
russian_grade = Grade('Русский язык')
history_grade = Grade('История')

Проверить работу проекта на разных ситуациях с помощью клиентского кода.
"""


class Grade:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return f'Вы получили доступ к оценке за экзамен по предмету {self.name}'

    def __set__(self, instance, value):
        if not (1 <= value <= 100):
            raise ValueError('Некорректный балл ЕГЭ')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class ExamEGE:
    math_grade = Grade('Математика')
    russian_grade = Grade('Русский язык')
    history_grade = Grade('История')

    def __init__(self, math_grade, russian_grade, history_grade):
        self.math_grade = math_grade
        self.russian_grade = russian_grade
        self.history_grade = history_grade

    def sum(self):
        return self.math_grade + self.russian_grade + self.history_grade


grades = ExamEGE(101, 98, 76)

print(grades.sum())
