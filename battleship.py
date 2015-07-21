# script for playing battleship
from random import randint

##
## Create the boards as global variables
##
board = []
res_board = []

for x in range(10):
    board.append(["O"] * 10)
    res_board.append(["O"] * 10)

def print_board(board):
    print ""
    for row in board:
        print " ".join(row)

def clear_board():
    global board
    global res_board
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            board[i][j] = "O"
            res_board[i][j] = "O"

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
        return ship_place(length, pos)

def hit_ship(guess_pos, hit_count, ship_name, ship_len, ship_count):

    print "HIT! You hit the " + ship_name
    board[guess_pos[0]][guess_pos[1]] = 'H'
    hit_count += 1
    ship_count += 1

    if ship_count == ship_len:
        print 'The %s has sunk' % (ship_name)
    else:
        print 'There are %s hits required to sink the %s' % (ship_len - ship_count, ship_name)

    return hit_count, ship_count

def is_good_guess(guess):
    if guess[0] > len(board) or guess[0] < 0:
        print 'That position is outside the board'
        return False
    elif guess[1] > len(board) or guess[1] < 0:
        print 'That position is outside the board'
        return False
    elif board[guess[0]][guess[1]] == 'H' or board[guess[0]][guess[1]] == 'M':
        print 'You guessed that position already!'
        return False
    else:
        return True

def play_battleship():

    recon_ship   = ship_place(2, get_pos_delim())
    dest_ship    = ship_place(3, get_pos_delim())
    submarine    = ship_place(3, get_pos_delim())
    battle_ship  = ship_place(4, get_pos_delim())
    carrier_ship = ship_place(5, get_pos_delim())

    hit_count = 0
    recon_count, dest_count, sub_count, batt_count, carr_count = 0, 0, 0, 0, 0
    print_board(res_board)
    while hit_count < (len(recon_ship) + len(dest_ship) + len(submarine) + len(battle_ship) + len(carrier_ship)):
        guess_pos = [int(raw_input("Guess Row: ")), int(raw_input("Guess Column: "))]
        if is_good_guess(guess_pos):
            if guess_pos in recon_ship:
                hit_count, recon_count = hit_ship(guess_pos, hit_count, 'reconnasance ship', len(recon_ship),   recon_count)
            elif guess_pos in dest_ship:
                hit_count, dest_count  = hit_ship(guess_pos, hit_count, 'destroyer ship',    len(dest_ship),    dest_count)
            elif guess_pos in submarine:
                hit_count, sub_count   = hit_ship(guess_pos, hit_count, 'submarine',         len(submarin),     sub_count)
            elif guess_pos in battle_ship:
                hit_count, batt_count  = hit_ship(guess_pos, hit_count, 'battle ship',       len(battle_ship),  batt_count)
            elif guess_pos in carrier_ship:
                hit_count, carr_count  = hit_ship(guess_pos, hit_count, 'carrier',           len(carrier_ship), carr_count)
            else:
                print "MISS!"
                board[guess_pos[0]][guess_pos[1]] = 'M'
        else:
            continue
        print_board(board)
    else:
        print "Congratulations! You sunk the fleet!"

def play_again(char):
    l_yes = ['y', 'Y', 'yes', 'Yes', 'YES']
    l_no  = ['n', 'N', 'no', 'No', 'NO']
    while char not in l_yes and char not in l_no:
        print "I'm sorry, that is not a vaild option."
        char = raw_input("Would you like to play again? (y/n) ")
    else:
        if char in l_yes:
            return True
        else:
            print "Thanks for playing!"
            return False


def main():

    '''
    Plays the game of battleship
    '''

    play_game = True
    while play_game == True:
        print "Let's play Battleship!"
        print_board(board)
        play_battleship()
        play_game = play_again(raw_input("Would you like to play again? (y/n) ")) 
        clear_board()

if __name__ == '__main__':
    main()

