#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pydoc import _PlainTextDoc

import pandas as pd
from sys import argv
import json
import platform

if platform.system().lower() == 'windows':
    ifile = 'c:\Python\ospf.txt'
    ifile62 = 'c:\Python\config_sw1.txt'
    ifile63 = 'c:\Python\CAM_table.txt'
    ofile62 = 'c:\Python\config_sw1_cleared.txt'
    ofile62c = 'c:\Python\config_sw1_cleared62c.txt'
else:
    ifile = '/home/dima/Documents/Python/ospf.txt'
    ifile62 = '/home/dima/Documents/Python/config_sw1.txt'
    ifile63 = '/home/dima/Documents/Python/CAM_table.txt'
    ofile62 = '/home/dima/Documents/Python/config_sw1_cleared.txt'
    ofile62c = '/home/dima/Documents/Python/config_sw1_cleared62c.txt'

ospf_dict_keys = ('Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface')
ospf_route_list = []
with open(ifile, 'r') as f:
    for line in f:
        ospf_route = (line.rstrip().replace(',', ' ').split())
        ospf_route[0] = 'OSPF'
        ospf_route.remove('via')
        ospf_route[2] = ospf_route[2][1:-1]
        ospf_route_list.append(ospf_route)

pd.set_option('display.width', None)
table = pd.DataFrame(ospf_route_list)
table.transpose()
table.columns = ospf_dict_keys

print(table)
print(table.loc[[1, 5], ['Next-Hop', 'Prefix']])

for i in ospf_route_list:
    for key, value in zip(ospf_dict_keys, i):
        print('{:25} {:20}'.format(key + ':', value))
    print()

# ospf_route_dict = dict(zip(ospf_dict_keys, ospf_route_list))
#
# print(ospf_route_dict)
# for key, value in ospf_route_dict.items():
#     print('{:25} {:20}'.format(key + ':', value))
#
# Task 6.2
path = ''.join(argv[1])
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('!'):
            print('{}'.format(line.rstrip()))

# Task 6.2a
print('6.2a')
ignore = ['duplex', 'alias', 'Current configuration']
with open(ifile62, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('!'):
            for i in ignore:
                if i in line:
                    break
            else:
                print('{}'.format(line.strip()))

print('new 6.2a')
with open(ifile62, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('!'):
            find_ignore = [i for i in ignore if i in line]
            if not find_ignore:
                print('{}'.format(line.strip()))

# Task 6.2b
with open(ifile62, 'r', encoding='utf-8') as src, open(ofile62, 'w', encoding='utf-8') as dst:
    for line in src:
        find_ignore = [i for i in ignore if i in line]
        if not find_ignore:
            dst.write(line)

# Task 6.2c
try:
    with open(argv[1], 'r', encoding='utf-8') as src, open(argv[2], 'w', encoding='utf-8') as dst:
        for line in src:
            find_ignore = [i for i in ignore if i in line]
            if not find_ignore:
                dst.write(line)
except FileNotFoundError:
    print('File not found')

# Task 6.3
try:
    with open(ifile63, 'r', encoding='utf-8') as f:
        for line in f:
            find_line = [i for i in line.split() if i.isdigit()]
            if find_line:
                print('   '.join('{:4}'.format(i) for i in line.split() if i != 'DYNAMIC'))
except FileNotFoundError:
    print('File not found')

# Task 6.3a
try:
    with open(ifile63, 'r', encoding='utf-8') as f:
        lines = [line.split() for line in f.read().split('\n') if len(line.strip()) > 0 and line.split()[0].isdigit()]
        print(lines)
        lines = [line.remove('DYNAMIC') for line in lines]
        print(lines)
        lines.sort()
        for line in lines:
            # if line[0] == '100':
            if line:
                print(line)
except FileNotFoundError:
    print('File not found')

print()
# Test JSON
to_json = {'trunk': (
    'switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'),
    'access': (
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable')
}

# to_json = {'trunk': trunk_template, 'access': access_template}

'''
with open('sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json))
'''
with open('sw_templates.json', 'w', encoding='utf-8') as f:
    json.dump(to_json, f, sort_keys=True, indent=4, ensure_ascii=False)

with open('sw_templates.json') as f:
    print(f.read())
