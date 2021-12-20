#!/usr/bin/env python

from brain_games.game_process import generate_int

GAME_NAME = 'brain-even'
GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def find_true_answer(generated_int):
    generated_int = generated_int % 2 == 0
    if generated_int is True:
        return 'yes'
    else:
        return 'no'


def print_question_return_answer():
    random_int = generate_int()
    print('Question: {}'.format(random_int))
    correct_answer = find_true_answer(random_int)
    return correct_answer
