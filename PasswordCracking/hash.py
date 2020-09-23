#!/usr/bin/python

import hashlib

hashval = input("Enter the password you'd like to hash: ")

# md5 hash
hashobj1 = hashlib.md5()
hashobj1.update(hashval.encode())
print(hashobj1.hexdigest())

# sha1 hash
hashobj2 = hashlib.sha1()
hashobj2.update(hashval.encode())
print(hashobj2.hexdigest())

# sha256 hash
hashobj3 = hashlib.sha256()
hashobj3.update(hashval.encode())
print(hashobj3.hexdigest())

# sha512 hash
hashobj4 = hashlib.sha512()
hashobj4.update(hashval.encode())
print(hashobj4.hexdigest())


