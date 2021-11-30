#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.brain_games import print_game_instruction
from brain_games.scripts.brain_games import generate_int
import prompt
import random


def find_true_answer(int1, int2, sign):
    if sign == '*':
        return int(int1 * int2)
    elif sign == '+':
        return int(int1 + int2)
    elif sign == '-':
        return int(int1 - int2)


def main():
    game_name = 'brain-calc'
    greet()
    user_name = welcome_user()
    print_game_instruction(game_name)
    counter_correct_answers = 0
    while True:
        random_int1 = generate_int()
        random_int2 = generate_int()
        signs = ['-', '+', '*']
        sign1 = random.choice(signs)
        print('Question: {} {} {}'.format(random_int1, sign1, random_int2))
        correct_answer = find_true_answer(random_int1, random_int2, sign1)
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
            print("'{}' is wrong answer ;(. "
            "Correct answer was '{}'\nLet's try again, {}!"
            .format(user_answer, correct_answer, user_name))
            break


if __name__ == '__main__':
    main()
