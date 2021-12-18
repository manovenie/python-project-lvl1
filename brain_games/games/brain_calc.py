#!/usr/bin/env python

from brain_games.cli import get_user_answer
from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import print_lose_message
from brain_games.scripts.brain_games import generate_int
from brain_games.scripts.brain_games import COUNT_WINS_NEEDED
import prompt
import random

GAME_NAME = 'brain-calc'

def find_true_answer(int1, int2, sign):
    if sign == '*':
        return int(int1 * int2)
    elif sign == '+':
        return int(int1 + int2)
    elif sign == '-':
        return int(int1 - int2)


def main():
    user_name = welcome_user(GAME_NAME)
    counter_correct_answers = 0
    while True:
        random_int1, random_int2 = generate_int(), generate_int()
        random_sign = random.choice(['-', '+', '*'])
        print('Question: {} {} {}'.format(random_int1, random_sign, random_int2))
        correct_answer = find_true_answer(random_int1, random_int2, random_sign)
        user_answer = get_user_answer(GAME_NAME)
        if correct_answer == user_answer:
            counter_correct_answers += 1
            if counter_correct_answers < COUNT_WINS_NEEDED:
                print('Correct!')
                continue
            else:
                print("Congratulations, {}!".format(user_name))
                break
        else:
            print_lose_message(user_answer, correct_answer, user_name)


if __name__ == '__main__':
    main()
