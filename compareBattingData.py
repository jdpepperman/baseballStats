import sys
import cPickle as pickle

if len(sys.argv) != 3:
	print("Pass the program the two dates to compare in dd/mm/yyy format")

firstDate = "battingDataFile_" + str(sys.argv[1])
secondDate = "battingDataFile_" + str(sys.argv[2])

try:
    firstBatterData = pickle.load(open("playerData/" + firstDate, "rb"))
    secondBatterData = pickle.load(open("playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

firstBatterData.sortBy('score')
secondBatterData.sortBy('score')

secondBatterData.getPlayer("Jose Altuve").ab = 999


