import urllib2
import datetime
from datetime import timedelta
import cPickle as pickle
from Batters import *
from Batter import *
from Pitchers import *
from Pither import *

def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
                start = haystack.find(needle, start+len(needle))
                n -= 1
        return start

batters = Batters()
pitchers = Pitchers()


#batter stat links
playerLinks = ["http://espn.go.com/mlb/stats/batting/_/sort/atBats/qualified/false"]
i = 1
while i <= 1281:
	i = i + 40
	playerLinks.append("http://espn.go.com/mlb/stats/batting/_/sort/atBats/count/"+ str(i) + "/qualified/false")

expandedStatLinks = ["http://espn.go.com/mlb/stats/batting/_/type/expanded"]
i = 1
while i <= 121:
	i = i + 40
	expandedStatLinks.append("http://espn.go.com/mlb/stats/batting/_/count/" + str(i) + "/qualified/true/type/expanded")

saberStatLinks = ["http://espn.go.com/mlb/stats/batting/_/type/sabermetric"]
i = 1
while i <= 121:
	i = i + 40
	saberStatLinks.append("http://espn.go.com/mlb/stats/batting/_/count/" + str(i) + "/qualified/true/type/sabermetric")

#pitcher stat links
pitcherLinks = ["http://espn.go.com/mlb/stats/pitching/_/sort/thirdInnings"]
i = 1
while i <= 652:
    i = i + 40
    pitcherLinks.append("http://espn.go.com/mlb/stats/pitching/_/sort/thirdInnings/count/"+ str(i) +"/qualified/false")

expanded1Links = ["http://espn.go.com/mlb/stats/pitching/_/sort/battersFaced/qualified/false/type/expanded"]
i = 1
while i <= 652:
    i = i + 40
    expanded1Links.append("http://espn.go.com/mlb/stats/pitching/_/sort/battersFaced/count/" + str(i) + "/qualified/false/type/expanded")

expanded2Links = ["http://espn.go.com/mlb/stats/pitching/_/qualified/false/type/expanded-2/order/false"]
i = 1
while i <= 652:
    i = i + 40
    expanded2Links.append("http://espn.go.com/mlb/stats/pitching/_/count/" + str(i) + "/qualified/false/type/expanded-2/order/false")

saberPitcherLinks = ["http://espn.go.com/mlb/stats/pitching/_/qualified/false/type/sabermetric/order/false"]
i = 1
while i <= 652:
    i = i + 40
    saberPitcherLinks.append("http://espn.go.com/mlb/stats/pitching/_/count/" + str(i) + "/qualified/false/type/sabermetric/order/false")

oppPitcherLinks = ["http://espn.go.com/mlb/stats/pitching/_/qualified/false/type/opponent-batting/order/false"]
i = 1
while i <= 652:
    i = i + 40
    oppPitcherLinks.append("http://espn.go.com/mlb/stats/pitching/_/count/" + str(i) + "/qualified/false/type/opponent-batting/order/false")

hldPitcherLink = ["http://www.sportingcharts.com/mlb/stats/pitching-holds-leaders/2014/#"]

#get the batter data from the links
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
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
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
                if ab != "" and not batters.hasBatter(name):
                        newBatter = Batter(name,team,ab,r,h,b2,b3,hr,rbi,sb,cs,bb,so,avg,obp,slg,ops,war)
			if newBatter.hasData():
				newBatter.addExpandedData(0,0,0,0,0,0,0,0,0,0,0)
				newBatter.addSaberData(0,0,0,0,0,0,0,0,0,0)
                        	batters.addBatter(newBatter)

for pl in expandedStatLinks:
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
                gp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                p = p[p.index("</td>")+5:]
                tpa = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                pit = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                p2pa = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                tb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                xbh = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                hbp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ibb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gdp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sh = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sf = p[p.index(">")+1:find_nth(p, "<", 2)]
                if gp != "":
			batters.getBatter(name).addExpandedData(gp, tpa, pit, p2pa, tb, xbh, hbp, ibb, gdp, sh, sf)

for pl in saberStatLinks:
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
                p = p[p.index("</td>")+5:]
                rc = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                rc27 = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                isop = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                seca = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                fb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                g2f = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ab2hr = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                bb2pa = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                bb2k = p[p.index(">")+1:find_nth(p, "<", 2)]
                if rc != "":
			batters.getBatter(name).addSaberData(rc, rc27, isop, seca, gb, fb, g2f, ab2hr, bb2pa, bb2k)

#get the pitcher data from the links


batters.calculateScores()

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

pickle.dump(batters, open("/home/joshua/programming/baseball/playerData/battingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb"))

csv = open("/home/joshua/programming/baseball/playerData/csvFiles/battingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb")
csv.write(batters.toCSV())
