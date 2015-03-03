import sys
import cPickle as pickle
from Pitcher import *

if len(sys.argv) != 4:
	print("Pass the program the two dates to compare in yyyy-mm-dd format followed by the stat to compare")
        exit()

firstDate = "pitchingDataFile_" + str(sys.argv[1])
secondDate = "pitchingDataFile_" + str(sys.argv[2])

try:
    firstPitcherData = pickle.load(open("/home/joshua/programming/baseball/playerData/" + firstDate, "rb"))
    secondPitcherData = pickle.load(open("/home/joshua/programming/baseball/playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

if len(secondPitcherData) < len(firstPitcherData):
    while len(secondPitcherData) != len(firstPitcherData):
        secondPitcherData.addPitcher(Pitcher("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
elif len(firstPitcherData) < len(secondPitcherData):
    while len(firstPitcherData) != len(secondPitcherData):
        firstPitcherData.addPitcher(Pitcher("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

#now they should have an equal number of players
    
firstPitcherData.calculateScores()
secondPitcherData.calculateScores()

firstPitcherData.sortBy(sys.argv[3])
secondPitcherData.sortBy(sys.argv[3])

for i in range(1, len(firstPitcherData)+1):
    second = secondPitcherData[i-1]
    first = firstPitcherData[i-1]
    if second != first:
        #get position of second in both and compare it
        secondPos = secondPitcherData.indexOf(second)
        firstPos = firstPitcherData.indexOf(second)
        if secondPos - firstPos > 1 or firstPos - secondPos > 0 or secondPos == -1 or firstPos == -1:
		nameAndMove = second.getStat('name') + ": " + str(firstPos+1) + " -> " + str(secondPos+1)
		if len(nameAndMove) <= 25:
            		print(nameAndMove + "\t\t\t" + str(second.getStat(sys.argv[3])))
		else:
            		print(nameAndMove + "\t\t" + str(second.getStat(sys.argv[3])))
			
