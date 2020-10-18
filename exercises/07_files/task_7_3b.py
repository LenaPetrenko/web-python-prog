# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import re
new_vlan = input('Введите номер vlan: ')
new_vlan = int(new_vlan)
file_table = open('/home/std/python-web/exercises/07_files/CAM_table.txt', 'r')
for line in file_table:
    if re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None:
        vlan = line.split()[0]
        vlan= int(vlan)
        if new_vlan == vlan:
            print(line.replace('DYNAMIC     ',''), end='')
