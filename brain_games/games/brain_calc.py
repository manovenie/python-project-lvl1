#!/usr/bin/env python3

from operator import add, sub, mul
import random

GAME_INSTRUCTION = 'What is the result of the expression?'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 30
OPERATIONS = {
    '-': sub,
    '+': add,
    '*': mul,
}


def get_question_and_answer():
    int1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    int2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    symbol, operation = random.choice(list(OPERATIONS.items()))
    answer = str(operation(int1, int2))
    question = '{} {} {}'.format(int1, symbol, int2)
    return question, answer
