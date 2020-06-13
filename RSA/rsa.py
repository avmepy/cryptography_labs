#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

import numpy as np
from random import randint
from RSA.miller_rabin import miller_rabin


def get_rand_prime():
    """
    finding random prime number
    :return:
    """
    x = randint(1 << 1024 - 1, 1 << 1024)
    if x & 1 == 0:
        x += 1
    while not miller_rabin(x):
        x += 2
    return x


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def mod_inv(a, b):
    """ return x such that (x * a) % b == 1 """
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


class RSA:
    """
    RSA implementation
    """

    def __init__(self, p=None, q=None, exp=None):
        """
        constructor
        :param p: prime int
        :param q: prime int
        :param exp: secret exponent
        """

        if p is None and q is None:
            self._p, self._q = self._get_primes()
        else:
            self._p = p
            self._q = q

        if exp is None:
            self._exp = 3
        else:
            self._exp = exp

        self._N = self._p * self._q  # get N = p*q
        self._tot = (self._p - 1) * (self._q - 1)   # Euler function
        self._d = mod_inv(self._exp, self._tot)

    def _get_primes(self):
        """
        get different prime numbers
        :return: (p1, p2)
        """
        p = get_rand_prime()
        q = get_rand_prime()
        while q == p:
            q = get_rand_prime
        return p, q

    def encrypt(self, message):
        """
        encryption implementation
        :param message: int number
        :return: crypto text
        """
        return pow(message, self._exp, self._N)

    def decrypt(self, message):
        """
        decryption implementation
        :param message: int number
        :return: plain text
        """
        return pow(message, self._d, self._N)


if __name__ == '__main__':
    # for test
    rsa = RSA(p=11, q=23)
    message = 133
    ct = rsa.encrypt(message)
    print(ct)
    pt = rsa.encrypt(ct)
    print(pt)

