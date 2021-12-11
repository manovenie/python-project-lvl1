#!/usr/bin/env python

from brain_games.cli import welcome_user
import random

MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 100
COUNT_WINS_NEEDED = 3


def greet():
    """print welcome message."""
    print('Welcome to the Brain Games!')


def print_game_instruction(game):
    if game == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain-calc':
        print('What is the result of the expression?')
    elif game == 'brain-gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'brain-progression':
        print('What number is missing in the progression?')
    elif game == 'brain-prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_int():
    return random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT)


def main():
    """list of commands after we run brain-games."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
