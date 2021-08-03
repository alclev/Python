import os
from cryptography.hazmat.primitives.ciphers import *
from cryptography.hazmat.primitives.ciphers.algorithms import *
from cryptography.hazmat.primitives.ciphers.modes import *

# STREAM CIPHERS
message = b'encrypt me plz'

key = os.urandom(32)
nonce = os.urandom(16)
cipher = Cipher(ChaCha20(key, nonce), mode=None)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()
print(ciphertext.hex())
print(message.hex())
