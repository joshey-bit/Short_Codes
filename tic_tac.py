theBoard = {'top-L' : '', 'top-M' : '','top-R' : '',
'mid-L' : '','mid-M' : '','mid-R' : '',
'low-L' : '','low-M' : '','low-R' : ''}

def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printboard(theBoard)
    print('the turn for '+turn+' . move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printboard(theBoard)
