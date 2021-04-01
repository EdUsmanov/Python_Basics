"""
Создать класс-сущность: MyClass. Сделать его заглушкой.

Создать класс-дескриптор TypedProperty. Реализовать его по новому протоколу дескрипторов.

В классе-дескрипторе реализовать перегрузку:
1) __set__ - проверяет относится ли присваиваемое значение к типу данных, указанному
и переданному в конструктор класса-дескриптора
Если не относится, возбуждать исключение TypeError
с выводом сообщения "Значение должно быть типа {self.type}"
Если относится, присвоить значение атрибуту.

2) __delete__ - при попытке удаления атрибута давать исключение
AttributeError с выводом соответствующего сообщения.

Продолжить работу над классом MyClass.
Создать вместо заглушки атрибуты на уровне класса. Сделать их дескрипторами (экземплярами класса TypedProperty).
В конструктор класса при этом передвать тип данных

Например,
name = TypedProperty(str)

Проверить работу проекта на разных ситуациях с помощью клиентского кода..
"""


class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = '_' + name
        self.type = type_name
        self.default = default if default else type_name()

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f'Значение должно быть типа {self.type}')
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError('Невозможно удалить аттрибут')


class MyClass:
    name = TypedProperty('name', str)
    num = TypedProperty('name', int)


m = MyClass()
a = m.name
b = m.num
m.name = '123'
m.num = '123'
del m.num
