##
## Class for the ships in battleship
##
from random import randint
## Custom Modules Below
import board as B

class Ship(object):

    def __init__(self, length, name, board):
        
        self._length  = length
        self._name    = name
        self._location = self.placeShip(board)


    def placeShip(self, board): # ship_place
        
        ## Create a board for the ships and get the length
        board_length = board._length
        pos = self.getOrientation()
        iVal_x = randint(0, board_length - 1)
        iVal_y = randint(0, board_length - 1)
        ship    = [[iVal_x, iVal_y]]
        if pos == 'd':
            if (iVal_y + self._length - 1) > board_length - 1 and (iVal_x + self._length - 1 <= board_length - 1):
                for i in xrange(1, self._length):
                    ship.append([iVal_x + i, iVal_y])
            elif (iVal_y + self._length - 1) > board_length - 1 and (iVal_x + self._length - 1 > board_length - 1):
                for i in xrange(1, self._length):
                    ship.append([iVal_x, iVal_y - i])
            else:
                for i in xrange(1, self._length):
                    ship.append([iVal_x, iVal_y + i])
        else:
            if (iVal_x + self._length - 1) > board_length - 1 and (iVal_y + self._length - 1 <= board_length - 1):
                for i in xrange(1, self._length):
                    ship.append([iVal_x, iVal_y + i])
            elif (iVal_x + self._length - 1) > board_length - 1 and (iVal_y + self._length - 1 > board_length - 1):
                for i in xrange(1, self._length):
                    ship.append([iVal_x - i, iVal_y])
            else:
                for i in xrange(1, self._length):
                    ship.append([iVal_x + i, iVal_y])

        if self.checkOverlap(ship, board):
            for loc in ship:
                board.fill(loc, 'S')
            
            return ship
        else:
            return self.placeShip(board)


    def getOrientation(self): # get_pos_delim
        
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
            if board.getFillValue(i[1], i[0]) == 'S':
                return False
            else:
                continue

        return True


    def hit(self, pos, h_count, board, s_count): # hit_ship

        '''
        Called in the instance of a hit
        '''

        print "\nHIT! You hit the " + self._name
        board.fill(pos, 'H')
        h_count += 1
        s_count += 1

        if s_count == self._length:
            print 'The %s has sunk' % (self._name)
        elif self._length - s_count == 1:
            print 'There is one hit required to sink the %s' % (self._name)
        else:
            print 'There are %s hits required to sink the %s' % (self._length - s_count, self._name)

        return h_count, s_count


