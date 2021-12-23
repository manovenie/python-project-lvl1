#!/usr/bin/env python3

from brain_games.game_process import generate_int
import operator
import random

GAME_NAME = 'brain-calc'
GAME_INSTRUCTION = 'What is the result of the expression?'

operations = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
}


def print_question_return_answer():
    random_int1, random_int2 = generate_int(), generate_int()
    operation = random.choice(list(operations.keys()))
    print('Question: {} {} {}'.format(random_int1, operation, random_int2))
    correct_answer = find_true_answer(random_int1, random_int2, operation)
    return correct_answer


def find_true_answer(int1, int2, operation):
    return str(operations[operation](int1, int2))
