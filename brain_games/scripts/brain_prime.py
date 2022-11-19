#!/usr/bin/env python3

"""
 ""Prime game""
"""

from brain_games.logic_game import run_game
from brain_games.games import code_prime


def prime():
    run_game(code_prime)


if __name__ == '__main__':
    prime()
