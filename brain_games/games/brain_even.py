#!/usr/bin/env python

from brain_games.cli import get_user_answer
from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.brain_games import generate_int
from brain_games.scripts.brain_games import print_lose_message
from brain_games.scripts.brain_games import COUNT_WINS_NEEDED
import prompt


GAME_NAME = 'brain-even'


def find_true_answer(generated_int):
    generated_int = generated_int % 2 == 0
    if generated_int is True:
        return 'yes'
    else:
        return 'no'


def main():
    user_name = welcome_user(GAME_NAME)
    counter_correct_answers = 0
    while True:
        random_int = generate_int()
        print("Question: {}".format(random_int))
        correct_answer = find_true_answer(random_int)
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
