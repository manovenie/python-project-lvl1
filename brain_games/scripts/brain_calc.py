#!/usr/bin/env python3

'''Brain-calc game'''

from brain_games.game_process import game_loop
from brain_games.games import brain_calc


def main():
    """Run brain-calc game"""
    game_loop(brain_calc)


if __name__ == '__main__':
    main()
