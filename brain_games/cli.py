#!/usr/bin/env python3

import prompt


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    return user_name


def get_user_answer():
    """Prompt user for answer."""
    return prompt.string('Your answer: ')
