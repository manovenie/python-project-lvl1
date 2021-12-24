#!/usr/bin/env python3

import operator
import random

GAME_INSTRUCTION = 'What is the result of the expression?'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 30

operations = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
}


def get_question_and_answer():
    random_int1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    random_int2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    operation = random.choice(list(operations.keys()))
    question = '{} {} {}'.format(random_int1, operation, random_int2)
    answer = str(operations[operation](int1, int2))
    return question, answer
