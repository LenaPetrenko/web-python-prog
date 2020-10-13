# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = (input('Введите ip-адрес в формате 10.0.1.1: '))

broadcast_ip = '255.255.255.255'
unassigned_ip = '0.0.0.0'

ip_work = ip.split('.')

ip_count = 0
if len(ip_work) == 4:
  for i in ip_work:
    if i.isdigit() and (0 <= int(i) <= 255):
      ip_count = ip_count + 1
if ip_count !=4:
  print ('Неправильный IP-адрес')
  exit()

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
