from scapy.all import *

# Filter packets based on IP address and Protocol
packets = sniff(filter="ip and udp", count=100)
# Save captured packets to a file
wrpcap('captured_packets.pcap', packets)
