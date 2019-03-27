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
    card_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_scores = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = []

    # Generate the deck and shuffle
    for card in list(product(card_suits,card_values)):
        cards.append(card[0]+card[1])
    cards.sort()
    rnd.shuffle(cards)

    # Deal initial cards
    p1_hand = []
    dealer_hand = []

    # Draw first cards
    p1_hand.append( cards.pop() )
    dealer_hand.append( cards.pop() )

    # Draw second cards
    p1_hand.append( cards.pop() )
    dealer_hand.append( cards.pop() )

    if args.player_hits:
        p1_hand.append( cards.pop() )

    if args.dealer_hits:
        dealer_hand.append( cards.pop() )
    dealer_score = 0
    for card in dealer_hand:
        value = card[1:]
        index = card_values.index(value)
        score = card_scores[index]
        dealer_score += score
    print('D [{:>2}]: {}'.format(dealer_score,' '.join(dealer_hand)))
    player_score = 0
    for card in p1_hand:
        value = card[1:]
        index = card_values.index(value)
        score = card_scores[index]
        player_score += score
    print('P [{:>2}]: {}'.format(player_score,' '.join(p1_hand)))

    if player_score > 21:
        print('Player busts! You lose, loser!'.format(player_score))
        exit(0)
    if dealer_score > 21:
        print('Dealer busts.'.format(dealer_score))
        exit(0)
    if player_score == 21:
        print('Player wins. You probably cheated.'.format(player_score))
        exit(0)
    if dealer_score == 21:
        print('Dealer wins!'.format(dealer_score))
        exit(0)
    if dealer_score < 18:
        print('Dealer should hit.'.format(dealer_score))
    if player_score < 18:
        print('Player should hit.'.format(player_score))

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='"Black Jack" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='INT',
        default=None,
        type=int,
        )
    parser.add_argument(
    '-p', '--player_hits', help='A boolean player', action='store_true')
    parser.add_argument(
    '-d', '--dealer_hits', help='A boolean dealer', action='store_true')

    return parser.parse_args()

if __name__ == "__main__":
    main()

