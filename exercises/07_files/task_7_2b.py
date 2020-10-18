# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
from sys import argv
config_sw1 = argv[1]
config_sw1_cleared = open('config_sw1_cleared.txt', 'w')
config_file = open(config_sw1, 'r')
for string in config_file:
    if not (string.startswith('!') or string.strip(' ') == ''):  
      comand_ignore = False
      for ign in ignore:
        if string.find(ign) >=0:
         comand_ignore = True
         break
      if not comand_ignore:  
         config_sw1_cleared.write(string)
