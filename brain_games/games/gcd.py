#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 50


def generate_question_and_answer():
    number1 = random.randint(MIN_NUM, MAX_NUM)
    number2 = random.randint(MIN_NUM, MAX_NUM)
    question = '{} {}'.format(number1, number2)
    answer = find_gcd(number1, number2)
    return question, answer


def find_gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return str(a)
