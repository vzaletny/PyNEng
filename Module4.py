#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Comment for Module 4
"""
# from sys import argv

# Task 4.1
text = ['Network:', 'Mask:']
ip_address_mask = input('IP Address: ')

# TAsk 4.1b
# ip_address_mask = ''.join(argv[1:])
ip_list = ip_address_mask.split('/')

# print(ip_list)
print(text[0], '\n')
print(''.join('{:10}'.format(val) for val in ip_list[0].split('.')))
print(''.join('{:08b}  '.format(int(val)) for val in ip_list[0].split('.')))
print('\n' + text[1], '\n')
print(''.join('/{:10}'.format(ip_list[1])))
ones = '1' * int(ip_list[1])
zeros = '0' * (32 - int(ip_list[1]))
bit_mask = ones + zeros
print(''.join('{:<10}'.format(int(bit_mask[i:i + 8], 2)) for i in range(0, 24+1, 8)))
print(''.join('{:10}'.format(bit_mask[i:i + 8]) for i in range(0, 24+1, 8)))

print('\n' + text[0], '\n')

# Task 4.1a
net_address = [int(i) for i in ip_list[0].split('.')]
mask = list(int(bit_mask[i:i + 8], 2) for i in range(0, 24+1, 8))
# print(net_address, mask)
net = tuple(zip(net_address, mask))
print(''.join('{:<10}'.format(n & m) for n, m in net))
print(''.join('{:08b}  '.format(n & m) for n, m in net))
print('\n' + text[1], '\n')
print(''.join('/{:10}'.format(ip_list[1])))
print(''.join('{:<10}'.format(b) for b in mask))
print(''.join('{:08b}  '.format(b) for b in mask))

# Task 4.2
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device = input('Enter device name: ')
# prop = input('Enter parameter name: ')
# Task 4.2b

# if device in london_co:
desc = london_co.get(device, 'Device name not found')
param = ', '.join('{}'.format(par) for par in london_co[device])
prop = input('Enter parameter name ({}):'.format(param))
print(london_co.get(device))
print(london_co.get(device).get(prop.lower(), 'Parameter not found!!!'))

# Task 4.2a
# if prop in london_co[device]:
#     print(london_co[device][prop])
# else:
#     print('Parameter not found')
# print('\n')
# for key, val in desc.items():
#    print(key, val)
# else:
#    print('Device name not found')

# Task 4.3
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

template = {'access': access_template,
            'trunk': trunk_template
            }
question = {'access': 'Enter VLAN number:',
            'trunk': 'Enter allowed VLANs:'
            }
int_mode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number: ')
vlan = input('{}'.format(question.get(int_mode)))
print('\n' + '-' * 30)
print('interface {}'.format(interface))
get_value = template.get(int_mode, "Mode not found")
print('\n'.join(get_value).format(vlan))
