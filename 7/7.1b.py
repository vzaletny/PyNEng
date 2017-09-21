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

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    conf_dict = {}
    for key, value in access.items():
        conf_list = [f'interface {key}']
        for cmd in access_template:
            if cmd.endswith('access vlan'):
                conf_list.append(f'{cmd} {value}')
            else:
                conf_list.append(cmd)
        if psecurity:
            for cmd in port_security:
                conf_list.append(cmd)
        conf_dict[key] = conf_list
    return conf_dict


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

conf = (generate_access_config(access_dict, True))
print('=' * 45)
for k, v in conf.items():
    print(k, '\n' + '-' * 45)
    for i in v:
        print(i)
    print('=' * 45)
