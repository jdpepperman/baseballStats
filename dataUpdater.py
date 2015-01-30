import urllib2
import time
import cPickle as pickle
from Batters import *
from Player import *

def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
                start = haystack.find(needle, start+len(needle))
                n -= 1
        return start

batters = Batters()

#playerLinks = ["http://espn.go.com/mlb/stats/batting/_/sort/atBats/order/true","http://espn.go.com/mlb/stats/batting/_/sort/runs/order/true","http://espn.go.com/mlb/stats/batting/_/sort/hits/order/true","http://espn.go.com/mlb/stats/batting/_/sort/doubles/order/true","http://espn.go.com/mlb/stats/batting/_/sort/triples/order/true","http://espn.go.com/mlb/stats/batting/_/sort/homeRuns/order/true","http://espn.go.com/mlb/stats/batting/_/sort/RBIs/order/true","http://espn.go.com/mlb/stats/batting/_/sort/stolenBases/order/true","http://espn.go.com/mlb/stats/batting/_/sort/caughtStealing/order/true","http://espn.go.com/mlb/stats/batting/_/sort/walks/order/true","http://espn.go.com/mlb/stats/batting/_/sort/strikeouts/order/true","http://espn.go.com/mlb/stats/batting/_/order/true","http://espn.go.com/mlb/stats/batting/_/sort/onBasePct/order/true","http://espn.go.com/mlb/stats/batting/_/sort/slugAvg/order/true","http://espn.go.com/mlb/stats/batting/_/sort/OPS/order/true","http://espn.go.com/mlb/stats/batting/_/sort/WARBR/order/true"]
playerLinks = ["http://espn.go.com/mlb/stats/batting/_/sort/atBats/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/41/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/81/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/121/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/161/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/201/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/241/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/281/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/321/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/361/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/401/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/441/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/481/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/521/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/561/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/601/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/641/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/681/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/721/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/761/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/801/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/841/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/881/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/921/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/961/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1001/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1041/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1081/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1121/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1161/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1201/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1241/qualified/false","http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/1281/qualified/false"]

expandedStatLinks = ["http://espn.go.com/mlb/stats/batting/_/type/expanded"]
i = 1
while i <= 1281:
	i = i + 40
	expandedStatLinks.append("http://espn.go.com/mlb/stats/batting/_/count/" + str(i) + "/qualified/true/type/expanded")

saberStatLinks = ["http://espn.go.com/mlb/stats/batting/_/type/sabermetric"]
i = 1
while i <= 1281:
	i = i + 40
	saberStatLinks.append("http://espn.go.com/mlb/stats/batting/_/count/" + str(i) + "/qualified/true/type/sabermetric")

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
		if ab != 0: data = True
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
			if newPlayer.hasData():
                        	batters.addPlayer(newPlayer)

pickle.dump(batters, open("/home/joshua/programming/baseball/playerData/battingDataFile_" + time.strftime("%d-%m-%Y"), "wb"))
