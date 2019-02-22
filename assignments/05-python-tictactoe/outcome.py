#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 2.20.2019
Purpose: Python program to write tictactoe program
"""
 # Tic Tac Toe
import os
import sys


def main():
    state = parse_args()
    check_state(state)
    check_winner(state)
def parse_args():
        args=sys.argv[1:]
        if len(args) != 1:
            print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
            exit(1)
        state=args[0]
        return state
def check_state( state ):
    if len(state) != 9:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        exit(1)
    for char in state:
        if char not in "XxOo.":
            #looping through eachs character in the state and making sure it is either an 'x' or 'o'
            print('State "{}" must be 9 characters of only ., X, O'.format(state))
            exit(1)
def check_winner(state):
    win_conditions=[(0,1,2),(3,4,5),(6,7,8),(2,4,6),(0,4,8),(0,3,6),(2,5,8),(1,4,7)]
    noWinner = True
    for win in win_conditions:
        win_str = state[win[0]]+state[win[1]]+state[win[2]]
        check = ( win_str ).upper()
        if check == 'XXX':
            print('X has won')
            noWinner = False
            break
        elif check == 'OOO':
            print('O has won')
            noWinner = False
            break
    if noWinner:
        print('No winner')

if __name__ == "__main__":
    main()

