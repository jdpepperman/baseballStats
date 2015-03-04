#Joshua Pepperman

import sys
import urllib2
import datetime
from datetime import timedelta
import cPickle as pickle
from Pitcher import *
from Pitchers import *

def find_nth(haystack, needle, n):
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

pitchers = pickle.load(open("playerData/pitchingDataFile_" + yesterday.strftime("%Y-%m-%d"), "rb"))

pitchers.calculateScores()
print("NAME\t\t\t\tSCORE\tGP\tGS\tIP\tH\tR\tER\tBB\tSO\tW\tL\tSV\tBLSV\tWAR\tWHIP\tERA\tHLD")
if len(sys.argv) == 2:
	pitchers.sortBy(sys.argv[1])
	print(pitchers.toString())
elif len(sys.argv) == 3:
	pitchers.sortBy(sys.argv[1])
	if int(sys.argv[2]) < 0:
		print(pitchers.toStringInRange(range(len(pitchers)-1, len(pitchers) - int(sys.argv[2][1:])-1, -1)))
	else:
		print(pitchers.toStringInRange(range(0, int(sys.argv[2]))))
else:
	pass
