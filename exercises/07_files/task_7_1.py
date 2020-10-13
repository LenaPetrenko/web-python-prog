# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('/home/std/python-web/exercises/07_files/ospf.txt', 'r') as file_ospf:
    ospf = file_ospf.readlines()
    for lines in ospf:
        lines = lines.split()
        prefix = lines[1]
        ad_metric = lines[2].strip('[]')
        next_hop = lines[4].strip(',')
        last_update = lines[5].strip(',')
        outbound_interface = lines[6]
        ospf_route = """
        Prefix:               {}
        AD/Metric:            {}
        Next-Hop:             {}
        Last update:          {}
        Outbound Interface:   {}
        """
        print(ospf_route.format(prefix,ad_metric,next_hop,last_update,outbound_interface))

