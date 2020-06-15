#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from SHA.sha256 import sha256_hash


def hmac(key, message):
    b = 64
    key0 = key
    if len(key) > b:
        key0 = sha256_hash(key)
    key0 = key0.ljust(b, b'\x00')
    okeypad = bytes([k ^ 0x5c for k in key0])
    ikeypad = bytes([k ^ 0x36 for k in key0])
    return sha256_hash(okeypad + sha256_hash(ikeypad + message))


if __name__ == '__main__':
   key = b'skdjflwkdls'
   message = b'message'
   print(hmac(key, message))
