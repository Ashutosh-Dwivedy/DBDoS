from scapy.all import IP, send, Ether, ICMP, TCP, UDP

ip = input('Enter the target IP: ')
ip_spoof = input('Enter source IP to be used: ')
mac_spoof = input('Enter source MAC to be used: ')
pkts = int(input('Enter number of packet to be sent: '))
protocol = input('Enter protocol to be used (ICMP/TCP/UDP): ').upper()

Ip = IP(src=ip_spoof, dst=ip)
Eth = Ether(src=mac_spoof)

if protocol == 'ICMP':
    pkt = Eth / Ip / ICMP()
    print(f'Sending {pkts} packets to {ip}...')
    send(pkt, count=pkts, verbose = 0)
    print(f'Sent {pkts} packets to {ip} succesfully')
elif protocol == 'TCP':
    sp = int(input('Enter source port to be used: '))
    dp = int(input('Enter destination port to be used: '))
    tcp = TCP(sport=sp, dport=dp )
    pkt = Eth / Ip / tcp
    print(f'Sending {pkts} packets to {ip}...')
    send(pkt, count=pkts, verbose = 0)
    print(f'Sent {pkts} packets to {ip} succesfully')
elif protocol == 'UDP':
    sp = int(input('Enter source port to be used: '))
    dp = int(input('Enter destination port to be used: '))
    udp = UDP(sport=sp, dport=dp )
    pkt = Eth / Ip / udp
    print(f'Sending {pkts} packets to {ip}...')
    send(pkt, count=pkts, verbose = 0)
    print(f'Sent {pkts} packets to {ip} succesfully')