#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    random_int1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    random_int2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{} {}'.format(random_int1, random_int2)
    answer = find_true_answer(random_int1, random_int2)
    return question, answer


def find_true_answer(int1, int2):
    biggest_divider = 1
    smallest_nbr = min(int1, int2)
    for counter in range(biggest_divider, smallest_nbr + 1):
        if int1 % counter == 0 and int2 % counter == 0:
            biggest_divider = counter
    return str(biggest_divider)
