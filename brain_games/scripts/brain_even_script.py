#!/usr/bin/env python

from brain_games.game_process import start
from brain_games.games import brain_even


def main():
    """Runs brain-even game"""
    start(brain_even)


if __name__ == '__main__':
    main()
