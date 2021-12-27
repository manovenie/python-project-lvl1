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
    length = random.randint(PROGRESSION_LEN_MIN, PROGRESSION_LEN_MAX)
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = [start + counter * step for counter in range(length)]
    hidden_num_index = random.randint(0, length - 1)
    answer = str(progression[hidden_num_index])
    progression[hidden_num_index] = '..'
    question = ' '.join(str(item) for item in progression)
    return question, answer
