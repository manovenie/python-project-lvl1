#!/usr/bin/env python3

from brain_games.game_process import generate_int

GAME_NAME = 'brain-prime'
GAME_INSTRUCTION = 'Answer "yes" if given ' \
                   'number is prime. Otherwise answer "no".'


def find_true_answer(nbr):
    counter = 0
    for iter in range(1, nbr + 1):
        if nbr % iter == 0:
            counter += 1
    if counter == 2:
        return 'yes'
    else:
        return 'no'


def print_question_return_answer():
    random_int = generate_int()
    print('Question: {}'.format(random_int))
    correct_answer = find_true_answer(random_int)
    return correct_answer
