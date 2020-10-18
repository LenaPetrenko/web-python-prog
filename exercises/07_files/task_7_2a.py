# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
from sys import argv
config_sw1 = argv[1]
config_file = open(config_sw1, 'r')
for string in config_file:
    if not (string.startswith('!') or string.strip(' ') == ''):  
      comand_ignore = False
      for ign in ignore:
        if string.find(ign) >=0:
         comand_ignore = True
         break
      if not comand_ignore:  
         print(string, end='')

