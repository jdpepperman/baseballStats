#Joshua Pepperman

import urllib2
import os
import datetime
from datetime import timedelta
import cPickle as pickle
from Batters import *
from Batter import *
from Pitchers import *
from Pitcher import *

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
while i <= 700:
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

hldPitcherLinks = ["http://www.sportingcharts.com/mlb/stats/pitching-holds-leaders/2014/#"]

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
for pl in pitcherLinks:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""

        while "<tr " in html:
            lineToAdd = html[html.index("<tr "):html.index("</tr>")]
            htmlLines.append(lineToAdd)
            html = html[html.index("</tr>")+5:]

        playerHtmlLines = []
        for h in htmlLines:
            if "http://espn.go.com/mlb/player/_/id/" in h:
                playerHtmlLines.append(h)

	for p in playerHtmlLines:
                p = p[p.index("http://espn.go.com/mlb/player/_/id/")+35:]
                name = p[p.index(">")+1:p.index("</a>")]
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gp = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                gs = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                ip = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                h = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                r = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                er = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                bb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                so = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                w = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                l = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                sv = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                blsv = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                war = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                whip = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                era = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                if gp != "" and not pitchers.hasPitcher(name):
                        newPitcher = Pitcher(name,team,gp,gs,ip,h,r,er,bb,so,w,l,sv,blsv,war,whip,era)
			#print("Added: " + newPitcher.toString())
			if newPitcher.hasData():
				newPitcher.addExpandedData1(0,0,0,0,0,0,0,0,0,0,0,0,0)
				newPitcher.addExpandedData2(0,0,0,0,0,0,0,0,0,0,0,0)
				newPitcher.addSaberData(0,0,0,0,0,0,0,0,0)
                                newPitcher.addOppBattingStats(0,0,0,0,0,0,0,0,0,0,0,0,0)
                        	pitchers.addPitcher(newPitcher)

for pl in expanded1Links:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""

        while "<tr " in html:
            lineToAdd = html[html.index("<tr "):html.index("</tr>")]
            htmlLines.append(lineToAdd)
            html = html[html.index("</tr>")+5:]

        playerHtmlLines = []
        for h in htmlLines:
            if "http://espn.go.com/mlb/player/_/id/" in h:
                playerHtmlLines.append(h)

	for p in playerHtmlLines:
                p = p[p.index("http://espn.go.com/mlb/player/_/id/")+35:]
                name = p[p.index(">")+1:p.index("</a>")]
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                era = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                cg = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                sho = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                tbf = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                gf = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                svo = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                sh = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                sf = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                hbp = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                gdp = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                wp = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                bk = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                qs = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                qsp = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                if era != "" and pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addExpandedData1(cg,sho,tbf,gf,svo,sh,sf,hbp,gdp,wp,bk,qs,qsp)

for pl in expanded2Links:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""

        while "<tr " in html:
            lineToAdd = html[html.index("<tr "):html.index("</tr>")]
            htmlLines.append(lineToAdd)
            html = html[html.index("</tr>")+5:]

        playerHtmlLines = []
        for h in htmlLines:
            if "http://espn.go.com/mlb/player/_/id/" in h:
                playerHtmlLines.append(h)

	for p in playerHtmlLines:
                p = p[p.index("http://espn.go.com/mlb/player/_/id/")+35:]
                name = p[p.index(">")+1:p.index("</a>")]
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                era = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                k2bb = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                k29 = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                pit = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                p2pa = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                p2ip = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                wper = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                ags = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                gb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                fb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                g2f = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                rs = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                whip = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                if k2bb != "" and pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addExpandedData2(k2bb,k29,pit,p2pa,p2ip,wper,ags,gb,fb,g2f,rs,whip)

for pl in saberPitcherLinks:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""

        while "<tr " in html:
            lineToAdd = html[html.index("<tr "):html.index("</tr>")]
            htmlLines.append(lineToAdd)
            html = html[html.index("</tr>")+5:]

        playerHtmlLines = []
        for h in htmlLines:
            if "http://espn.go.com/mlb/player/_/id/" in h:
                playerHtmlLines.append(h)

	for p in playerHtmlLines:
                p = p[p.index("http://espn.go.com/mlb/player/_/id/")+35:]
                name = p[p.index(">")+1:p.index("</a>")]
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                era = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                erc = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                ercr = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                dips = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                dipr = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                tloss = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                cwin = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                pfr = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                babip = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                k29 = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                if erc != "" and pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addSaberData(erc,ercr,dips,dipr,tloss,cwin,pfr,babip,k29)
                    
for pl in oppPitcherLinks:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""

        while "<tr " in html:
            lineToAdd = html[html.index("<tr "):html.index("</tr>")]
            htmlLines.append(lineToAdd)
            html = html[html.index("</tr>")+5:]

        playerHtmlLines = []
        for h in htmlLines:
            if "http://espn.go.com/mlb/player/_/id/" in h:
                playerHtmlLines.append(h)

	for p in playerHtmlLines:
                p = p[p.index("http://espn.go.com/mlb/player/_/id/")+35:]
                name = p[p.index(">")+1:p.index("</a>")]
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                era = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                tb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                b2 = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                b3 = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                hr = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                rbi = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                ibb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                sb = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                cs = int(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                csp = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                baa = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                obp = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                slg = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                p = p[p.index("</td>")+5:]
                ops = float(p[p.index(">")+1:find_nth(p, "<", 2)])
                if tb != "" and pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addOppBattingStats(tb,b2,b3,hr,rbi,ibb,sb,cs,csp,baa,obp,slg,ops)
		    
for pl in hldPitcherLinks:
    response = urllib2.urlopen(pl)
    html = response.read()
    
    htmlLines = []
    lineToAdd = ""
    
    for char in html:
        if '\n' in char or '\r' in char:
                htmlLines.append(lineToAdd)
                lineToAdd = ""
        else:
                lineToAdd = lineToAdd + char
    
    playerHtmlLines = []
    for h in htmlLines:
        if "/mlb/players/" in h:
            playerHtmlLines.append(h)

    for p in playerHtmlLines:
        p = p[p.index("/mlb/players/")+13:]
        p = p[p.index(">")+1:]
        name = p[:p.index("</a>")]
        p = p[find_nth(p, "center", 3):]
        hld = int(p[p.index('>')+1:p.index('<')])
        if hld != "" and pitchers.getPitcher(name):
            pitchers.getPitcher(name).addOther(hld)


batters.calculateScores()
pitchers.calculateScores()

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

pickle.dump(batters, open(os.getcwd() + "/playerData/battingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb"))
pickle.dump(pitchers, open(os.getcwd() + "/playerData/pitchingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb"))

csv = open(os.getcwd() + "/playerData/csvFiles/battingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb")
csv.write(batters.toCSV())
csvP = open(os.getcwd() + "/playerData/csvFiles/pitchingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb")
csvP.write(pitchers.toCSV())
