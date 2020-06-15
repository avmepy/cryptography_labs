#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from AES.FF import FiniteField
from AES.aes128 import AES


def task_2_1():
    # (a)
    # x^7 + x^5 + x^2
    a = b"010100100"
    print(f"a(x) = x^7 + x^5 + x^2\nbin: {a}, hex: {hex(int(a, 2))}, int: {int(a, 2)}\n")

    # (b)
    # x^7 + x^6 + x^2 + x + 1
    b = b"011000111"
    print(f"b(x) = x^7 + x^6 + x^2 + x + 1\nbin: {b}, hex: {hex(int(b, 2))}, int: {int(b, 2)}\n")


def task_2_2():
    # (a)
    # {10010111} * {01010111}
    r1 = FiniteField(int(b"10010111", 2)) * FiniteField(int(b"01010111", 2))
    print(f"10010111 * 01010111 = {bin(r1.num)}")

    # (b)
    # {d7} * {3c}
    r2 = FiniteField(0xd7) * FiniteField(0x3c)
    print(f"0xd7 * 0x3c = {r2}")

    # (c)
    # {200} * {100}
    r3 = FiniteField(200) * FiniteField(100)
    print(f"200 * 100 = {r3.num}")


def task_2_3():
    # (a)
    # {e5}
    s1 = AES.sbox[0x0e][5]
    print(f"(sbox): 0xe5 -> {hex(s1)}")

    # (b)
    # {f1}
    s2 = AES.sbox[0x0f][1]
    print(f"(sbox): 0xf1 -> {hex(s2)}")


def task_2_4():
    # (a)
    # {e5}
    s1 = AES.inv_sbox[0x0e][5]
    print(f"(inv sbox): 0xe5 -> {hex(s1)}")

    # (b)
    # {f1}
    s2 = AES.inv_sbox[0x0f][1]
    print(f"(inv sbox): 0xf1 -> {hex(s2)}")


def task_c2_1():
    plain_text = [
        [0x36, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x01, 0x07],
        [0xa8, 0x8f, 0xa2, 0x34]
    ]
    key = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]
    aes = AES(key)
    encrypted = aes.encrypt(plain_text)
    decrypted = aes.decrypt(encrypted)
    print(f"--- plain ---")
    for row in plain_text:
        print(row)

    print(f"--- encrypted ---")
    for row in encrypted:
        print(row)

    print(f"--- decrypted ---")
    for row in decrypted:
        print(row)

    print(f"\npt = dec(enc(pt): {plain_text == decrypted}")


def task_c2_2():
    print("полностью изменится криптотекст")


if __name__ == '__main__':
    print("--- #2.1 ---")
    task_2_1()
    print("--- #2.2 ---")
    task_2_2()
    print("--- #2.3 ---")
    task_2_3()
    print("--- #2.4 ---")
    task_2_4()
    print("--- #c2.1 ---")
    task_c2_1()
    print("--- #c2.2 ---")
    task_c2_2()


