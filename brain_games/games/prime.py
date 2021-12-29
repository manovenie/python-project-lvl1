#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Answer "yes" if given ' \
                   'number is prime. Otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 50


def generate_question_and_answer():
    number = random.randint(MIN_NUM, MAX_NUM)
    question = '{}'.format(number)
    answer = is_prime(number)
    return question, answer


def is_prime(number):
    if (number < 2):
        return 'no'
    for counter in range(2, (number // 2) + 1):
        if number % counter == 0:
            return 'no'
    return 'yes'
