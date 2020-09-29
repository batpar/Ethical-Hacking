#!/usr/bin/python

import subprocess

def change_mac_addr(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"down"])
def main():

    interface = input("[*]Enter the Interface you'd like to change the MAC of:")
    mac = input("[*]Enter the mac address that you'd like to change to: ")

    before_change = subprocess.check_output(["ifconfig",interface])
    change_mac_addr(interface,mac)
    after_change = subprocess.check_output(["ifconfig",interface])

    if before_change == after_change:
        print(f'[-]Failed to change MAC address to: {mac} ')
    
    else:
        print(f'[+] The MAC address was successfully changed to: {mac}')

main()