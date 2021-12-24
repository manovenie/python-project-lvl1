#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    random_int1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    random_int2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{} {}'.format(random_int1, random_int2)
    answer = find_gcd(random_int1, random_int2)
    return question, answer


def find_gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return str(a)
