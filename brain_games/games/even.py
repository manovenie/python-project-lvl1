#!/usr/bin/env python3

import random

GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50


def get_question_and_answer():
    number = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    question = '{}'.format(number)
    answer = 'no' if number % 2 else 'yes'
    return question, answer
