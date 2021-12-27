#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Answer "yes" if given ' \
                   'number is prime. Otherwise answer "no".'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    number = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{}'.format(number)
    answer = is_prime(number)
    return question, answer


def is_prime(num):
    if num > 1:
        for counter in range(2, (num // 2) + 1):
            if num % counter == 0:
                return 'no'
        else:
            return 'yes'
    return 'no'
