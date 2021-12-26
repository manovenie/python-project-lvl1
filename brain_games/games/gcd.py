#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    int1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    int2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{} {}'.format(int1, int2)
    answer = get_gcd(int1, int2)
    return question, answer


def get_gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return str(a)
