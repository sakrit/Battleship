##
## Class for the ships in battleship
##
from random import randint
## Custom Modules Below
import board

class ship(object):

    '''
    Class will:
        * Set the locations for each of the ships
        * Make sure they don't overlap
        * Set out what happens when a ship is hit
    '''

    def location(self, length, pos, board): # ship_place
        
        '''
        Set the location of the ship on the board
        '''

        iVal_x = randint(0, len(board) - 1)
        iVal_y = randint(0, len(board) - 1)
        ship    = [[iVal_x, iVal_y]]
        if pos == 'd':
            if (iVal_y + length - 1) > len(board) - 1 and (iVal_x + length - 1 <= len(board) - 1):
                for i in xrange(1, length):
                    ship.append([iVal_x + i, iVal_y])
            elif (iVal_y + length - 1) > len(board) - 1 and (iVal_x + length - 1 > len(board) - 1):
                for i in xrange(1, length):
                    ship.append([iVal_x, iVal_y - i])
            else:
                for i in xrange(1, length):
                    ship.append([iVal_x, iVal_y + i])
        else:
            if (iVal_x + length - 1) > len(board) - 1 and (iVal_y + length - 1 <= len(board) - 1):
                for i in xrange(1, length):
                    ship.append([iVal_x, iVal_y + i])
            elif (iVal_x + length - 1) > len(board) - 1 and (iVal_y + length - 1 > len(board) - 1):
                for i in xrange(1, length):
                    ship.append([iVal_x - i, iVal_y])
            else:
                for i in xrange(1, length):
                    ship.append([iVal_x + i, iVal_y])

        if checkOverlap(ship, board):
            for location in ship:
                board.place(location, board, 'S')
            
            return ship
        else:
            return location(length, pos, board)


    def orientation(self): # get_pos_delim
        
        '''
        Set the orientation of the ship (up or accross)
        '''

        if randint(0, 1) == 0:
            return 'd'
        else:
            return 'r'


    def checkOverlap(self, ship, board): # check_ship_place
        
        '''
        Check if the position is already filled
        '''

        for i in ship:
            if board[i[0]][i[1]] == 'S':
                return False
            else:
                continue

        return True
    

    def hit(self, pos, h_count, name, length, s_count): # hit_ship

        '''
        Called in the instance of a hit
        '''

        print "HIT! You hit the " + ship_name
        board.place(pos, board, 'H')
        h_count += 1
        s_count += 1

        if s_count == length:
            print 'The %s has sunk' % (name)
        else:
            print 'There are %s hits required to sink the %s' % (length - s_count, name)

        return h_count, s_count
