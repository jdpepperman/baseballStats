import sys
import urllib2
import time
import cPickle as pickle
from Player import *
from Batters import *

def find_nth(haystack, needle, n):
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

batters = pickle.load(open("playerData/battingDataFile_" + time.strftime("%d-%m-%Y"), "rb"))

batters.calculateScores()
print("NAME\t\t\t\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR\tSCORE")
if len(sys.argv) == 2:
	batters.sortBy(sys.argv[1])
	for player in batters:
		print(player.toString())
elif len(sys.argv) == 3:
	batters.sortBy(sys.argv[1])
	if int(sys.argv[2]) < 0:
		for i in range(len(batters)-1, len(batters) - int(sys.argv[2][1:])-1, -1):
			print(batters[i].toString())
	else:
		for i in range(0, int(sys.argv[2])):
			print(batters[i].toString())
else:
	pass
