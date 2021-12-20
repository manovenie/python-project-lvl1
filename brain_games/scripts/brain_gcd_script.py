#!/usr/bin/env python

from brain_games.game_process import start
from brain_games.games import brain_gcd


def main():
    """Runs brain-gcd game"""
    start(brain_gcd)


if __name__ == '__main__':
    main()
