#!/usr/bin/env python3

from brain_games.cli import welcome_user, get_user_name
import random


MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50
COUNT_WINS_NEEDED = 3


def generate_int():
    return random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)


def check_user_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def start(game=None):
    user_name = welcome_user()
    if game:
        print(game.GAME_INSTRUCTION)
        game_loop(user_name, game.print_question_return_answer)


def game_loop(user_name, print_question_return_answer):
    counter_correct_answers = 0
    while counter_correct_answers < COUNT_WINS_NEEDED:
        correct_answer = print_question_return_answer()
        user_answer = get_user_answer()
        if check_user_answer(user_answer, correct_answer):
            counter_correct_answers += 1
            print('Correct!')
        else:
            print_lose_message(user_answer, correct_answer, user_name)
            return
    print('Congratulations, {}!'.format(user_name))


def print_lose_message(user_answer, correct_answer, user_name):
    print("'{}' is wrong answer ;(. ".format(user_answer), end='')
    print("Correct answer was '{}'".format(correct_answer))
    print("Let's try again, {}!".format(user_name))
