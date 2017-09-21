#!/usr/bin/env python
# -*- coding: utf-8 -*-


def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    conf_dict = {}
    for key, value in trunk.items():
        conf_list = [f'interface {key}']
        for cmd in trunk_template:
            if cmd.endswith('trunk allowed vlan'):
                conf_list.append(f'{cmd} {" ".join(str(vlan) for vlan in value)}')
            else:
                conf_list.append(cmd)
        conf_dict[key] = conf_list
    return conf_dict


trunk_dict = {'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]}

conf = generate_trunk_config(trunk_dict)
print('=' * 45)
for k, v in conf.items():
    print(k, '\n' + '-' * 45)
    for i in v:
        print(i)
    print('=' * 45)
