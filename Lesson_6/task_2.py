"""
2. Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words_list = [b'class', b'function', b'method']

for line in words_list:
    print(f'Тип переменной: {format(type(line))}')
    print(f'Содержание переменной: {format(line)}')
    print(f'Длина строки: {format(len(line))}')