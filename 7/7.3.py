#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_int_vlan_map(conf_file):
    try:
        with open(conf_file, 'r', encoding='utf-8') as f:
            last_interface = ''
            for line in f:
                if line.startswith('interface'):
                    int_list = line.split()
                    last_interface = int_list[0]
                    conf_dict = {int_list[1]}
                elif line.endswith('mode access'):
                    pass
                elif line.endswith('mode trunk'):
                    pass
                elif line.endswith('vlan'):
                    pass

    except FileNotFoundError:
        print('File not found')
        return


ifile = 'config_sw1.txt'
get_int_vlan_map(ifile)

