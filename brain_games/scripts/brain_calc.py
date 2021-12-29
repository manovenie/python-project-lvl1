#!/usr/bin/env python3

'''Brain-calc game'''

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Run brain-calc game"""
    run_game(calc)


if __name__ == '__main__':
    main()
