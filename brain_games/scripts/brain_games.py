#!/usr/bin/env python

from brain_games.cli import get_user_name
import random

MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 100
COUNT_WINS_NEEDED = 3

def print_lose_message(user_answer, correct_answer, user_name):
    print("'{}' is wrong answer ;(. ".format(user_answer), end='')
    print("Correct answer was '{}'".format(correct_answer))
    print("Let's try again, {}!".format(user_name))
    break


def welcome_user(game_name):
    greet()
    user_name = get_user_name()
    print('Hello, {}!'.format(user_name))
    print_game_instruction(game_name)
    return user_name


def greet():
    """print welcome message."""
    print('Welcome to the Brain Games!')


def print_game_instruction(game_name):
    if game_name == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'brain-calc':
        print('What is the result of the expression?')
    elif game_name == 'brain-gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_name == 'brain-progression':
        print('What number is missing in the progression?')
    elif game == 'brain-prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_int():
    return random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)


def main():
    """list of commands after we run brain-games."""
    greet()

if __name__ == '__main__':
    main()
