from ipaddress import *

#Inputs
ip = ip_address(input('Ip: '))
mask = input('Mask(CIDR): ')
subnets = int(input('Subnets: '))

#Subnets list
n1 = list((ip_network(str(ip) + str(mask)).subnets(prefixlen_diff=subnets)))
print(n1[0]) #Get the first element of the 'n1' list


#Default gateway
atjaro = str(ip) + 1
print(atjaro)







