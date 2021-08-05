#!/usr/bin/env python3

from cryptography.hazmat.primitives.hashes import *


message = b'hash me please'

digest = Hash(MD5())
digest.update(message)
print(digest.finalize().hex())
