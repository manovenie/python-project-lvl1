#!/usr/bin/env python3

'''Brain-prime game'''

from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Runs brain-prime game"""
    run_game(prime)


if __name__ == '__main__':
    main()
