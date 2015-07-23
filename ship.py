##
## Class for the ships in battleship
##

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

    def orientation(self): # get_pos_delim
        
        '''
        Set the orientation of the ship (up or accross)
        '''

    def checkOverlap(self, ship, board): # check_ship_place
        
        '''
        Check if the position is already filled
        '''
    
    def hit(self, pos, h_count, name, length, s_count): # hit_ship

        '''
        Called in the instance of a hit
        '''
