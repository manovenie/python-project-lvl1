#!/usr/bin/env python3

'''Brain-prime game'''

from brain_games.game_process import game_loop
from brain_games.games import brain_prime


def main():
    """Runs brain-prime game"""
    game_loop(brain_prime)


if __name__ == '__main__':
    main()
