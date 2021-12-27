#!/usr/bin/env python3

from operator import add, sub, mul
import random

GAME_INSTRUCTION = 'What is the result of the expression?'
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 30
OPERATIONS = [['-', sub], ['+', add], ['*', mul]]


def get_question_and_answer():
    number1 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    number2 = random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
    symbol, operation = random.choice(OPERATIONS)
    answer = str(operation(number1, number2))
    question = '{} {} {}'.format(number1, symbol, number2)
    return question, answer
