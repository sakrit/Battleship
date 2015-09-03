##
## Class for battleship board(s)
##

class Board(object):

    '''
    Class Will:
        * Setup the battleship playing field
        * Print the board
        * Clear the board at the end of the game
        * Place objects onto the board
        * Make sure the guesses are legal
        * Convert the coordinates
    '''

    def __init__(self, length):

        self.__board = []
        self._length = length
        ## Create the board
        for x in xrange(self._length):
            self.__board.append(["O"] * self._length)


    def display(self): # print_board

        '''
        Print the board to the terminal
        '''
        print ''
        print 'A B C D E F G H I J |  '
        print '--------------------|--'
        for i, row in enumerate(self.__board):
            print ' '.join(row) + ' |' + str(i + 1)


    def fill(self, guess, delim): # place_ship

        '''
        Change the value of the coordinate of the board
        '''
        self.__board[guess[1]][guess[0]] = delim
        
        return self.__board


    def getFillValue(self, i1, i2):

        return self.__board[i1][i2]


    def legalGuess(self, guess): # is_good_guess

        '''
        Check the guess is within the board
        '''
        if guess[0] > len(self.__board) or guess[0] < 0:
            print 'That position is invalid, try again'
            return False
        elif guess[1] > len(self.__board) or guess[1] < 0:
            print 'That position is invalid, try again'
            return False
        elif self.__board[guess[1]][guess[0]] == 'H' or self.__board[guess[1]][guess[0]] == 'M':
            print 'You have guessed that position already! Try again'
            return False
        else:
            return True


    def convertX(self, x): # get_x_coord

        '''
        Convert the X coordinate to a list location
        '''
        d = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
             'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}
        try:
            return d[x.upper()]
        except KeyError as e:
            print 'KeyError:: %s not valid' % (e)
            return -1


    def convertY(self, y): # get_y_coord

        '''
        Convert the Y coordinate to a list location
        '''
        try:
            return int(y) - 1
        except ValueError as e:
            print 'ValueError::', e
            return -1


