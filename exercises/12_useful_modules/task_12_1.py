# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip_addresses(ip_list):
    access_ip = []
    not_access_ip = []
    for ip in ip_list:
        reply = subprocess.run(['ping', ip])
        if reply.returncode == 0:
            access_ip.append(ip)
        else:
            not_access_ip.append(ip)
    return access_ip, not_access_ip
print(ping_ip_addresses(["123.23.6", "google.com", "255.255.255.255", "1.1.1.1", "fgh.df.g.qw", "124.35.89.6"]))
