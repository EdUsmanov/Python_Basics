"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet!!!
"""
import subprocess
import chardet

args_ya = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(args_ya, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding'].encode('utf-8'))
    print(line.decode('utf-8'))

args_yo = ['ping', 'youtube.com']
yo_ping = subprocess.Popen(args_yo, stdout=subprocess.PIPE)
for line in yo_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding'].encode('utf-8'))
    print(line.decode('utf-8'))
