#!/usr/bin/env python3

'''Brain-gcd game'''

from brain_games.game_process import game_loop
from brain_games.games import brain_gcd


def main():
    """Runs brain-gcd game"""
    game_loop(brain_gcd)


if __name__ == '__main__':
    main()
