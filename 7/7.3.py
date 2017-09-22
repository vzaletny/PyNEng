#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint


def get_int_vlan_map(conf_file):
    """
    Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
    и возвращает два объекта:
    * словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}

    * словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
    {'FastEthernet0/1':[10,20],
     'FastEthernet0/2':[11,30],
     'FastEthernet0/4':[17]}

    Функция ожидает в качестве аргумента имя конфигурационного файла.

    Проверить работу функции на примере файла config_sw1.txt

    Ограничение: Все задания надо выполнять используя только пройденные темы.

    :param conf_file:
    :return: 2 dictionary
    """
    try:
        with open(conf_file, 'r', encoding='utf-8') as f:
            last_interface = ''
            intf = ''
            trunk_dict = {}
            access_dict = {}
            for line in f:
                if line.startswith('interface'):
                    intf = line.split()[1]
                    if intf != last_interface:
                        last_interface = intf
                elif 'trunk allowed vlan' in line:
                    if intf == last_interface:
                        trunk_dict[intf] = [int(i) for i in (line.split()[-1].split(','))]
                elif 'access vlan' in line:
                    if intf == last_interface:
                        access_dict[intf] = int(line.split()[-1])
            return trunk_dict, access_dict
    except FileNotFoundError:
        print('File not found')
        return


ifile = './PyNEng/7/config_sw1.txt'
dict1, dict2 = get_int_vlan_map(ifile)
pprint(dict1)
pprint(dict2)
