#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov


UA = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
EN = "abcdefghijklmnopqrstuvwxyz"
alp = dict(enumerate(EN))  # dict {0: 'а', 1: 'б', 2: 'в', ...}
alp_rev = dict(map(lambda x: x[::-1], enumerate(EN)))  # dict {'а': 0, 'б': 1, 'в': 2, ...}


def _complement(word1, word2):
    """
    complements the cipher word to the length of the plain text
    :param word1: the cipher word
    :param word2: the plain text
    :return: complete cipher
    """
    res = word1 * int(len(word2) / len(word1))
    for i in range(len(word1)):
        if len(res) == len(word2):
            break
        res += word1[i]
    return res


def encrypt(text, key):
    """
    Encrypt text with Vigenere cipher
    :param text: plain text
    :param key: encryption key
    :return: crypto text
    """
    # Solution
    text = text.replace(' ', '')
    cipher = _complement(key, text)
    encrypted = ''.join([alp[(alp_rev[text[i]] + alp_rev[cipher[i]]) % 26] for i in range(len(text))])
    return encrypted


def decrypt(text, key):
    """
    Decrypt text with Vigenere cipher
    :param text: crypto text
    :param key: decryption key
    :return: plain text
    """
    # Solution
    text = text.replace(' ', '')
    cipher = _complement(key, text)
    decrypted = ''.join([alp[(alp_rev[text[i]] - alp_rev[cipher[i]]) % 26] for i in range(len(text))])
    return decrypted


def test():
    keyword = "x"
    text = "meetmelater"
    encrypted = encrypt(text=text, key=keyword)
    print(encrypted)
    decrypted = decrypt(text=encrypted, key=keyword)
    print(decrypted)


if __name__ == '__main__':
    test()
