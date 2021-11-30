#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import generate_int
import prompt


def find_true_answer(int1, int2):
    biggest_divider = 1
    smallest_nbr = min(int1, int2)
    for counter in range(biggest_divider, smallest_nbr + 1):
        if int1 % counter == 0 and int2 % counter == 0:
            biggest_divider = counter
    return biggest_divider


def main():
    game_name = 'brain-gcd'
    greet()
    user_name = welcome_user()
    print_game_instruction(game_name)
    counter_correct_answers = 0
    while True:
        random_int1 = generate_int()
        random_int2 = generate_int()
        print('Question: {} {}'.format(random_int1, random_int2))
        correct_answer = find_true_answer(random_int1, random_int2)
        user_answer = prompt.integer('Your answer: ')
        if correct_answer == user_answer:
            counter_correct_answers += 1
            if counter_correct_answers < 3:
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
