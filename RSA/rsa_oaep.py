#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from copy import deepcopy
from hashlib import sha256
from random import SystemRandom


n = 1024  # bits
k0 = 256


def str_to_bin(string):
    bits = bin(int.from_bytes(string.encode(), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def bin_to_str(binary):
    n = int(binary, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode() or '\0'


def encrypt(message):
    sha1 = sha256()
    sha2 = sha256()
    rand_binary = format(SystemRandom().getrandbits(k0), '0256b')
    m = str_to_bin(message)
    if len(m) <= (n - k0):
        k1 = n - k0 - len(m)
        zeros = m + ('0' * k1)
    sha1.update(rand_binary.encode())
    x = format(int(zeros, 2) ^ int(sha1.hexdigest(), 16), '0768b')
    sha2.update(x.encode())
    y = format(int(sha2.hexdigest(), 16) ^ int(rand_binary, 2), '0256b')
    return x + y


def decrypt(message):
    sha1 = sha256()
    sha2 = sha256()
    x = message[0:768]
    y = message[768:]

    sha2.update(x.encode())
    r = format(int(y, 2) ^ int(sha2.hexdigest(), 16), '0256b')

    sha1.update(r.encode())
    res = format(int(x, 2) ^ int(sha1.hexdigest(), 16), '0768b')

    return bin_to_str(res)


if __name__ == '__main__':
    m = "hello world"
    print(f"message: {m}")
    ct = encrypt(m)
    print(f"encrypted: {ct}")
    pt = decrypt(ct)