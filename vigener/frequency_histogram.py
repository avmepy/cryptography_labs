#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# author: Valentyn Kofanov

from matplotlib import pyplot as plt


def frequency_histogram(text, plot=False):
    """
    Plot frequency histogram
    :param text: input text
    :param plot: plot if True
    :return: dictionary character frequencies
    """
    freq = {}
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
            if char in freq.keys():
                freq[char] += 1
            else:
                freq[char] = 1
    for key in freq.keys():
        freq[key] /= count
    if plot:
        plt.bar(freq.keys(), freq.values())
        plt.show()
    return freq


def _test():
    text = "abababab34frdkjlfskababaaaaaaaa   \!@##^%&!@%^&#^%*("
    print(frequency_histogram(text, plot=True))


if __name__ == '__main__':
    _test()
