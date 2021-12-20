#!/usr/bin/env python3

from brain_games.game_process import generate_int

GAME_NAME = 'brain-gcd'
GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'


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
