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
    out = []
    for x in data:
  out.append(chr(x/n))
    return ''.join(out)

ciphertext = encrypt("an amazingly secret and unbreakable cipher", "password")
print decryptDurr(ciphertext)
