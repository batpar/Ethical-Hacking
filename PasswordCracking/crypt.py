#!/usr/bin/python
'''
This script uses the password.txt file which is a mock of a database containing
username and password with a salt and dictionary.txt which is a password list and then use this information to find the correct password.
'''

import crypt

# dictFile takes the cryptword from the main function and compares it with the password in the dictionary.txt file.
def dictFile(word):
  # salt is the first 2 characters in the word variable.
    salt = word[0:2]
    try:
        with open('dictionary.txt') as passList:
            print(passList)
            for line in passList.readlines():
                line = line.strip("\n")
                cryptedword = crypt.crypt(line, salt)

                if cryptedword == word:
                    print(f"[+] The password is {word}")
                    quit()
                else:
                    continue
            print("[-]The password does not seem to exist")
    except:
        print("[-]Unable to open the file you have specified")

    
def main():

    with open("password.txt") as passFile:
        for line in passFile.readlines():
            username = line.split(":")[0]
            cryptWord = line.split(":")[1].strip("\n")
            print(f'[+]Cracking password for {username}')
            print(cryptWord)
            dictFile(cryptWord)

main()