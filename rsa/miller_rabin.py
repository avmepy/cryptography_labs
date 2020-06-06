#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

import random


def mod_pow(a: int, b: int, n: int) -> int:
    """
    modular exponentiation
    returns a ^ b (mod n)
    :param a: base (int)
    :param b: power (int)
    :param n: modulo (int)
    :return: a ^ b (mod n)
    """
    res = 1
    a = a % n
    while b > 0:
        if b & 1:  # if odd
            res = (res * a) % n
        #  here b must be odd
        b = b >> 1  # b = b / 2
        a = (a * a) % n
    return res


def _miller_rabin_helper(d: int, n: int) -> bool:
    """
    auxiliary function for miller-rabin primality test
    :param d: number such that d*2<sup>r</sup> = n-1  for some r >= 1
    :param n: number to test
    :return: True if probably prime / False if composite
    """
    # Pick a random number in [2..n-2]
    a = 2 + random.randint(1, n - 4)
    # Corner cases make sure that n > 4
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    # Keep squaring x while one
    # of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    # Return composite
    return False


def miller_rabin(n: int, k=12) -> bool:
    """
    miller rabin primality test
    :param n: number to check
    :param k: number of iteration
    :return: True if probably prime / False if composite
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    # Find r such that n =  2^d * r + 1 for some r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2
    # Iterate given number of 'k' times
    for _ in range(k):
        if not _miller_rabin_helper(d, n):
            return False
    return True


if __name__ == '__main__':
    # for test
    # output all prime numbers from 0 to 100
    for i in range(100):
        if miller_rabin(i):
            print(i, end=" ")
