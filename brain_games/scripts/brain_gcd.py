#!/usr/bin/env python3

"""
 ""*Gcd game*""
"""

from brain_games.logic_game import run_game
from brain_games.games import code_gcd


def gcd():
    run_game(code_gcd)


if __name__ == '__main__':
    gcd()
