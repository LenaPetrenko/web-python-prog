# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = (input('ввесди IP-сети в формате: 10.1.1.0/24 '))
network = ip[:ip.find('/')] 
bin_network = network.split('.')

pr_mask= ip[ip.find('/')::] 
mask = ip[ip.find('/')+1::] 
bin_mask = int(mask)
bin_mask = '1' * bin_mask
bin_mask = "{:<032}".format(bin_mask)

print_network = '''
 Network:
 {0:<8} {1:<8} {2:<8} {3:<8}
 {0:<08b} {1:<08b} {2:<08b} {3:<08b}
 '''
print_mask = '''
 Mask:
 {4:<}
 {0:<10} {1:<10} {2:<10} {3:<10}
 {0:<10b} {1:<10b} {2:<10b} {3:<10b}
 ''' 
print(print_network.format(int(bin_network[0]), int(bin_network[1]), int(bin_network[2]), int(bin_network[3])))
print(print_mask.format(int(bin_mask[0:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2), pr_mask))
