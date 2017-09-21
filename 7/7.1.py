#!/usr/bin/env python
# -*- coding: utf-8 -*-


def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    conf_list = []
    for key in access.keys():
        conf_list.append('{} {}'.format('interface', key))
        for command in access_template:
            if command.endswith('access vlan'):
                conf_list.append('{} {}'.format(command, access.get(key)))
            else:
                conf_list.append(command)
    return conf_list


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

conf = (generate_access_config(access_dict))
for line in conf:
    print(line)
