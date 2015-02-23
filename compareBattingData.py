import sys
import cPickle as pickle
from Player import *

if len(sys.argv) != 4:
	print("Pass the program the two dates to compare in dd-mm-yyy format followed by the stat to compare")
        exit()

firstDate = "battingDataFile_" + str(sys.argv[1])
secondDate = "battingDataFile_" + str(sys.argv[2])

try:
    firstBatterData = pickle.load(open("playerData/" + firstDate, "rb"))
    secondBatterData = pickle.load(open("playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

#remove this later
secondBatterData.getPlayer("Jose Altuve").ab = 999
secondBatterData.addPlayer(Player("Joshua Pepperman", "TOR", 523, 1000, 82, 92, 32, 18, 1001, 4, 9, 92, 21, .300, .682, .382, .975, .932))

if len(secondBatterData) < len(firstBatterData):
    while len(secondBatterData) != len(firstBatterData):
        secondBatterData.addPlayer(Player("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
elif len(firstBatterData) < len(secondBatterData):
    while len(firstBatterData) != len(secondBatterData):
        firstBatterData.addPlayer(Player("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

#now they should have an equal number of players
    
firstBatterData.calculateScores()
secondBatterData.calculateScores()

firstBatterData.sortBy(sys.argv[3])
secondBatterData.sortBy(sys.argv[3])

for i in range(1, len(firstBatterData)+1):
    second = secondBatterData[i-1]
    first = firstBatterData[i-1]
    if second != first:
        #get position of second in both and compare it
        secondPos = secondBatterData.indexOf(second)
        firstPos = firstBatterData.indexOf(second)
        if secondPos - firstPos > 1 or secondPos == -1 or firstPos == -1:
            print(second.name + ": " + str(firstPos+1) + " -> " + str(secondPos+1) + "\t" + second.getStat(sys.argv[3]))
        #print(second.name + ": " + str(firstPos+1) + " -> " + str(secondPos+1))

        #only show the changes for people who moved up, or down by more than 1 (?)
