"""
    Generator liczb naturalnych.
    Funkcje użytkowe.
"""

import random


def generate_number_between(min, max):
    """Losuje liczbę z przedziału <min, max>.

    :param min:
    :param max:
    :return:
    """
    number = int(random.random() * (max-min) + min)
    return number


def generate_until_drawn(number, min, max):
    """Losuje liczbę z przedzialu <min, max> tak dlugo az wylosuje liczbe number.

    :param number:
    :param min:
    :param max:
    :return: ilosc potrzebnych losowan do ostatecznego wylosowania liczby number.
    """
    loop_no = 1
    while generate_number_between(min, max) != number:
        loop_no += 1
    return loop_no
