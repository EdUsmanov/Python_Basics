"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""
words = str(input("Введите слова через пробел:"))
new_words = words.split(" ")
k = 0
for el in new_words:
    k += 1
    if len(el) < 11:
        print(f"{k}. {el}")
    else:
        print(f"{k}. {el[0:10]}")
