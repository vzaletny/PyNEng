#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    for key in access.keys():
        # conf_list.append('{} {}'.format('interface', key))
        conf_list.append(f'interface {key}')
        for cmd in access_template:
            if cmd.endswith('access vlan'):
                # conf_list.append('{} {}'.format(cmd, access.get(key)))
                conf_list.append(f'{cmd} {access.get(key)}')
            else:
                conf_list.append(cmd)
        if psecurity:
            for cmd in port_security:
                conf_list.append(cmd)
    return conf_list


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

conf = (generate_access_config(access_dict, True))
for line in conf:
    print(line)
