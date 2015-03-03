import os
import subprocess
import datetime
from datetime import timedelta

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
	'blsv' : "Blown Saves",
	'war' : "Wins Above Replacement",
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

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
dayBeforeYesterday = yesterday - timedelta(days=1)

output = "BATTING DATA\n\n"

for stat in battingStats:
	command = "python /home/joshua/programming/baseball/compareBattingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + battingStats[stat] + "\n" + process.stdout.read() + "\n"

output = output + "\nPITCHING DATA\n\n"
for stat in pitchingStats:
	command = "python /home/joshua/programming/baseball/comparePitchingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + pitchingStats[stat] + "\n" + process.stdout.read() + "\n"


os.system("echo \"" + output + "\" | mail -s \"Baseball Statistics Changes From " + dayBeforeYesterday.strftime("%Y-%m-%d") + " to " + yesterday.strftime("%Y-%m-%d") + "\" joshuapepperman@gmail.com")
