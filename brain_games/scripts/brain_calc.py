#!/usr/bin/env python3

from brain_games.game_process import start
from brain_games.games import brain_calc


def main():
    """Run brain-calc game"""
    start(brain_calc)


if __name__ == '__main__':
    main()
