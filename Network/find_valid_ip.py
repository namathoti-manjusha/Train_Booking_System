import socket
import re
valid_id=[]
#pattern=r"([0-9]{3}.+[0-9]{3}.+[0-9]{3}+[0-9]{3}.+)"
ip_address=["192.168.189.100","1.2.3.4","1020.209.009.2902.09",'001.209.234.098']
valid_ip1=[]
valid_ip2=[]
for ip in ip_address:
    r=re.findall(r'\.',ip)
    #print(r)
    if len(r)==3:
        valid_ip1.append(ip)
'''        
for ip in valid_ip1:
    try:
        socket.inet_aton(ip)
        valid_ip2.append(ip)
    except Exception as e:
        pass
'''
#print(valid_ip2)
def is_valid_ip_address(ip_address):
    ip_components = ip_address.split('.')
    if len(ip_components) != 4:
        return False
    for component in ip_components:
        try:
            if int(component) > 255:
                return False
        except ValueError:
            return False
        return True

ap_ad = list(filter(is_valid_ip_address, valid_ip1))
print(ap_ad)