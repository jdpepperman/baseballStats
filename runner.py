import os
import subprocess
import datetime
from datetime import timedelta

stats = {
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

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
dayBeforeYesterday = yesterday - timedelta(days=1)

output = ""

for stat in stats:
	command = "python /home/joshua/programming/baseball/compareBattingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + stats[stat] + "\n" + process.stdout.read() + "\n"

os.system("echo \"" + output + "\" | mail -s \"Baseball Statistics Changes From " + dayBeforeYesterday.strftime("%Y-%m-%d") + " to " + yesterday.strftime("%Y-%m-%d") + "\" joshuapepperman@gmail.com")
