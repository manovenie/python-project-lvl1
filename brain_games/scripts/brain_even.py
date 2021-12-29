#!/usr/bin/env python3

'''Brain-even game'''

from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Runs brain-even game"""
    run_game(even)


if __name__ == '__main__':
    main()
