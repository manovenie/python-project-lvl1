#!/usr/bin/env python3

from operator import add, sub, mul
import random

GAME_INSTRUCTION = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 30
OPERATIONS = [['-', sub], ['+', add], ['*', mul]]


def generate_question_and_answer():
    number1 = random.randint(MIN_NUM, MAX_NUM)
    number2 = random.randint(MIN_NUM, MAX_NUM)
    math_symbol, operation = random.choice(OPERATIONS)
    answer = str(operation(number1, number2))
    question = '{} {} {}'.format(number1, math_symbol, number2)
    return question, answer
