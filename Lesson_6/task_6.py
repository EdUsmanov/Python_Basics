"""
6. Создать НЕ! программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Проверить кодировку файла по умолчанию.

Принудительно!!!!! открыть файл в формате Unicode - encoding='utf-8'
и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""
from chardet.universaldetector import UniversalDetector

DETECTOR = UniversalDetector
with open ('1.txt', 'rb') as test_file:
    for i in test_file:
        DETECTOR.feed(i)
        if DETECTOR.done:
            break
    DETECTOR.close()
print(DETECTOR.result['encoding'])

with open('1.txt', 'r', encoding='utf-8') as test_file:
    content = file.read()
print(content)
