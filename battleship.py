## script for playing battleship

## Standard Modules
import time
## Battleship Modules
import board as B
import ship

def playBattleship():

    '''
    Function controlling the gameplay
    '''
    ## Create the board
    main_board = B.Board(10)
    main_board.display()

    ## Get each of the ships and place them on the board
    recon_ship   = ship.location(2)
    dest_ship    = ship.location(3)
    submarine    = ship.location(3)
    battle_ship  = ship.location(4)
    carrier_ship = ship.location(5)

    ## Start the main game loop, playing until all the ships are sunk
    hit_count = 0
    recon_count, dest_count, sub_count, batt_count, carr_count = 0, 0, 0, 0, 0
    n_hits    = len(recon_ship) + len(dest_ship) + len(submarine) + len(battle_ship) + len(carrier_ship)
    while hit_count < n_hits:
        guess = [main_board.convertX(raw_input("Guess Column: ")), main_board.convertY(raw_input("Guess Row: "))]
        if main_board.legalGuess(guess):
            if guess in recon_ship:
                hit_count, recon_count = ship.hit(guess, hit_count, main_board, 'reconnaissance ship', 
                                                  len(recon_ship),   recon_count)
            elif guess in dest_ship:
                hit_count, dest_count  = ship.hit(guess, hit_count, main_board, 'destroyer ship',      
                                                  len(dest_ship),    dest_count)
            elif guess in submarine:
                hit_count, sub_count   = ship.hit(guess, hit_count, main_board, 'submarine',           
                                                  len(submarine),    sub_count)
            elif guess in battle_ship:
                hit_count, batt_count  = ship.hit(guess, hit_count, main_board, 'battleship',          
                                                  len(battle_ship),  batt_count)
            elif guess in carrier_ship:
                hit_count, carr_count  = ship.hit(guess, hit_count, main_board, 'carrier',             
                                                  len(carrier_ship), carr_count)
            else:
                print 'MISS!'
                main_board.fill(guess, 'M')
        else:
            continue

        main_board.display()
    else:
        print 'Congratualtions! You sank the fleet'


def playAgain(char):

    yes = ['yes', 'y']
    no  = ['no',  'n']
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

    play_game = True;
    while play_game == True:
        start = time.time()
        print "Let's play battleship!"
        playBattleship()
        end = time.time() - start
        print "Well done! This game took %s minutes %s seconds" % (int(end / 60), int(end % 60))
        print "The average time per hit was: %s seconds" % (int(end / 17))
        play_game = playAgain(raw_input('Would you like to play again? (y/n) '))


if __name__ == '__main__':
    main()
