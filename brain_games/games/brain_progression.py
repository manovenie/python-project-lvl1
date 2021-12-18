#!/usr/bin/env python

from brain_games.cli import get_user_answer
from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import COUNT_WINS_NEEDED
from brain_games.scripts.brain_games import print_lose_message
import prompt
import random

GAME_NAME = 'brain-progression'
PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10
START_MIN = 1
START_MAX = 50
STEP_MIN = 2
STEP_MAX = 10


def find_true_answer(int1, int2):
    biggest_divider = 1
    smallest_nbr = min(int1, int2)
    for counter in range(biggest_divider, smallest_nbr + 1):
        if int1 % counter == 0 and int2 % counter == 0:
            biggest_divider = counter
    return biggest_divider


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


def main():
    user_name = welcome_user(GAME_NAME)
    counter_correct_answers = 0
    while True:
        random_progression = generate_progression()
        nbr_to_be_missed = random.choice(random_progression)
        print('Question: ', end='')
        show_incomplete_progression(random_progression, nbr_to_be_missed)
        correct_answer = nbr_to_be_missed
        user_answer = get_user_answer(GAME_NAME)
        if correct_answer == user_answer:
            counter_correct_answers += 1
            if counter_correct_answers < COUNT_WINS_NEEDED:
                print('Correct!')
                continue
            else:
                print("Congratulations, {}!".format(user_name))
                break
        else:
            print_lose_message()


if __name__ == '__main__':
    main()
