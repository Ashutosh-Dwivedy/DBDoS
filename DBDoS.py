from scapy.all import IP, send, Ether, ICMP

ip = input('Enter the target IP: ')
ip_spoof = input('Enter source IP to be used: ')
mac_spoof = input('Enter source MAC to be used: ')
pkts = int(input('Enter number of packet to be sent: '))

Ip = IP(src=ip_spoof, dst=ip)
Eth = Ether(src=mac_spoof)
pkt = Eth / Ip / ICMP()
print(f'Sending {pkts} packets to {ip}...')
send(pkt, count=pkts, verbose = 0)
print(f'Sent {pkts} packets to {ip} succesfully')