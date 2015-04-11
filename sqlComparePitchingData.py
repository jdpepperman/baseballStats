#Joshua Pepperman

import sys
import os
import MySQLdb
from Pitcher import *
from Pitchers import *

if len(sys.argv) != 4:
	print("Pass the program the two dates to compare in yyyy-mm-dd format followed by the stat to compare")
        exit()

firstDate = str(sys.argv[1])
secondDate = str(sys.argv[2])

pitchingStats = {
        'score' : "Score",
	'gp' : "Games Played",
	'gs' : "Games Started",
	'ip' : "Innings Pitched",
	'h' : "Hits",
	'r' : "Runs",
	'er' : "Earned Runs",
	'bb' : "Walks",
	'so' : "Strikeouts",
	'w' : "Wins",
	'l' : "Losses",
	'sv' : "Saves",
	'hld' : "Holds",
	'blsv' : "Blown Saves",
	'whip' : "Walks and Hits per Inning Pitched",
	'era' : "Earned Run Average",
	'cg' : "Complete Games",
	'sho' : "Shutouts",
	'tbf' : "Total Batters Faced",
	'gf' : "Games Finished",
	'svo' : "Save Opportunities",
	'sh' : "Sacrifice Bunts",
	'sf' : "Sacrifice Flys",
	'hbp' : "Hit By Pitch",
	'gdp' : "Ground into Double Play",
	'wp' : "Wild Pitches",
	'bk' : "Balks",
	'qs' : "Quality Starts",
	'qsp' : "Quality Start Percentage",
	'k2bb' : "Strikeout to Walk Ratio",
	'k29' : "Strikeouts per 9 Innings",
	'pit' : "Number of Pitches",
	'p2pa' : "Pitches per Plate Appearance",
	'p2ip' : "Pitches per Inning Pitched",
	'wper' : "Win Percentage",
	'ags' : "Average Game Score",
	'gb' : "Ground Balls",
	'fb' : "Fly Balls",
	'g2f' : "Ground Ball to Fly Ball Ratio",
	'rs' : "Run Support Average (per start)",
	'erc' : "Component ERA",
	'ercr' : "Component ERA Ratio",
	'dips' : "Defense Independent ERA",
	'dipr' : "Defense Independent ERA Ratio",
	'tloss' : "Tough Losses",
	'cwin' : "Cheap Wins",
	'pfr' : "Power/Finesse Ratio",
	'babip' : "Batting Average on Balls in Play",
	'obtb' : "Opposing Batter Total Bases",
	'obb2' : "Opposing Batter Doubles",
	'obb3' : "Opposing Batter Triples",
	'obhr' : "Opposing Batter Home Runs",
	'obrbi' : "Opposing Batter Runs Batted In",
	'obibb' : "Opposing Batter Intentional Walks",
	'obsb' : "Opposing Batter Stolen Bases", 
	'obcs' : "Opposing Batter Caught Stealing",
	'obcsp' : "Opposing Batter Caught Stealing Percentage",
	'obbaa' : "Opposing Batter Batting Average",
	'obobp' : "Opposing Batter On Base Percentage",
	'obslg' : "Opposing Batter Slugging Average",
	'obops' : "Opposing Batter OPS"
}

try:
	firstPitcherData = Pitchers()
	secondPitcherData = Pitchers()
	db = MySQLdb.connect("localhost", "python", "pythonPaSswOrD#", "baseballdb")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM pitchers WHERE date=\"" + firstDate + "\";")
	firstSQLData = cursor.fetchall()
	for row in firstSQLData:
		newPitcher = Pitcher(row[1],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
		newPitcher.addSaberData(row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50],row[33])
		newPitcher.addExpandedData1(row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31])
		newPitcher.addExpandedData2(row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[17])
		newPitcher.addOppBattingStats(row[51],row[52],row[53],row[54],row[55],row[56],row[57],row[58],row[59],row[60],row[61],row[62],row[63])
		firstPitcherData.addPitcher(newPitcher)

	cursor.execute("SELECT * FROM pitchers WHERE date=\"" + secondDate + "\";")
	secondSQLData = cursor.fetchall()
	for row in secondSQLData:
		newPitcher = Pitcher(row[1],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
		newPitcher.addSaberData(row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50],row[33])
		newPitcher.addExpandedData1(row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31])
		newPitcher.addExpandedData2(row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[17])
		newPitcher.addOppBattingStats(row[51],row[52],row[53],row[54],row[55],row[56],row[57],row[58],row[59],row[60],row[61],row[62],row[63])
		secondPitcherData.addPitcher(newPitcher)
	
	cursor.close()
	db.close()
except:
    print("There was a problem with the dates you entered. Please try again with different dates.")
    exit()

if len(secondPitcherData) < len(firstPitcherData):
    while len(secondPitcherData) != len(firstPitcherData):
        secondPitcherData.addPitcher(Pitcher("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
elif len(firstPitcherData) < len(secondPitcherData):
    while len(firstPitcherData) != len(secondPitcherData):
        firstPitcherData.addPitcher(Pitcher("Placeholder", "NAN", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

#now they should have an equal number of players
    
firstPitcherData.calculateScores()
secondPitcherData.calculateScores()

firstPitcherData.sortBy(sys.argv[3])
secondPitcherData.sortBy(sys.argv[3])

print(pitchingStats[sys.argv[3]] + "\n")
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
