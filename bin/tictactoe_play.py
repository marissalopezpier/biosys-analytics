#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 2.13.2019
Purpose: Python program to write tictactoe program
"""
 # Tic Tac Toe
import os
import sys


def main():
    args = parse_args()

    state = "........."#args.state
    #state = state.replace('.','-') # fix error in test code
    #check_state(state)
    #player = args.player
    #cell = args.cell

    starting_player = args.starting_player
    if starting_player:
        starting_player = starting_player.upper()
        check_player( starting_player )

    cur_player = starting_player.upper()
    # Game loop
    # 1) Game logic
    # 2) Check win condition
    # 3) Update states (get ready for next loop)
    while True:
        # Do logic
        print('Available moves (1-9):')
        print_board( state )
        new_state = get_player_move(cur_player,state)

        # Check win condition
        gameover = check_winner(new_state) #prints winner if there is a winner
        if gameover: # There is a winner so we are done
            break

        # Get ready for next loop
        state = new_state
        if cur_player=='X':
            cur_player='O'
        else:
            cur_player='X'
        print('')

#    if cell and player:
#        # Update the board
#        cell = int(cell)
#        #check_state( state )
#        state = update_state( player, cell, state )
#    elif (cell and not player) or (player and not cell):
#        print('Must provide both --player and --cell')
#        exit(1)
#
#    print_board( state )
##    print_board( "........." )
##    print(update_state('X',1,"123456789"))

def get_player_move( player, state ):
    move = int(input('Select player "{}" move (1-9 where available):'.format(player)))
    check_cell(move)
    new_state = update_state( player, move, state )
    check_state(new_state)
    return new_state

def print_board( state="........." ):
    template = """-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------"""
    st = []
    for i,char in enumerate(state):
        if char=='.':
            char = str(i+1)
        st.append(char)
    print(template.format(st[0],st[1],st[2],st[3],st[4],st[5],st[6],st[7],st[8]), end='')

def update_state( player, cell, state ):
    idx = cell-1
    existing_char = state[idx]
    if existing_char != '.':
        print('Cell {} already taken'.format(cell))
        exit(1)
#    new_state = state[:idx]+player+state[idx+1:]
    state_list = list(state)
    state_list[idx] = player
    new_state = ''.join(state_list)
    return new_state

def check_state( state ):
    if len(state) != 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state))
        exit(1)
    for char in state:
        if char not in "XxOo.":
            print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state))
            exit(1)

def check_player( player ):
    if len(player) != 1:
        print('Invalid player "{}", must be X or O'.format(player))
        exit(1)
    if player not in 'XxOo':
        print('Invalid player "{}", must be X or O'.format(player))
        exit(1)

def check_cell( cell ):
    if cell < 1 :
        print('Invalid cell "{}", must be 1-9'.format(cell))
        exit(1)
    elif cell > 9:
        print('Invalid cell "{}", must be 1-9'.format(cell))
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
        #print('No winner')
        if state.count('.')==0:
            print('Stalemate!!! Play again')
            gameover = True
        else:
            gameover = False
    else:
        gameover = True
    return gameover

def parse_args():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description="Tic-Tac-Toe board",formatter_class=ArgumentDefaultsHelpFormatter)
    #parser.add_argument( '-s', '--state', help='Board state', default=".........", type=str, metavar='str' )
    parser.add_argument( '-p', '--starting_player', help='Starting player', type=str, metavar='str', default='X' )
    #parser.add_argument( '-c', '--cell', help='Cell to apply -p', type=int, metavar='int' )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

