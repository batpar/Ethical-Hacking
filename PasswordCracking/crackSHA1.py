from urllib.request import urlopen
import hashlib

hash = input("Enter  hash value of the password: ")
hashvalue = hash.lower()

# This is a 100000 list password file from github
passwordlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt').read(), 'utf-8')

for password in passwordlist.split('\n'):
  hash = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
  if hash == hashvalue:
    print(f'[+] The correct password is {password}')
    quit()
  
  else:
    continue

print("The password was not found on this list.")
  
  