#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint


def get_int_vlan_map(conf_file):
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
            return trunk_dict, access_dict
    except FileNotFoundError:
        print('File not found')
        return


ifile = './PyNEng/7/config_sw1.txt'
dict1, dict2 = get_int_vlan_map(ifile)
pprint(dict1)
pprint(dict2)
