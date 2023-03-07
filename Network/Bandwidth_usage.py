import psutil
import matplotlib.pyplot as plt
#define the network interface to monitor
interface='eth0'
#retrive the network usage satatics for the specified interface
net_io_counters=psutil.net_io_counters()
#interface_counters=net_io_counters.get(interface)
print(net_io_counters)
#calculate the amount of data received and sent in Mb
bytes_received=net_io_counters.bytes_recv / 1024 / 1024
bytes_sent=net_io_counters.bytes_sent /1024 / 1024
#Create a bar chart of the network usage
plt.bar(["Received","Sent"],[bytes_received,bytes_sent])
plt.ylabel("Bandwidth usage(MB)")
plt.title("Network usage for interface {}".format(interface))
plt.show()