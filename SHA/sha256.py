#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from hashlib import sha256 as sha_origin

"""  sha256 constants """
K = [
       0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
       0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
       0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
       0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
       0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
       0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
       0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
       0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]


def add_mod(*args, mod=32):
    """
    modulo 32 addition
    :param args: arguments to summarize
    :param mod: modulo
    :return: needed sum
    """
    res = 0
    for i in args:
        res += i % 2 ** mod
    return res % 2 ** mod


def rotr(x, n):
    """
    right rotation (cyclic shift)
    :param x: rotated value
    :param n: rotate length
    :return: rotated value
    """
    return (x >> n) | (x << 32 - n)


def padding(message):
    """
    Pre-processing (Padding):
    begin with the original message of length L bits
    append a single '1' bit
    append K '0' bits, where K is the minimum number >= 0 such that L + 1 + K + 64 is a multiple of 512
    append L as a 64-bit big-endian integer, making the total post-processed length a multiple of 512 bits
    :param message: bytes string
    :return: padded message
    """
    length = len(message) * 8
    k = (448 - length - 1) % 512
    add = '1' + '0' * k + bin(length)[2:].rjust(64, '0')
    res = message + bytes.fromhex(hex(int(add, 2))[2:])
    return res


def split(chunk):
    """
    create a 64-entry message schedule array w[0..63] of 32-bit words
    (The initial values in w[0..63] don't matter, so many implementations zero them here)
    copy chunk into first 16 words w[0..15] of the message schedule array
    :param chunk: 512-bit chunk
    :return: w
    """
    w = []
    for i in range(16):
        cur = chunk[4*i:4*i+4]
        cur = int(cur.hex(), 16)
        w.append(cur)
    w += [0] * 48
    return w


def sha256_hash(message: str):
    """
    sha 256 implementation
    :param message: string message
    :return: sha 256 hash
    """
    H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    message = message.encode()
    pad = padding(message)
    chunk_num = len(pad) // 512

    if chunk_num == 0:
        chunk_num = 1
    chunks = [pad[64*i:64*i+64] for i in range(chunk_num)]

    for chunk in chunks:
        w = split(chunk)
        for i in range(16, 64):
            s0 = rotr(w[i-15], 7) ^ rotr(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = rotr(w[i-2], 17) ^ rotr(w[i-2], 19) ^ (w[i-2] >> 10)
            w[i] = add_mod(w[i-16], s0, w[i-7], s1)

        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]
        f = H[5]
        g = H[6]
        h = H[7]

        for i in range(64):
            s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ (~ e & g)
            temp1 = add_mod(h, s1, ch, K[i], w[i])
            s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = add_mod(s0, maj)

            h = g
            g = f
            f = e
            e = add_mod(d + temp1)
            d = c
            c = b
            b = a
            a = add_mod(temp1, temp2)

        H[0] = add_mod(H[0], a)
        H[1] = add_mod(H[1], b)
        H[2] = add_mod(H[2], c)
        H[3] = add_mod(H[3], d)
        H[4] = add_mod(H[4], e)
        H[5] = add_mod(H[5], f)
        H[6] = add_mod(H[6], g)
        H[7] = add_mod(H[7], h)

    return b''.join(list(map(lambda x: bytes.fromhex(hex(x)[2:]), H))).hex()


if __name__ == '__main__':
    #  for test
    sha = sha_origin()

    t1 = ""
    sha.update(t1.encode())
    print(sha256_hash(t1))
    print(sha256_hash(t1) == sha.hexdigest())

    t2 = "hello world"
    sha.update(t2.encode())
    print(sha256_hash(t2))
    print(sha256_hash(t2) == sha.hexdigest())

