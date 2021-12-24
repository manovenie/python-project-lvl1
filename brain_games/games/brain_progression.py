#!/usr/bin/env python3

import random


GAME_INSTRUCTION = 'What number is missing in the progression?'
PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10
START_MIN = 1
START_MAX = 50
STEP_MIN = 2
STEP_MAX = 10


def get_question_and_answer():
    random_progression = generate_progression()
    nbr_to_be_hidden = random.choice(random_progression)
    hidden_index = random_progression.index(nbr_to_be_hidden)
    random_progression[hidden_index] = '..'
    random_progression = [str(item) for item in random_progression]
    answer = str(nbr_to_be_hidden)
    question = ' '.join(random_progression)
    return question, answer


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
