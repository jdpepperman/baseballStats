import sys
import cPickle as pickle
from Player import *

if len(sys.argv) != 3:
	print("Pass the program the two dates to compare in dd-mm-yyy format")
        exit()

firstDate = "battingDataFile_" + str(sys.argv[1])
secondDate = "battingDataFile_" + str(sys.argv[2])

try:
    firstBatterData = pickle.load(open("playerData/" + firstDate, "rb"))
    secondBatterData = pickle.load(open("playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()


secondBatterData.getPlayer("Jose Altuve").ab = 999

if len(firstBatterData) < len(secondBatterData):
    while len(secondBatterData) != len(firstBatterData):
        secondBatterData.addBatter(Player("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
elif len(secondBatterData) < len(firstBatterData):
    while len(firstBatterData) != len(secondBatterData):
        firstBatterData.addBatter(Player("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

#now they should have an equal number of players
    
firstBatterData.sortBy('ab')
secondBatterData.sortBy('ab')
