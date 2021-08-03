# BLOCK CIPHERS
import os
from cryptography.hazmat.primitives.ciphers import *
from cryptography.hazmat.primitives.ciphers.algorithms import *
from cryptography.hazmat.primitives.ciphers.modes import *

# AES block size is 32 bytes because AES is a 128-bit block size cipher.
message = b'encrypt me plz'
message = message + bytes(32 - len(message))

# Create the Cipher object and pass it the algorithm and the mode
# Algorithm is bound to the key.
# Mode is how the cipher is used. Typically bound with Initialization Vector (IV) or Nonce.
key = os.urandom(32) # AES = 128-bits... 32-bytes
iv = os.urandom(16)
cipher = Cipher(AES(key), CBC(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(message)
print(ciphertext.hex())
print(plaintext)
print()
