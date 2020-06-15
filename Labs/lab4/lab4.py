#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from RSA.miller_rabin import miller_rabin
from RSA.rsa import RSA
from RSA.rsa_oaep import encrypt, decrypt


def task_4_1():
    #  miller-rabin test
    print("output all primes from 0 to 100:")
    for i in range(100):
        if miller_rabin(i):
            print(i, end=" ")
    print()


def task_4_2():
    # rsa init
    rsa = RSA()
    print(f"p = {rsa._p}\nq = {rsa._q}\nexp = {rsa._exp}")


def task_4_3_and_4_4():
    # rsa encrypt/ decrypt
    message = 6414
    rsa = RSA()
    print(f"message = {message}")
    ct = rsa.encrypt(message)
    print(f"encrypted = {ct}")
    pt = rsa.decrypt(ct)
    print(f'decrypted = {pt}')
    print(f"equal : {pt == message}")


def task_4_5():
    # OAEP
    m = "hello world"
    print(f"message: {m}")
    ct = encrypt(m)
    print(f"encrypted: {ct}")
    pt = decrypt(ct)
    print(f"decrypted: {pt}")


if __name__ == '__main__':
    print("--- #4_1 ---")
    task_4_1()
    print("--- #4_2 ---")
    task_4_2()
    print("--- #4_3,4 ---")
    task_4_3_and_4_4()
    print("--- #4_5 ---")
    task_4_5()
