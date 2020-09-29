# Ethical-Hacking
My Journey into Ethical Hacking with Python.

1. portscanner - This allows a user to specify the host and ports they would like to scan. Uses threading for scanning multiple ports at once and
 optparse to provide the options to the code.

2. SSH - The sshbruteforce.py code allows you to login with bruteforce using a dictionary attack. This attack was carried out successfully on metasploitable.
The sshlogin.py using pexpect to automate the ssh login(useful for sysadmins.)

3. PasswordCracking - The hash.py file helps convert any arbitrary string value to a hash value of md5, sha1, sha256 and sha512.
The crackSHA1.py takes a sha1 hash and compares it to a 10000 common password file from github and provides a success message if the hash matches to any of the password in the list.
The crackMD5.py takes a md5 hash value and compares it to a password file (of your choice) and provides a success or failure message accordingly.
The crypt.py uses the password.txt file which is a mock of a database containing
username and password with a salt and dictionary.txt which is a password list and then use this information to find the correct password.