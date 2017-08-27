tmp = [
    'Protocol',
    'Prefix',
    'AD/Metric',
    'Next-Hop',
    'Last update',
    'Outbound Interface']

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

# ospf_list = [x for x in ospf_route.replace(',', '').split()]
ospf_list = ospf_route.replace(',', '').split()
ospf_list[0] = 'OSPF'
ospf_list.remove('via')
ospf_list[2] = ospf_list[2][1:-1]

print(''.join('{:25}{}\n'.format(t + ':', o) for t, o in zip(tmp, ospf_list)))
# for t, o in zip(tmp, ospf_list):
#    print('{:25}{}'.format(t + ':', o))

P = '192.168.3.1'
L = P.split('.')

print(''.join('{:10}'.format(x) for x in P.split('.')))
print(''.join('{:08b}  '.format(int(x)) for x in L))
