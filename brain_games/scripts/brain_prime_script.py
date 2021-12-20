#!/usr/bin/env python

from brain_games.game_process import start
from brain_games.games import brain_prime


def main():
    """Runs brain-prime game"""
    start(brain_prime)


if __name__ == '__main__':
    main()
