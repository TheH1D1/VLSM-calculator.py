from ipaddress import *

#Inputs
ip = ip_address(input('Ip: '))
mask = input('Mask(CIDR): ')
subnets = int(input('Subnets: '))
#pcs = int(input('PCS: '))

#Subnets list
n1 = list((ip_network(str(ip) + str(mask)).subnets(prefixlen_diff=subnets)))
print('Network address: ',n1[0]) #Get the first element of the 'n1' list
print('Subnets: ', n1)

#Usable hosts
hosts = list(ip_network(ip).hosts())
print('hosts: ',hosts)




#Default gateway
def default_gateway():
    atjaro = ip + int(1)
    print('Default gateway: ',atjaro)
default_gateway()




