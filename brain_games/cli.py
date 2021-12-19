#!/usr/bin/env python

import prompt


def get_user_name():
    """Prompt user for his/her name."""
    return prompt.string('May I have your name? ')


def get_user_answer():
    """Prompt user for answer."""
    return prompt.string('Your answer: ')
