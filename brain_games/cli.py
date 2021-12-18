#!/usr/bin/env python

import prompt

def get_user_name():
    """Prompt user for his/her name."""
    return prompt.string('May I have your name? ')


def get_user_answer(game_name):
    """Prompt user for answer."""
    if game_name == 'brain-even' or game_name == 'brain-prime':
        return prompt.string('Your answer: ')
    else:
        return prompt.integer('Your answer: ')
