#!/usr/bin/env python

from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import game_process
from brain_games.scripts.brain_games import generate_int
import operator

GAME_NAME = 'brain-calc'


operations = {
    '-': operator.sub,
    '+': operator.sum,
    '*': operator.mul,
}


def find_true_answer(int1, int2, operation):
    return str(operations[operation](int1, int2))


def print_question_return_answer():
    random_int1, random_int2 = generate_int(), generate_int()
    operation = operator.choice(list(operations.keys()))
    print('Question: {} {} {}'.format(random_int1, operations, random_int2))
    correct_answer = find_true_answer(random_int1, random_int2, operation)
    return correct_answer


def main():
    user_name = welcome_user()
    print_game_instruction(GAME_NAME)
    game_process(user_name, print_question_return_answer)


if __name__ == '__main__':
    main()
