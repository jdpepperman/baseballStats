import sys
import urllib2
import datetime
from datetime import timedelta
import cPickle as pickle
from Batter import *
from Batters import *

def find_nth(haystack, needle, n):
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

batters = pickle.load(open("playerData/battingDataFile_" + yesterday.strftime("%Y-%m-%d"), "rb"))

batters.calculateScores()
print("NAME\t\t\t\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR\tSCORE")
if len(sys.argv) == 2:
	batters.sortBy(sys.argv[1])
	print(batters.toString())
elif len(sys.argv) == 3:
	batters.sortBy(sys.argv[1])
	if int(sys.argv[2]) < 0:
		print(batters.toStringInRange(range(len(batters)-1, len(batters) - int(sys.argv[2][1:])-1, -1)))
	else:
		print(batters.toStringInRange(range(0, int(sys.argv[2]))))
else:
	pass
