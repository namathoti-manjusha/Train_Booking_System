from netmiko import ConnectHandler
#Define the device information
device={

    'device_type':'linux',
    'ip':'192.168.149.128', #Replace with the IP addres of your device
    'username':'manjusha',
    'password':'Jyothiraj@1999'
}
#create a Netmiko SSH coonection to the device
connection=ConnectHandler(**device)
#send the "show processes cpu" command and capture the output
cpu_output=connection.send_command('cat /proc/cpuinfo')
#send the "show memory statistcs" command and capture the output
mem_output=connection.send_command('free -h')
#close the netmiko SSH connection
connection.disconnect()
#print the CPU and memory output
print('CPU Information:')
print(cpu_output)
print('\nMemory Information')
print(mem_output)
