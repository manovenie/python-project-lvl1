#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
import prompt
import random


def brain_even_welcome_msg():
	print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_int():
	return random.randint(1, 100)


def question_to_solve(random_int):
	print("Question: {}".format(random_int))


def true_answer(generated_int):
	generated_int = generated_int % 2 == 0
	if generated_int is True:
		return 'yes'
	else:
		return 'no'


def main():
	greet()
	user_name = welcome_user()
	brain_even_welcome_msg()
	counter_correct_answers = 0
	while True:
		random_int = generate_int()
		question_to_solve(random_int)
		correct_answer = true_answer(random_int)
		user_answer = prompt.string('Your answer: ')
		if correct_answer == user_answer:
			counter_correct_answers += 1
			if counter_correct_answers < 3:
				print('Correct!')
				continue
			else:
				print("Congratulations, {}!".format(user_name))
				break
		else:
			# check if continue needed with setting counter to 0
			print("'{}' is wrong answer ;(. "
					"Correct answer was '{}'\nLet's try again, {}!"
					.format(user_answer, correct_answer, user_name))
			break


if __name__ == '__main__':
	main()
