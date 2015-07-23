##
## Class for battleship board(s)
##

class board(object):

    '''
    Class Will:
        * Setup the battleship playing field
        * Print the board
        * Clear the board at the end of the game
        * Place objects onto the board
        * Make sure the guesses are legal
        * Convert the coordinates
    '''

    def __init__(self): # global board setting

        '''
        Setup the board
        '''

    def print(self, board): # print_board

        '''
        Print the board to the terminal
        '''

    def clear(self, board): # clear_board

        '''
        Return the board to a natural state
        '''

    def place(self, guess, boardi, delim): # place_ship

        '''
        Change the value of the coordinate of the board
        '''

    def legalGuess(self, guess, board): # is_good_guess

        '''
        Check the guess is within the board
        '''

    def convertX(self, x): # get_x_coord

        '''
        Convert the X coordinate to a list location
        '''

    def convertY(self, y): # get_y_coord

        '''
        Convert the Y coordinate to a list location
        '''
