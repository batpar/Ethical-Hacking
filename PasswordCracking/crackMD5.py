#!/usr/bin/python

import hashlib
from termcolor import colored

hash = input("Enter the md5 hash of the password: ")
path = input ("Enter the path to the password file: ")
print(path)

# tryOpen opens the file specified in path variable, if unsuccessfull; prints erorr and quits the program.
def tryOpen(path):
    try:
        pass_file = open(path, 'r')
        return pass_file
    except:
        print('[-] Unable to open the file in path you have specified')
        quit()

pass_file = tryOpen(path)

for password in pass_file.readlines():
  # hashpass onverts the password from pass_file to md5 hash
    hashpass = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    if hash == hashpass:
        print(colored(f'[+]The correct password is: {password}', 'red'))
        quit()
    else:
        continue

print('[*]Unable to find the correct password in the file you have selected')