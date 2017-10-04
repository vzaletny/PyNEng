#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pprint import pprint


def parse_cdp_neighbors(cdp_str):
    """
    Задание 8.2

    Создать функцию parse_cdp_neighbors, которая обрабатывает
    вывод команды show cdp neighbors.

    Функция ожидает, как аргумент, вывод команды одной строкой.

    Функция должна возвращать словарь, который описывает соединения между устройствами.

    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors

    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0

    Функция должна вернуть такой словарь:

        {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
         ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

    Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

    Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

    Ограничение: Все задания надо выполнять используя только пройденные темы.
    """
    local_dev = ''
    local = []
    neighbors = []
    f_line = False
    cdp_list = cdp_str.split('\n')
    for line in cdp_list:
        if '>' in line:
            local_dev = line.split('>')[0]
        elif line.startswith('Device ID'):
            f_line = True
        elif f_line and line.split() and line.split()[0].isalnum():
            cdp_line = line.split()
            if cdp_line[1].isalpha():
                local.append((local_dev, cdp_line[1] + cdp_line[2]))
            else:
                local.append((local_dev, cdp_line[1]))
            if cdp_line[-1].replace('/', '').isdigit():
                neighbors.append((cdp_line[0], cdp_line[-2] + cdp_line[-1]))
            else:
                neighbors.append((cdp_line[0], cdp_line[-1]))
        else:
            f_line = False
    return dict(zip(local, neighbors))


def get_args():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(
        description='Create a configuration file for a switch')
    parser.add_argument('-i', '--ifile', required=True, action='store',
                        help='Incoming configuration file')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    with open(args.ifile, 'r', encoding='utf-8') as f:
        cdp_neighbors = parse_cdp_neighbors(f.read())
    pprint(cdp_neighbors)
    print('Parsing has completed')


# Start program
if __name__ == '__main__':
    main()
