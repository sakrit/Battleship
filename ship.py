##
## Class for the ships in battleship
##
from random import randint
## Custom Modules Below
import board as b


def location(length, board): # ship_place
    
    '''
    Set the location of the ship on the board
    '''

    pos = orientation()
    board_length =  board.getLength()
    iVal_x = randint(0, board_length - 1)
    iVal_y = randint(0, board_length - 1)
    ship    = [[iVal_x, iVal_y]]
    if pos == 'd':
        if (iVal_y + length - 1) > board_length - 1 and (iVal_x + length - 1 <= board_length - 1):
            for i in xrange(1, length):
                ship.append([iVal_x + i, iVal_y])
        elif (iVal_y + length - 1) > board_length - 1 and (iVal_x + length - 1 > board_length - 1):
            for i in xrange(1, length):
                ship.append([iVal_x, iVal_y - i])
        else:
            for i in xrange(1, length):
                ship.append([iVal_x, iVal_y + i])
    else:
        if (iVal_x + length - 1) > board_length - 1 and (iVal_y + length - 1 <= board_length - 1):
            for i in xrange(1, length):
                ship.append([iVal_x, iVal_y + i])
        elif (iVal_x + length - 1) > board_length - 1 and (iVal_y + length - 1 > board_length - 1):
            for i in xrange(1, length):
                ship.append([iVal_x - i, iVal_y])
        else:
            for i in xrange(1, length):
                ship.append([iVal_x + i, iVal_y])

    if checkOverlap(ship, board):
        for loc in ship:
            board.place(loc, 'S')
        
        return ship
    else:
        return location(length, board)


def orientation(): # get_pos_delim
    
    '''
    Set the orientation of the ship (up or accross)
    '''

    if randint(0, 1) == 0:
        return 'd'
    else:
        return 'r'


def checkOverlap(ship, board): # check_ship_place
    
    '''
    Check if the position is already filled
    '''

    for i in ship:
        if board.getFillValue(i[1], i[0]) == 'S':
            return False
        else:
            continue

    return True


def hit(pos, h_count, board, name, length, s_count): # hit_ship

    '''
    Called in the instance of a hit
    '''

    print "\nHIT! You hit the " + name
    board.place(pos, 'H')
    h_count += 1
    s_count += 1

    if s_count == length:
        print 'The %s has sunk' % (name)
    else:
        print 'There are %s hits required to sink the %s' % (length - s_count, name)

    return h_count, s_count
