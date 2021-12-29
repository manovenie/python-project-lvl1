#!/usr/bin/env python3

'''Brain-progression game'''

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Runs brain-progression game"""
    run_game(progression)


if __name__ == '__main__':
    main()
