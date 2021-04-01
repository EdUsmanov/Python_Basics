"""
Задание 4. Реализовать метакласс DocMeta, проверяющий наличие строк документации
в методах подчиненных ему классов.

Подсказка:
1) перегрузить метод __init__ метакласса
2) достучаться до атрибутов подчиненного класса вам поможет параметр clsdict
3) большая подсказка:
if not getattr(value, "__doc__"):
    raise TypeError(f"Метод должен иметь строку документации")

Создать подчиненный класс и проверить работу всего проекта
"""


class DocMeta(type):
    def __init__(self, clsname, bases, clsdict):
        for key, value in clsdict.items():
            if key.startswith('__'):
                continue

            if not hasattr(value, '__call__'):
                continue

            if not getattr(value, '__doc__'):
                raise TypeError("Метод должен иметь строку документации")

        type.__init__(self, clsname, bases, clsdict)


class Document(metaclass=DocMeta):
    pass


class Document1(Document):

    def met1(self, a, b):
        ''' Метод 1 выполняет функцию '''
        pass

    def met2(self):
        pass
