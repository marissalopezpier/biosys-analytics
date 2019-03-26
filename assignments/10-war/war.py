#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 3 25 2019
Purpose: Python program for 99 bottles
"""
import os
import sys
import argparse
from itertools import product
import random

def main():
    args = get_args()
    seed = args.seed
    rnd = random.Random(seed)
    card_suits = ['♠','♣','♥','♦']
    card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards = []
    for card in list(product(card_suits,card_values)):
        cards.append(card[0]+card[1])
    cards.sort()
    rnd.shuffle(cards)

    P1_cards = []
    P2_cards = []
    while len(cards):
        P1_cards.append(cards.pop())
        P2_cards.append(cards.pop())

    #Game loop
    #P1_used = []
    #P2_used = []
    p1_score = 0
    p2_score = 0
    while True:
        p1card = P1_cards.pop(0)
        p2card = P2_cards.pop(0)
        p1value = card_values.index(p1card[1:])
        p2value = card_values.index(p2card[1:])
        if p1value>p2value:
            winner = 'P1'
            p1_score += 1
        elif p2value>p1value:
            winner = 'P2'
            p2_score += 1
        else:
            winner = 'WAR!'
        print('{:>3} {:>3} {}'.format(p1card,p2card,winner))
        if len(P1_cards)==0 or len(P2_cards)==0:
            break
    if p1_score > p2_score:
        winner ='Player 1 wins'
    elif p2_score > p1_score:
        winner = 'Player 2 wins'
    else:
        winner= 'DRAW'
    print('P1 {} P2 {}: {}'.format(p1_score,p2_score,winner))

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='INT',
        default=None,
        type=int,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

