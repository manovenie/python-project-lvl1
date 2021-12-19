#!/usr/bin/env python

from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import game_process
from brain_games.scripts.brain_games import generate_int

GAME_NAME = 'brain-gcd'


def find_true_answer(int1, int2):
    biggest_divider = 1
    smallest_nbr = min(int1, int2)
    for counter in range(biggest_divider, smallest_nbr + 1):
        if int1 % counter == 0 and int2 % counter == 0:
            biggest_divider = counter
    return str(biggest_divider)


def print_question_return_answer():
    random_int1, random_int2 = generate_int(), generate_int()
    print('Question: {} {}'.format(random_int1, random_int2))
    correct_answer = find_true_answer(random_int1, random_int2)
    return correct_answer


def main():
    user_name = welcome_user()
    print_game_instruction(GAME_NAME)
    game_process(user_name, print_question_return_answer)


if __name__ == '__main__':
    main()
