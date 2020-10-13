# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:

  ip = (input('Введите ip-адрес в формате 10.0.1.1: '))

  broadcast_ip = '255.255.255.255'
  unassigned_ip = '0.0.0.0'

  ip_work = ip.split('.')

  ip_count = 0
  if len(ip_work) == 4:
    for i in ip_work:
      if i.isdigit() and (0 <= int(i) <= 255):
        ip_count = ip_count + 1
  if ip_count ==4:
   break
  print('Неправильный IP-адрес')

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
