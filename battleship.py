# script for playing battleship

import time
## Custom Modules Below!
import board
import ship

def playBattleship(iBoard):
    '''
    Main function for doing the actual game
    '''
    ## Create instance of ship class
    iShip = ship.Ship()

    ## Create the two boards used and display the players board
    ## for reference
    main_board = iBoard.get(10)
    pc_board   = iBoard.get(10)
    iBoard.display(main_board)

    ## Get each of the ships and place them on the pc board
    recon_ship   = iShip.location(2, pc_board)
    dest_ship    = iShip.location(3, pc_board)
    submarine    = iShip.location(3, pc_board)
    battle_ship  = iShip.location(4, pc_board)
    carrier_ship = iShip.location(5, pc_board)
   
    ## Start the main game loop, looping until all the ships are sunk
    hit_count = 0
    recon_count, dest_count, sub_count, batt_count, carr_count = 0, 0, 0, 0, 0
    n_hits    = len(recon_ship) + len(dest_ship) + len(submarine) + len(battle_ship) + len(carrier_ship)
    while hit_count < n_hits:
        guess = [iBoard.convertX(raw_input("Guess Column: ")), iBoard.convertY(raw_input("Guess Row: "))]
        if iBoard.legalGuess(guess, main_board):
            if guess in recon_ship:
                hit_count, recon_count = iShip.hit(guess, hit_count, main_board, 'reconnasance ship', 
                                                   len(recon_ship), recon_count)
            elif guess in dest_ship:
                hit_count, dest_count  = iShip.hit(guess, hit_count, main_board, 'destroyer ship',
                                                   len(dest_ship), dest_count)
            elif guess in submarine:
                hit_count, sub_count   = iShip.hit(guess, hit_count, main_board, 'submarine',
                                                   len(submarine), sub_count)
            elif guess in battle_ship:
                hit_count, batt_count  = iShip.hit(guess, hit_count, main_board, 'battle ship',
                                                   len(battle_ship), batt_count)
            elif guess in carrier_ship:
                hit_count, carr_count  = iShip.hit(guess, hit_count, main_board, 'carrier',
                                                    len(carrier_ship), carr_count)
            else:
                print 'MISS!'
                iBoard.place(guess, main_board, 'M')
        else:
            continue

        iBoard.display(main_board)
    else:
        print 'Congratualtions! You sank the fleet'


def playAgain(char):
    yes = ['y', 'yes']
    no  = ['n', 'no']
    while char.lower() not in yes and char.lower() not in no:
        print "I'm sorry, that is not a vaild option."
        char = raw_input('Would you like to play again? (y/n) ')
    else:
        if char.lower() in yes:
            return True
        else:
            print 'Thanks for playing!'
            return False


def main():
    iBoard = board.Board()
    
    play_game = True
    while play_game == True:
        ##
        ## Play Battleship
        ##
        start = time.time()
        print "Let's play Battleship!"
        playBattleship(iBoard)
        end   = time.time() - start
        ##
        ## Print out the basic statistics
        ##
        print "Well done! This game took %s minutes" % (end / 60)
        print "The average time per hit was: %s seconds" % (end / 17)
        play_game = playAgain(raw_input('Would you like to play again? (y/n) '))


if __name__ == '__main__':
    main()
