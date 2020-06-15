#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from SHA.sha256 import sha256_hash
from hashlib import sha256 as sha_origin
from random import randint
from SHA.hmac import hmac


def task_3_1():
    # sha256 implementation
    message = "hello world"
    sha = sha_origin()

    t1 = ""
    sha.update(t1.encode())
    print(sha256_hash(t1))
    print(sha256_hash(t1) == sha.hexdigest())

    t2 = "hello world"
    sha.update(t2.encode())
    print(sha256_hash(t2))
    print(sha256_hash(t2) == sha.hexdigest())


def task_3_2():
    # secret key for aes 128 generation
    r = str(randint(1000, 101011))
    s = sha256_hash(r)
    l = s[:32]
    r = s[32:]
    tmp = [f"0x{r[i]}{l[i]}" for i in range(32)]
    key = [tmp[4*i:4*i+4] for i in range(4)]
    for row in key:
        print(row)


def task_3_3():
    # hmac
    key = b'test'
    message = b'message'
    print(hmac(key, message))


if __name__ == '__main__':
    print("--- #3_1 ---")
    task_3_1()
    print("--- #3_2 ---")
    task_3_2()
    print("--- #3_3 ---")
    task_3_3()
