# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = (input('Введите ip-адрес в формате 10.0.1.1: '))

broadcast_ip = '255.255.255.255'
unassigned_ip = '0.0.0.0'

ip_work = ip.split('.')
okt1 = int(ip_work[0])
okt2 = int(ip_work[1])
okt3 = int(ip_work[2])
okt4 = int(ip_work[3])

if 1<= okt1 <=223: 
  print('This is unicast IP')
elif 224 <= okt1 <=239:
  print('This is multicast IP')
elif ip == broadcast_ip: 
 print('this is local broadcast IP')
elif ip == unassigned_ip:
 print('this is unassigned IP')
else:
  print('this is unused IP')

