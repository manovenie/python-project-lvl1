#!/usr/bin/env python3

from brain_games.cli import get_user_name, get_user_answer


COUNT_WINS_NEEDED = 3


def game_loop(game):
    print('Welcome to the Brain Games!')
    user_name = get_user_name()
    print('Hello, {}!'.format(user_name))
    print(game.GAME_INSTRUCTION)
    for _ in range(COUNT_WINS_NEEDED):
        question, answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = get_user_answer()
        if user_answer == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. ".format(user_answer), end='')
            print("Correct answer was '{}'".format(answer))
            print("Let's try again, {}!".format(user_name))
            return
    print('Congratulations, {}!'.format(user_name))
