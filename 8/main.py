#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from my_func import generate_access_config, generate_trunk_config, get_int_vlan_map


def get_args():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(
        description='Create a configuration file for a switch')
    parser.add_argument('-i', '--ifile', required=True, action='store',
                        help='Incoming configuration file')
    parser.add_argument('-o', '--ofile', required=True, action='store',
                        help='Outgoing configuration file')
    args = parser.parse_args()
    return args


def write_to_file(conf_file, config):
    """
    Write interfaces configuration to file
    :param conf_file: Path to destination file
    :param config: Interfaces configuration list
    :return:
    """
    with open(conf_file, 'w', encoding='utf-8') as dst:
        dst.writelines(line + '\n' for line in config)


def main():
    args = get_args()
    trunk, access = get_int_vlan_map(args.ifile)
    write_to_file(args.ofile, generate_trunk_config(trunk))
    write_to_file(args.ofile, generate_access_config(access, psecurity=True))
    print('Interfaces configuration file has been done')


# Start program
if __name__ == '__main__':
    main()
