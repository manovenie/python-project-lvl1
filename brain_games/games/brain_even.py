#!/usr/bin/env python

from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import game_process
from brain_games.scripts.brain_games import generate_int


GAME_NAME = 'brain-even'


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


def main():
    user_name = welcome_user()
    print_game_instruction(GAME_NAME)
    game_process(user_name, print_question_return_answer)


if __name__ == '__main__':
    main()
