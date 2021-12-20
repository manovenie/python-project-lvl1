#!/usr/bin/env python

from brain_games.game_process import start
from brain_games.games import brain_calc as game

def main():
    """list of commands after we run brain-games."""
    start(game)


if __name__ == '__main__':
    main()