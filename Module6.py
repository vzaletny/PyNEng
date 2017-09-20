# from pydoc import _PlainTextDoc

import pandas as pd
from sys import argv
import json
import platform

if platform.system().lower() == 'windows':
    ifile = 'c:\Python\ospf.txt'
    ofile = 'c:\Python\config_sw1_cleared.txt'
else:
    ifile = '/home/dima/Documents/Python/ospf.txt'
    ofile = '/home/dima/Documents/Python/config_sw1_cleared.txt'

ospf_dict_keys = ('Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface')
ospf_route_list = []
with open(ifile, 'r') as f:
    for line in f:
        ospf_route = (line.rstrip().replace(',', ' ').split())
        ospf_route[0] = 'OSPF'
        ospf_route.remove('via')
        ospf_route[2] = ospf_route[2][1:-1]
        # print(line.rstrip())
        ospf_route_list.append(ospf_route)

# print(ospf_route_list)
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

# Task 6.3
ignore = ['duplex', 'alias', 'Current configuration']
path = ''.join(argv[1:])
print(path)
with open(path, 'r', encoding='utf-8') as f:
    # lines = [line for line in f.read().split('\n') if '!' not in line]
    for line in f:
        # print(line)
        if not line.startswith('!'):
            # line = line.strip()
            print('{}'.format(line.rstrip()))

print('6.2a')
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('!'):
            for i in ignore:
                if i in line:
                    break
            else:
                print('{}'.format(line.strip()))
print('new 6.2a')
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('!'):
            find_ignor = [i for i in ignore if i in line]
            if not find_ignor:
                print('{}'.format(line.strip()))

# 6.2b
with open(path, 'r', encoding='utf-8') as src, open(ofile, 'w', encoding='utf-8') as dst:
    for line in src:
        for i in ignore:
            if i in line:
                break
        else:
            dst.write(line)


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
