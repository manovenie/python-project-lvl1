#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import generate_int
from brain_games.scripts.brain_games import COUNT_WINS_NEEDED
import prompt


def find_true_answer(nbr):
    counter = 0
    for iter in range(1, nbr + 1):
        if nbr % iter == 0:
            counter += 1
    if counter == 2:
        return 'yes'
    else:
        return 'no'


def main():
    game_name = 'brain-prime'
    greet()
    user_name = welcome_user()
    print_game_instruction(game_name)
    counter_correct_answers = 0
    while True:
        random_int = generate_int()
        print('Question: {}'.format(random_int))
        correct_answer = find_true_answer(random_int)
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            counter_correct_answers += 1
            if counter_correct_answers < COUNT_WINS_NEEDED:
                print('Correct!')
                continue
            else:
                print("Congratulations, {}!".format(user_name))
                break
        else:
            print("'{}' is wrong answer ;(. ".format(user_answer), end='')
            print("Correct answer was '{}'".format(correct_answer))
            print("Let's try again, {}!".format(user_name))
            break


if __name__ == '__main__':
    main()
