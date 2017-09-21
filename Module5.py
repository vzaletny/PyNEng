#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    ip = input('Enter IP address: ').split('.')
    if len(ip) == 4:
        ip = tuple(int(i) for i in ip if i.isdigit() and 0 <= int(i) <= 255)
        if len(ip) == 4:
            break
    print('Incorrect IPv4 address')


if 0 < ip[0] < 224:
    print('Unicast')
elif 224 <= ip[0] < 240:
    print('Multicast')
elif len(tuple(i for i in ip if i == 0)) == 4:
    print('unassigned')
elif len(tuple(i for i in ip if i == 255)) == 4:
    print('local broadcast')
else:
    print('unused')

'''
print(all(i == 0 for i in ip))
print(all(i == 255 for i in ip))
'''

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = [i.replace(':', '.') for i in mac]
print(mac_cisco)

# Task 5.3
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access': {'0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'},
            'trunk': {'0/1': ['add', '10', '20'],
                      '0/2': ['only', '11', '30'],
                      '0/4': ['del', '17']
                      }
            }

for intf in fast_int['access']:
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, fast_int['access'][intf]))
        else:
            print(' {}'.format(command))
for intf in fast_int['trunk']:
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('trunk allowed vlan'):
            if fast_int['trunk'][intf][0] == 'add':
                print(' {} {}'.format(command, ' '.join(i for i in fast_int['trunk'][intf])))
            elif fast_int['trunk'][intf][0] == 'del':
                print(' {} {}'.format(command, ' '.join(i if i != 'del' else
                                                        i.replace('del', 'remove')
                                                        for i in fast_int['trunk'][intf])))
            elif fast_int['trunk'][intf][0] == 'only':
                print(' {} {}'.format(command, ' '.join(i for i in fast_int['trunk'][intf] if i != 'only')))
            else:
                pass
        else:
            print(' {}'.format(command))
