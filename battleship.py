## script for playing battleship

## Standard Modules
import time
## Battleship Modules
import board as B
import ship as S
import stats

def playBattleship():

    '''
    Function controlling the gameplay
    '''
    ## Create the board
    main_board = B.Board(10)
    main_board.display()
    pc_board = B.Board(10)

    ## Get each of the ships and place them on the board
    recon     = S.Ship(2, 'reconnaissance ship', pc_board)
    destroyer = S.Ship(3, 'destroyer ship', pc_board)
    submarine = S.Ship(3, 'submarine', pc_board)
    battle    = S.Ship(4, 'battle ship', pc_board)
    carrier   = S.Ship(5, 'carrier', pc_board)
    
    pc_board.display()

    ## Start the main game loop, playing until all the ships are sunk
    hit_count = 0
    recon_count, dest_count, sub_count, batt_count, carr_count = 0, 0, 0, 0, 0
    n_hits    = recon._length + destroyer._length + submarine._length + battle._length + carrier._length
    while hit_count < n_hits:
        guess = [main_board.convertX(raw_input("Guess Column: ")), main_board.convertY(raw_input("Guess Row: "))]
        if main_board.legalGuess(guess):
            if guess in recon._location:
                hit_count, recon_count = recon.hit(guess, hit_count, main_board, recon_count) 
            elif guess in destroyer._location:
                hit_count, dest_count  = destroyer.hit(guess, hit_count, main_board, dest_count)
            elif guess in submarine._location:
                hit_count, sub_count   = submarine.hit(guess, hit_count, main_board, sub_count)
            elif guess in battle._location:
                hit_count, batt_count  = battle.hit(guess, hit_count, main_board, batt_count)
            elif guess in carrier._location:
                hit_count, carr_count  = carrier.hit(guess, hit_count, main_board, carr_count)
            else:
                print 'MISS!'
                main_board.fill(guess, 'M')
        else:
            continue

        main_board.display()
    else:
        print 'Congratualtions! You sank the fleet'


def endGame(start_time):

    total_time = stats.totTime(start_time, time.time())
    minutes = stats.minutes(total_time)
    seconds = stats.seconds(total_time)
    ## Print information about the game to the user
    print "Well done! This game took %s minutes %s seconds" % (minutes, seconds)
    print "The average time per hit was: %s seconds" % (int(total_time / 17))
    stats.saveTime(total_time)


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
        endGame(start)
        play_game = playAgain(raw_input('Would you like to play again? (y/n) '))


if __name__ == '__main__':
    main()
