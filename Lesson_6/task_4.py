"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words_list = ['разработка', 'администрирование', 'protocol']

for el in words_list:
    a = el.encode('utf-8')
    print(a, type(a))
    b = a.decode('utf-8')
    print(b, type(b))
