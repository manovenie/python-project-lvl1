#!/usr/bin/env python3

from brain_games.game_process import generate_int

GAME_NAME = 'brain-even'
GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_int = generate_int()
    question = '{}'.format(random_int)
    answer = 'yes' if random_int % 2 == 0 else 'no'
    return question, answer
