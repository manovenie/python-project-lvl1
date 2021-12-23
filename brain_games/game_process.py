#!/usr/bin/env python3

from brain_games.cli import welcome_user, get_user_answer
import random


MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50
COUNT_WINS_NEEDED = 3


def game_loop(game=None):
    user_name = welcome_user()
    if game:
        print(game.GAME_INSTRUCTION)
        counter_correct_answers = 0
        while counter_correct_answers < COUNT_WINS_NEEDED:
            question, answer = game.get_question_and_answer()
            print('Question: {}'.format(question))
            user_answer = get_user_answer()
            if user_answer == answer:
                counter_correct_answers += 1
                print('Correct!')
            else:
                print("'{}' is wrong answer ;(. ".format(user_answer), end='')
                print("Correct answer was '{}'".format(answer))
                print("Let's try again, {}!".format(user_name))
                return
        print('Congratulations, {}!'.format(user_name))


def generate_int():
    return random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
