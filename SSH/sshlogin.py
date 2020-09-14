import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

# send_command uses the child to run commands and print the output to stdoutput.
def send_command(child, command):
  child.sendline(command)
  child.expect(PROMPT)
  print(child.before)

# connect uses pexpect library to automate the ssh login and returns the ssh shell.
def connect(host, user, password):
  ssh_newkey = 'Are you sure you want to continue connecting'
  connectStr = 'ssh' + user + '@' + host
  child = pexpect.spawn(connectStr)
  ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword]')
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
    child.expect(PROMPT)
    return child

def main():
  host = input("Enter the host information: ")
  user = input("Enter your SSH username: ")
  password = input("Enter your SSH password: ")
  child = connect(host, user, password)
  send_command(child, 'ls')

main()
