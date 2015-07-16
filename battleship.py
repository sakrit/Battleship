# script for playing battleship
from random import randint

board = []
res_board = []

for x in range(10):
    board.append(["O"] * 10)
    res_board.append(["O"] * 10)

def print_board(board):
    print ""
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
        return ship_place(length, pos)

recon_ship   = ship_place(2, get_pos_delim())
dest_ship    = ship_place(3, get_pos_delim())
submarine    = ship_place(3, get_pos_delim())
battle_ship  = ship_place(4, get_pos_delim())
carrier_ship = ship_place(6, get_pos_delim())

hit_count = 0
recon_count, dest_count, sub_count, batt_count, carr_count = 0, 0, 0, 0, 0
while hit_count < 18:
    guess_pos = [int(raw_input("Guess Row: ")), int(raw_input("Guess Column: "))]
    if board[guess_pos[0]][guess_pos[1]] == 'H' or board[guess_pos[0]][guess_pos[1]] == 'M':
        print "You guessed that position already!"
        continue
    elif guess_pos in recon_ship:
        print "HIT! You hit the reconnasance ship!"
        board[guess_pos[0]][guess_pos[1]] = 'H'
        recon_count += 1
        hit_count += 1
        if recon_count == len(recon_ship):
            print "The reconnasance ship has sunk"
        else:
            print "There are %s hits required to sink the reconassance ship" % (len(recon_ship) - recon_count)
    elif guess_pos in dest_ship:
        print dest_ship
        print "HIT! You hit the destroyer ship!"
        board[guess_pos[0]][guess_pos[1]] = 'H'
        dest_count += 1
        hit_count += 1
        if dest_count == len(dest_ship):
            print "The destroyer ship has sunk"
        else:
            print "There are %s hits required to sink the destroyer ship" % (len(dest_ship) - dest_count)
    elif guess_pos in submarine:
        print "HIT! You hit the sumbraine!"
        board[guess_pos[0]][guess_pos[1]] = 'H'
        sub_count += 1
        hit_count += 1
        if sub_count == len(submarine):
            print "The submarine has sunk"
        else:
            print "There are %s hits required to sink the submarine" % (len(submarine) - sub_count)
    elif guess_pos in battle_ship:
        print battle_ship
        print "HIT! You hit the battle ship!"
        board[guess_pos[0]][guess_pos[1]] = 'H'
        batt_count += 1
        hit_count += 1
        if batt_count == len(battle_ship):
            print "The battle ship has sunk"
        else:
            print "There are %s hits required to sink the battle ship" % (len(battle_ship) - batt_count)
    elif guess_pos in carrier_ship:
        print "HIT! You hit the Aircraft Carrier"
        board[guess_pos[0]][guess_pos[1]] = 'H'
        carr_count += 1
        hit_count += 1
        if carr_count == len(carrier_ship):
            print "The Carrier has sunk"
        else:
            print "There are %s hits required to sink the carrier" % (len(carrier_ship) - carr_count)
    else:
        print "MISS!"
        board[guess_pos[0]][guess_pos[1]] = 'M'

    print_board(board)

print "Congratulations! You sunk the fleet!"
