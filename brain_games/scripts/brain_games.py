#!/usr/bin/env python

from brain_games.cli import welcome_user


def greet():
    """print welcome message."""
    print('Welcome to the Brain Games!')


def print_game_instruction(game):
    if game == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain-calc':
        print('What is the result of the expression?')

def generate_int():
	return random.randint(1, 100)


def main():
    """list of commands after we run brain-games."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
