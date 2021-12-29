#!/usr/bin/env python3

'''Brain-gcd game'''

from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Runs brain-gcd game"""
    run_game(gcd)


if __name__ == '__main__':
    main()
