#!/usr/bin/env python

from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import game_process
from brain_games.scripts.brain_games import generate_int

GAME_NAME = 'brain-prime'


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


def main():
    user_name = welcome_user()
    print_game_instruction(GAME_NAME)
    game_process(user_name)


if __name__ == '__main__':
    main()
