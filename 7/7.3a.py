#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint


def get_int_vlan_map(conf_file):
    """
    Сделать копию скрипта задания 7.3.

    Дополнить скрипт:
        - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
                interface FastEthernet0/20
                    switchport mode access
                    duplex auto
          То есть, порт находится в VLAN 1

    В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
          Пример словаря: {'FastEthernet0/12':10,
                           'FastEthernet0/14':11,
                           'FastEthernet0/20':1 }

    Функция ожидает в качестве аргумента имя конфигурационного файла.

    Проверить работу функции на примере файла config_sw2.txt


    Ограничение: Все задания надо выполнять используя только пройденные темы.

    :param conf_file:
    :return:
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
                elif 'mode access' in line:
                    if intf == last_interface and not access_dict.get(intf):
                        access_dict[intf] = 1
            return trunk_dict, access_dict
    except FileNotFoundError:
        print('File not found')
        return


ifile = './PyNEng/7/config_sw2.txt'
dict1, dict2 = get_int_vlan_map(ifile)
pprint(dict1)
pprint(dict2)
