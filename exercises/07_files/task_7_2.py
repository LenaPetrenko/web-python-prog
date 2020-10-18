# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
config_sw1 = argv[1]
config_file = open(config_sw1, 'r')
for string in config_file:
    if not (string.startswith('!') or string.strip(' ') == ''):  
       print(string, end='')
