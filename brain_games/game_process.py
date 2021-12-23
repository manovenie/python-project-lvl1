#!/usr/bin/env python3

from brain_games.cli import welcome_user, get_user_answer
import random


MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 50
COUNT_WINS_NEEDED = 3


def game_loop(game):
    user_name = welcome_user()
    if game:
        print(game.GAME_INSTRUCTION)
        counter_correct_answers = 0
        while counter_correct_answers < COUNT_WINS_NEEDED:
            correct_answer = game.print_question_return_answer()
            user_answer = get_user_answer()
            if user_answer == correct_answer:
                counter_correct_answers += 1
                print('Correct!')
            else:
                print("""
                '{}' is wrong answer ;(. Correct answer was '{}'\n
                Let's try again, {}!
                """.format(user_answer, correct_answer, user_name))
                return
        print('Congratulations, {}!'.format(user_name))


def generate_int():
    return random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)
