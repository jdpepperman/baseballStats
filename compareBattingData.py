import sys
import cPickle as pickle
from Player import *

if len(sys.argv) != 4:
	print("Pass the program the two dates to compare in yyyy-mm-dd format followed by the stat to compare")
        exit()

firstDate = "battingDataFile_" + str(sys.argv[1])
secondDate = "battingDataFile_" + str(sys.argv[2])

try:
    firstBatterData = pickle.load(open("/home/joshua/programming/baseball/playerData/" + firstDate, "rb"))
    secondBatterData = pickle.load(open("/home/joshua/programming/baseball/playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

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
        if secondPos - firstPos > 1 or firstPos - secondPos > 0 or secondPos == -1 or firstPos == -1:
		nameAndMove = second.getStat('name') + ": " + str(firstPos+1) + " -> " + str(secondPos+1)
		if len(nameAndMove) <= 25:
            		print(nameAndMove + "\t\t\t" + str(second.getStat(sys.argv[3])))
		else:
            		print(nameAndMove + "\t\t" + str(second.getStat(sys.argv[3])))
			
