#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Answer "yes" if given ' \
                   'number is prime. Otherwise answer "no".'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    random_int = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{}'.format(random_int)
    answer = is_prime(random_int)
    return question, answer


def is_prime(nbr):
    if nbr > 1:
        for counter in range(2, (nbr // 2) + 1):
            if nbr % counter == 0:
                return 'no'
        else:
            return 'yes'
    else:
        return 'no'
