#!/usr/bin/env python3

import random


GAME_NAME = 'brain-progression'
GAME_INSTRUCTION = 'What number is missing in the progression?'
PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10
START_MIN = 1
START_MAX = 50
STEP_MIN = 2
STEP_MAX = 10


def generate_progression():
    random_length = random.randint(PROGRESSION_LEN_MIN, PROGRESSION_LEN_MAX)
    random_start = random.randint(START_MIN, START_MAX)
    nbr_to_add = random_start
    random_step = random.randint(STEP_MIN, STEP_MAX)
    progression = []
    for counter in range(random_length):
        nbr_to_add += random_step
        progression.append(nbr_to_add)
    return progression


def show_incomplete_progression(progression, hidden_nbr):
    for number in progression:
        if number == hidden_nbr:
            print("..", end=' ')
        else:
            print(number, end=' ')
    print()


def print_question_return_answer():
    random_progression = generate_progression()
    nbr_to_be_missed = random.choice(random_progression)
    print('Question: ', end='')
    show_incomplete_progression(random_progression, nbr_to_be_missed)
    correct_answer = nbr_to_be_missed
    return str(correct_answer)
