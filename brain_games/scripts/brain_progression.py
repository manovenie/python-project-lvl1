#!/usr/bin/env python3

'''Brain-progression game'''

from brain_games.game_process import start
from brain_games.games import brain_progression


def main():
    """Runs brain-progression game"""
    start(brain_progression)


if __name__ == '__main__':
    main()
