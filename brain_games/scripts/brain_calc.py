#!/usr/bin/env python3

"""
 "Calc game"
"""

from brain_games.logic_game import run_game
from brain_games.games import code_calc


def main():
    run_game(code_calc)


if __name__ == '__main__':
    main()
