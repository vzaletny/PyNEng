#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Comment for Module 3
"""
# Task 3.1
ospf_dict_keys = ('Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface')
ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route_fr = ospf_route.replace(',', ' ')
# ospf_route_fr = ospf_route_fr.replace('[', ' ')
# ospf_route_fr = ospf_route_fr.replace(']', ' ')
# ospf_route_fr = ospf_route.replace('O', 'OSPF')
ospf_route_fr = ospf_route_fr.split()

print(ospf_route_fr)
ospf_route_fr[0] = 'OSPF'
ospf_route_fr.remove('via')
ospf_route_fr[2] = ospf_route_fr[2][1:-1]
print(ospf_route_fr)
ospf_route_dict = dict(zip(ospf_dict_keys, ospf_route_fr))

print(ospf_route_dict)
for key, value in ospf_route_dict.items():
    print('{:25} {:20}'.format(key + ':', value))
print('-----------------------------------')
for key, value in ospf_route_dict.items():
    print('%-25s %-20s' % (key + ':', value))

# Task 3.2
MAC = "AAAA:BBBB:CCCC"
print(MAC.replace(':', "."))

# Task 3.3
CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = CONFIG.split()[-1].split(',')
print(vlans)

# Task 3.4
command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))
print(vlans1 & vlans2)

# Task 3.5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
uniq_vlans = list(set(VLANS))
uniq_vlans.sort()
print(uniq_vlans)

# Task 3.6
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast', 'Gigabit'))

# Task 3.7
MAC = "AAAA:BBBB:CCCC"
print('MAC')
print(' '.join('{:08b}'.format(int(mac, 16)) for mac in MAC.replace(':', '')))
# print(bin(int('0x' + MAC[:4] + MAC[5:9] + MAC[10:], 16)))

# Task 3.8
IP = '192.168.3.1'
# ip = IP.split('.')
# print('{a[0]:10}{a[1]:10}{a[2]:10}{a[3]:10}'.format(a=ip))
# print(type(ip[0]))

# ipn = list(map(int, ip))

# print(type(ipn[0]))

# print('{a[0]:10b}{a[1]:10b}{a[2]:10b}{a[3]:10b}'.format(a=ipn))
print(''.join('{:10}'.format(val) for val in IP.split('.')))
print(''.join('{:08b}  '.format(int(val)) for val in IP.split('.')))

# print('{:10}{:10}{:10}{:10}'.format(bin(ipn[0])[2:].zfill(8), bin(ipn[1])[2:].zfill(8),
#                                    bin(ipn[2])[2:].zfill(8), bin(ipn[3])[2:].zfill(8)))
# print(bin(ipn[2])[2:].zfill(8))

# Task 3.9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

print(len(num_list) - num_list[::-1].index(10) - 1)
