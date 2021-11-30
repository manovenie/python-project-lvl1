#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.brain_games import print_game_instruction
import prompt
import random


def find_true_answer(int1, int2):
    biggest_divider = 1
    smallest_nbr = min(int1, int2)
    for counter in range(biggest_divider, smallest_nbr + 1):
        if int1 % counter == 0 and int2 % counter == 0:
            biggest_divider = counter
    return biggest_divider


def generate_progression():
    random_length = random.randint(5, 10)
    random_start = random.randint(1, 50)
    nbr_to_add = random_start
    random_step = random.randint(2, 10)
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
    game_name = 'brain-progression'
    greet()
    user_name = welcome_user()
    print_game_instruction(game_name)
    counter_correct_answers = 0
    while True:
        random_progression = generate_progression()
        nbr_to_be_missed = random.choice(random_progression)
        print('Question: ', end='')
        show_incomplete_progression(random_progression, nbr_to_be_missed)
        correct_answer = nbr_to_be_missed
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
