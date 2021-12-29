#!/usr/bin/env python3

import random

GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 50


def generate_question_and_answer():
    number = random.randint(MIN_NUM, MAX_NUM)
    question = '{}'.format(number)
    answer = 'no' if number % 2 else 'yes'
    return question, answer
