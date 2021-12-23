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


def get_question_and_answer():
    random_int1, random_int2 = generate_int(), generate_int()
    operation = random.choice(list(operations.keys()))
    question = '{} {} {}'.format(random_int1, operation, random_int2)
    answer = find_true_answer(random_int1, random_int2, operation)
    return question, answer


def find_true_answer(int1, int2, operation):
    return str(operations[operation](int1, int2))
