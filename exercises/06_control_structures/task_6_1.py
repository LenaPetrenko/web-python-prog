# -*- coding: utf-8 -*-
"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac_cisco = mac
mac_cisco = ','.join(mac_cisco)
mac_cisco = mac_cisco.replace(':', '.')
mac_cisco = mac_cisco.split(',') 
print(mac_cisco)
