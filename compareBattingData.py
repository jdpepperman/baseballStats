#Joshua Pepperman

import sys
import os
import cPickle as pickle
from Batter import *

if len(sys.argv) != 4:
	print("Pass the program the two dates to compare in yyyy-mm-dd format followed by the stat to compare")
        exit()

battingStats = {
        'score' : "Score",
	'ab' : "At Bats",
	'r' : "Runs",
	'h' : "Hits",
	'b2' : "Doubles",
	'b3' : "Triples",
	'hr' : "Home Runs",
	'rbi' : "Runs Batted In",
	'sb' : "Stolen Bases",
	'cs' : "Caught Stealing",
	'bb' : "Walks",
	'so' : "Strike Outs",
	'avg' : "Batting Average",
	'obp' : "On Base Perentage",
	'slg' : "Slugging Percentage",
	'ops' : "OBP + SLG",
	'war' : "Wins Above Replacement",
	'rc' : "Runs Created",
	'rc27' : "Runs Created per 27 Outs",
	'isop' : "Isolated Power",
	'seca' : "Secondary Average",
	'gb' : "Ground Balls",
	'fb' : "Fly Balls",
	'g2f' : "Ground Balls to Fly Balls",
	'ab2hr' : "At Bats per Home Run",
	'bb2pa' : "Walks per Plate Appearance",
	'bb2k' : "Walk to Strikeout Ratio",
	'gp' : "Games Played",
	'tpa' : "Total Plate Appearances",
	'pit' : "Number of Pitches",
	'p2pa' : "Pitches per Plate Appearances",
	'tb' : "Total Bases",
	'xbh' : "Extra Base Hits",
	'hbp' : "Hit By Pitch",
	'gdp' : "Ground into Double Play",
	'sh' : "Sacrifice Hits",
        'sf' : "Sacrifice Flies"
}

firstDate = "battingDataFile_" + str(sys.argv[1])
secondDate = "battingDataFile_" + str(sys.argv[2])

try:
    firstBatterData = pickle.load(open(os.getcwd() + "/playerData/" + firstDate, "rb"))
    secondBatterData = pickle.load(open(os.getcwd() + "/playerData/" + secondDate, "rb"))
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

if len(secondBatterData) < len(firstBatterData):
    while len(secondBatterData) != len(firstBatterData):
        secondBatterData.addBatter(Batter("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
elif len(firstBatterData) < len(secondBatterData):
    while len(firstBatterData) != len(secondBatterData):
        firstBatterData.addBatter(Batter("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

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
		print(battingStats[sys.argv[3]] + "\n")
		nameAndMove = second.getStat('name') + ": " + str(firstPos+1) + " -> " + str(secondPos+1)
		if len(nameAndMove) <= 25:
            		print(nameAndMove + "\t\t\t" + str(second.getStat(sys.argv[3])))
			print()
		else:
            		print(nameAndMove + "\t\t" + str(second.getStat(sys.argv[3])))
			print()
			
