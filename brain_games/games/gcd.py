#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    number1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    number2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{} {}'.format(number1, number2)
    answer = get_gcd(number1, number2)
    return question, answer


def get_gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return str(a)
