#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


trunk_dict = {'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]}
conf = generate_trunk_config(trunk_dict)
for line in conf:
    print(line)
