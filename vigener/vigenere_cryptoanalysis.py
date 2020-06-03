#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from vigener.frequency_histogram import frequency_histogram
from vigener.ukrainian_letter_frequences import UKRAINIAN_LETTER_FREQUENCES
from vigener.vigenere_cipher import UA, encrypt, decrypt


def _index_of_coincidence(string):
    """
    find the index of coincidences
    :param string: input text
    :return: index
    """
    n = len(string)
    return sum([(string.count(i) * (string.count(i) - 1)) / (n * (n - 1)) for i in UA])


def _crypto_analysis(text):
    """
    part 2 - crypto analysis
    :param text: input text
    :return: xi2
    """
    freq = frequency_histogram(text)  # dictionary of frequencies
    return sum([(freq.get(alp, 0) - UKRAINIAN_LETTER_FREQUENCES.get(alp, 0)) ** 2 /
                UKRAINIAN_LETTER_FREQUENCES.get(alp, 0) for alp in UA])


def analyze_encrypted_text(text):
    """
    Frequency analysis of encrypted text.
    :param text: encrypted text
    :return: proposed decrypted text
    """
    # Solution
    index_ua = 5e-2
    coincidences_dict = {}  # dictionary {key length: index of coincidence}
    for k in range(1, 33):  # size of key
        cur = ''.join([text[i] for i in range(k, len(text), k)])  # string generation (each k-th char)
        coincidences_dict[k] = _index_of_coincidence(cur)

    # find the length of the key
    tmp_min = (coincidences_dict[1] - index_ua) ** 2
    key_len = 1
    for key, value in coincidences_dict.items():
        cur_min = (value - index_ua) ** 2
        if cur_min < tmp_min:
            tmp_min = cur_min
            key_len = key
    proposed_key = ""

    for start in range(key_len):
        cur = ''.join([text[i] for i in range(start, len(text), key_len)])
        cur_xi = _crypto_analysis(text)
        cur_alp = 'а'
        for alp in UA:
            tmp_text = decrypt(cur, alp)
            tmp_xi = _crypto_analysis(tmp_text)
            if tmp_xi < cur_xi:
                cur_xi = tmp_xi
                cur_alp = alp
        proposed_key += cur_alp
    print(proposed_key)
    proposed = decrypt(text, proposed_key)
    return proposed
