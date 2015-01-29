import sys
import urllib2
import cPickle as pickle
from Player import *
from Batters import *

def find_nth(haystack, needle, n):
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

oldBatters = pickle.load(open("battingDataFile","rb"))
batters = Batters()

playerLinks = ["http://espn.go.com/mlb/stats/batting/_/sort/atBats/order/true","http://espn.go.com/mlb/stats/batting/_/sort/runs/order/true","http://espn.go.com/mlb/stats/batting/_/sort/hits/order/true","http://espn.go.com/mlb/stats/batting/_/sort/doubles/order/true","http://espn.go.com/mlb/stats/batting/_/sort/triples/order/true","http://espn.go.com/mlb/stats/batting/_/sort/homeRuns/order/true","http://espn.go.com/mlb/stats/batting/_/sort/RBIs/order/true","http://espn.go.com/mlb/stats/batting/_/sort/stolenBases/order/true","http://espn.go.com/mlb/stats/batting/_/sort/caughtStealing/order/true","http://espn.go.com/mlb/stats/batting/_/sort/walks/order/true","http://espn.go.com/mlb/stats/batting/_/sort/strikeouts/order/true","http://espn.go.com/mlb/stats/batting/_/order/true","http://espn.go.com/mlb/stats/batting/_/sort/onBasePct/order/true","http://espn.go.com/mlb/stats/batting/_/sort/slugAvg/order/true","http://espn.go.com/mlb/stats/batting/_/sort/OPS/order/true","http://espn.go.com/mlb/stats/batting/_/sort/WARBR/order/true"]

for pl in playerLinks:
	response = urllib2.urlopen(pl)
	html = response.read()
	
	htmlLines = []
	lineToAdd = ""
	for char in html:
		if '\n' in char:
			if "PLAYER" in lineToAdd:
				htmlLines.append(lineToAdd)
			lineToAdd = ""
		else:
			lineToAdd = lineToAdd + char
	
	for h in htmlLines:
		playerHtml = ""
		playerHtmlLines = []
		while "</tr>" in h:
			playerHtml = h[h.index("<tr"):h.index("</tr>")]
			playerHtmlLines.append(playerHtml)
			h = h[h.index("</tr>")+5:]
	
	for p in playerHtmlLines:
		p = p[p.index("</td>")+5:]
		name = p[find_nth(p, '>', 2)+1:p.index("</a>")]
		p = p[p.index("</td>")+5:]
		p = p[p.index("</td>")+5:]
		ab = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		r = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		h = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		b2 = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		b3 = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		hr = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		rbi = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		sb = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		cs = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		bb = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		so = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		avg = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		obp = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		slg = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		ops = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		war = p[p.index(">")+1:find_nth(p, "<", 2)]
		p = p[p.index("</td>")+5:]
		if ab != "" and not batters.hasPlayer(name):
			newPlayer = Player(name,ab,r,h,b2,b3,hr,rbi,sb,cs,bb,so,avg,obp,slg,ops,war)
			batters.addPlayer(newPlayer)

batters.calculateScores()
print("NAME\t\t\t\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR\tSCORE")
if len(sys.argv) == 2:
	batters.sortBy(sys.argv[1])
elif len(sys.argv) == 3:
	batters.sortBy(sys.argv[1])
	if int(sys.argv[2]) < 0:
		for i in range(len(batters)-1, len(batters) - int(sys.argv[2][1:])-1, -1):
			print(batters[i].toString())
	else:
		for i in range(0, int(sys.argv[2])):
			print(batters[i].toString())
else:
	for player in batters:
		print(player.toString())

pickle.dump(batters, open("battingDataFile", "wb"))
