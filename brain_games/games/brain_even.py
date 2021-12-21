#!/usr/bin/env python3

from brain_games.game_process import generate_int

GAME_NAME = 'brain-even'
GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def print_question_return_answer():
    random_int = generate_int()
    print('Question: {}'.format(random_int))
    correct_answer = 'yes' if random_int % 2 == 0 else 'no'
    return correct_answer
