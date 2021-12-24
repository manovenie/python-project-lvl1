#!/usr/bin/env python3

from brain_games.game_process import generate_int


GAME_INSTRUCTION = 'Answer "yes" if given ' \
                   'number is prime. Otherwise answer "no".'


def get_question_and_answer():
    random_int = generate_int()
    question = '{}'.format(random_int)
    answer = find_true_answer(random_int)
    return question, answer


def find_true_answer(nbr):
    counter = 0
    for iter in range(1, nbr + 1):
        if nbr % iter == 0:
            counter += 1
    if counter == 2:
        return 'yes'
    else:
        return 'no'
