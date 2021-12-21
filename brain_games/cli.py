#!/usr/bin/env python3

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    return user_name


def get_user_answer():
    """Prompt user for answer."""
    return prompt.string('Your answer: ')
