"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open('1.txt', r, encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        lines = 0
        symbols = -1
        for el in content:
            lines += 1
            for i in el:
                symbols += 1
            print(el)
            print(f'Количество символов в строке: {symbols}')
            symbols = -1
    print(f'Количество строк в файле: {lines}')
except IOError:
    print('Произошла ошибка ввода-вывода')
