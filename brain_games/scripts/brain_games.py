#!/usr/bin/env python3

'''Welcome part of the game'''

from brain_games.cli import get_user_name


def main():
    """No game: just prints welcome messages"""
    print('Welcome to the Brain Games!')
    user_name = get_user_name()
    print('Hello, {}!'.format(user_name))


if __name__ == '__main__':
    main()
