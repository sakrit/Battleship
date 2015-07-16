# script for playing battleship
from random import randint

board = []
res_board = []

for x in range(10):
    board.append(["O"] * 10)
    res_board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def get_pos_delim():
    if randint(0, 1) == 0:
        return 'd'
    else:
        return 'r'

def check_ship_place(ship):
    for i in ship:
        if res_board[i[0]][i[1]] == 'S':
            return False
        else:
            continue

    return True

def place_ship(ship):
    for i in ship:
        res_board[i[0]][i[1]] = 'S'

    return ship

def ship_place(length, pos):
    iVal_x = randint(0, len(board) - 1)
    iVal_y = randint(0, len(board) - 1)
    ll_ = [[iVal_x, iVal_y]]
    if pos == 'd':
        if (iVal_y + length - 1) > len(board) - 1 and (iVal_x + length - 1 <= len(board) - 1):
            for i in xrange(1, length):
                ll_.append([iVal_x + i, iVal_y])
        elif (iVal_y + length - 1) > len(board) - 1 and (iVal_x + length - 1 > len(board) - 1):
            for i in xrange(1, length):
                ll_.append([iVal_x, iVal_y - i])
        else:
            for i in xrange(1, length):
                ll_.append([iVal_x, iVal_y + i])
    else:
        if (iVal_x + length - 1) > len(board) - 1 and (iVal_y + length - 1 <= len(board) - 1):
            for i in xrange(1, length):
                ll_.append([iVal_x, iVal_y + i])
        elif (iVal_x + length - 1) > len(board) - 1 and (iVal_y + length - 1 > len(board) - 1):
            for i in xrange(1, length):
                ll_.append([iVal_x - i, iVal_y])
        else:
            for i in xrange(1, length):
                ll_.append([iVal_x + i, iVal_y])

    if check_ship_place(ll_):
        place_ship(ll_)
        return ll_
    else:
        ship_place(length, pos)

recon_ship   = ship_place(2, get_pos_delim())
dest_ship    = ship_place(3, get_pos_delim())
submarine    = ship_place(3, get_pos_delim())
battle_ship  = ship_place(4, get_pos_delim())
carrier_ship = ship_place(6, get_pos_delim())
print ''
print_board(res_board)
#def random_row(board):
#    return randint(0, len(board) - 1)
#
#def random_col(board):
#    return randint(0, len(board[0]) - 1)
#
#ship_row = random_row(board)
#ship_col = random_col(board)
#
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
#for turn in range(4):
#    guess_row = int(raw_input("Guess Row:"))
#    guess_col = int(raw_input("Guess Col:"))
#
#    if guess_row == ship_row and guess_col == ship_col:
#        print "Congratulations! You sunk my battleship!"
#        break
#    else:
#        if (guess_row < 0 or guess_row > len(board)) or (guess_col < 0 or guess_col > len(board)):
#            print "Oops, that's not even in the ocean."
#        elif(board[guess_row][guess_col] == "X"):
#            print "You guessed that one already."
#        else:
#            print "You missed my battleship!"
#            board[guess_row][guess_col] = "X"
#    print "Turn", turn + 1
#    print_board(board)
#    
#    if turn == 3:
#        print "Game Over"
