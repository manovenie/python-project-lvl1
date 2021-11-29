#!/usr/bin/env python

from brain_games.cli import welcome_user


def greet():
    """print welcome message."""
    print('Welcome to the Brain Games!')


def main():
    """list of commands after we run brain-games."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
