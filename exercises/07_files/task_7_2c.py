# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]
from sys import argv
config_sw1 = argv[1]
config_sw1_cleared = argv[2]
config_sw1_cleared = open('config_sw1_cleared', 'w')
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
