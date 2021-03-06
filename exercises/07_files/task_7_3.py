# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
'''with open('/home/std/python-web/exercises/07_files/CAM_table.txt', 'r') as file_table:
    for line in file_table:
        if line.count('.') is 2:
         line.split(' ')
         vlan = line[0:4]
         mac = line[4:24]
         ports = line [36:] 
         print_line = 
         print(print_line.format(vlan, mac, ports), end='')'''

import re
file_table = open('/home/std/python-web/exercises/07_files/CAM_table.txt', 'r')
for line in file_table:
    if re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None:
        print(line.replace('DYNAMIC     ',''), end='')
