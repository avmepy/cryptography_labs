#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


class FiniteField:
    """
    FiniteField GF(2^8) implementation
    """

    modulo = 0x011b

    def __init__(self, decimal: int) -> None:
        """
        constructor
        :param decimal: int representation
        """
        self.num = decimal

    @staticmethod
    def add(a, b):
        """
        add method implementation
        :param a: first FiniteField's value
        :param b: second FiniteField's value
        :return: ff sum (a + b)
        """
        return FiniteField(a.num ^ b.num)

    @staticmethod
    def mul(a, b):
        """
        
        :param a:
        :param b:
        :return:
        """
        res = 0
        for i in range(8):
            if ((1 << i) & b.num) != 0:
                tmp = a.num
                for j in range(i):
                    tmp <<= 1
                    if tmp >= 256:
                        tmp ^= FiniteField.modulo
                res ^= tmp
        return FiniteField(res)

    @staticmethod
    def pow(base, exp):
        val = FiniteField(1)
        while exp > 0:
            val = FiniteField.mul(val, base)
            exp -= 1
        return val
