##
## Module to perform some stats
##
import utils

def totTime(start, end):

    return end - start

def minutes(time):

    return int(time / 60)

def seconds(time):

    return int(time % 60)

def saveTime(time):

    dir_ = './.Scores/'
    utils.mkdir_p(dir_)
    f = open(dir_ + '.Scores.txt', 'a')
    f.write(str(time) + '\n')
    f.close()

