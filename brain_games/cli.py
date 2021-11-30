#!/usr/bin/env python

import prompt


def welcome_user():
    """prompt user for their name"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
