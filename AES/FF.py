#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


class FiniteField:
    """
    FiniteField GF(2^8) implementation
    """

    modulo = 0x011b  # x^8 + x^4 + x^3 + x + 1

    def __init__(self, decimal: int) -> None:
        """
        constructor
        :param decimal: int representation
        """
        self.num = decimal

    def __add__(self, other):
        """
        add method implementation
        :param a: first FiniteField's value
        :param b: second FiniteField's value
        :return: ff sum (a + b)
        """
        return FiniteField(self.num ^ other.num)

    def __mul__(self, other):
        """
        :param a:
        :param b:
        :return:
        """
        res = 0
        for i in range(8):
            if ((1 << i) & other.num) != 0:
                tmp = self.num
                for j in range(i):
                    tmp <<= 1
                    if tmp >= 256:
                        tmp ^= FiniteField.modulo
                res ^= tmp
        return FiniteField(res)

    def __pow__(self, power):
        """
        pow raising implementation
        :param power:
        :return:
        """
        val = FiniteField(1)
        power = power % 255  # for negative power
        while power > 0:
            val = val * self
            power -= 1
        return val

    def __str__(self):
        return str(hex(self.num))

    def __repr__(self):
        return str(hex(self.num))


if __name__ == '__main__':
    # for test
    a = FiniteField(5)
    b = FiniteField(98)
    print(a + b)
    print(a * b)
    print(a ** 3)
    print(a ** 254)
    print(a ** (-1))
