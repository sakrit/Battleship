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

    def get(self, length): # global board setting

        board = []
        for x in range(length):
            board.append(["O"] * length)

        return board


    def display(self, board): # print_board

        '''
        Print the board to the terminal
        '''
        print ''
        print 'A B C D E F G H I J |  '
        print '--------------------|--'
        for i, row in enumerate(board):
            print ' '.join(row) + ' |' + str(i + 1)


    def clear(self, board): # clear_board

        '''
        Return the board to a natural state
        '''
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                board[i][j] = "O"


    def place(self, guess, board, delim): # place_ship

        '''
        Change the value of the coordinate of the board
        '''

        board[guess[1]][guess[0]] = delim

        return board


    def legalGuess(self, guess, board): # is_good_guess

        '''
        Check the guess is within the board
        '''
        if guess[0] > len(board) or guess[0] < 0:
            print 'That position is invalid, try again'
            return False
        elif guess[1] > len(board) or guess[1] < 0:
            print 'That position is invalid, try again'
            return False
        elif board[guess[0]][guess[1]] == 'H' or board[guess[0]][guess[1]] == 'M':
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
