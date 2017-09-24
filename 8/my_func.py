#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Set of functions for task 8.1
"""


def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    conf_list = []
    for key, value in access.items():
        conf_list.append(f'interface {key}')
        for cmd in access_template:
            if cmd.endswith('access vlan'):
                conf_list.append(f'{cmd} {value}')
            else:
                conf_list.append(cmd)
        if psecurity:
            for cmd in port_security:
                conf_list.append(cmd)
    return conf_list


def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    conf_list = []
    for key, value in trunk.items():
        conf_list.append(f'interface {key}')
        for cmd in trunk_template:
            if cmd.endswith('trunk allowed vlan'):
                conf_list.append(f'{cmd} {" ".join(str(vlan) for vlan in value)}')
            else:
                conf_list.append(cmd)
    return conf_list


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
    :return: Tuple of 2 dictionaries
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
