#! python3
#This program lets you play a simple 2-player game of Tic-Tac-Toe

import sys

board = {'tl':' ','tm':' ','tr':' ','ml':' '
,'mm':' ','mr':' ','bl':' ','bm':' ','br':' ',}

count = 0
turn = 'X'
plays = []

def win(check):
    '''This function checks to see if you have won the game'''

    check('tl','tm','tr')
    check('ml','mm','mr')
    check('bl','bm','br')
    check('tl','ml','bl')
    check('tm','mm','bm')
    check('tr','mr','br')
    check('tl','mm','br')
    check('bl','mm','tr')

def check(a,b,c):
    ''' This function checks to see if you have three in a row in
    one position
    '''
    con = [board[a],board[b],board[c]]
    content = [x.strip() for x in con]
    if board[a] == board[b] == board[c] and all(content):
        print('You have won!')
        sys.exit()


def tictac(board):
    '''This function prints the board'''
    count = 0
    print()
    for key, value in board.items():
        count += 1
        print(f'{value:^6}', end =' | ')
        if count %3 == 0:
            print()

for key, value in board.items():
    place = input('\nWhere do you want to play? ')
    while place not in board:
        print('That is not a valid move on the board.')
        place = input('\nWhere do you want to play? ')
    while place in plays:
        print('You can only play in a position one time.')
        place = input('\nWhere do you want to play? ')
    board[place] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    tictac(board)
    win(check)
    plays.append(place)