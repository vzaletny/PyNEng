#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

ignore_list = ['duplex', 'alias', 'Current configuration']


def config_to_dict(conf_file):
    """
    Задача такая же, как и задании 7.4.
    Проверить работу функции надо на примере файла config_r1.txt

    Обратите внимание на конфигурационный файл.
    В нем есть разделы с большей вложенностью, например, разделы:
    * interface Ethernet0/3.100
    * router bgp 100

    Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
    При этом, не привязываясь к конкретным разделам.
    Она должна быть универсальной, и сработать, если это будут другие разделы.

    Если уровня вложенности два:
    * то команды верхнего уровня будут ключами словаря,
    * а команды подуровней - списками

    Если уровня вложенности три:
    * самый вложенный уровень должен быть списком,
    * а остальные - словарями.

    На примере interface Ethernet0/3.100:

    {'interface Ethernet0/3.100':{
                   'encapsulation dot1Q 100':[],
                   'xconnect 10.2.2.2 12100 encapsulation mpls':
                       ['backup peer 10.4.4.4 14100',
                        'backup delay 1 1']}}
    """
    try:
        with open(conf_file, 'r', encoding='utf-8') as f:
            conf_dict = {}
            cmd1 = ''
            cmd2 = ''
            for line in f:
                if line.strip() and line[1] != 1 or not line.startswith('!') and not ignore_command(line, ignore_list):
                    if not line.startswith(' '):
                        cmd1 = line.rstrip()
                        conf_dict[cmd1] = []
                    elif line.startswith('  '):
                        if type(conf_dict[cmd1]) is list:
                            conf_dict[cmd1] = {k: [] for k in conf_dict[cmd1]}
                        conf_dict[cmd1][cmd2].append(line.rstrip())
                    else:
                        cmd2 = line.rstrip()
                        conf_dict[cmd1].append(cmd2)
            return conf_dict
    except FileNotFoundError:
        print('File not found')
        return


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)


ifile = './PyNEng/7/config_r1.txt'
config_dict = config_to_dict(ifile)
pprint(config_dict, width=120)
