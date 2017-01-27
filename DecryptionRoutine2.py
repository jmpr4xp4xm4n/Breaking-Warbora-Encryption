import hashlib
from fractions import gcd

def encrypt(plain, password):
    password = hashlib.md5(password).hexdigest()
    encrypted = []
    for x in plain:
  x = ord(x)
  for y in password:
  y = ord(y)
  x = x * y
  encrypted.append(str(x))

    return '/'.join(encrypted)

def decrypt(encrypted, password):
    data = encrypted.split("/")
    password = hashlib.md5(password).hexdigest()
    out = []
    for x in data:
  x = int(x)
  for y in password:
    y = ord(y)
    x = x/y
  out.append(chr(x))
    return ''.join(out)

def decryptDurr(encrypted):
    data = [int(x) for x in encrypted.split("/")]
    n = reduce(lambda a, b: gcd(a, b), data)
    return ''.join([chr(x/n) for x in data])

ciphertext = encrypt("anamazinglysecretandunbreakablecipher", "password")
print decryptDurr(ciphertext)

# decryptDurr decrypts without a password. Just shortened it a bit
