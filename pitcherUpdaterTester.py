import urllib2
import datetime
from datetime import timedelta
import cPickle as pickle
from Pitchers import *
from Pitcher import *

def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
                start = haystack.find(needle, start+len(needle))
                n -= 1
        return start

pitchers = Pitchers()


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

#get the pitcher data from the links
for pl in pitcherLinks:
        response = urllib2.urlopen(pl)
        html = response.read()

        htmlLines = []
        lineToAdd = ""
        #for char in html:
        #        if '\n' in char:
        #                if "http://espn.go.com/mlb/player/_/id/" in lineToAdd:
        #                        htmlLines.append(lineToAdd)
        #                lineToAdd = ""
        #        else:
        #                lineToAdd = lineToAdd + char

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
		print(p)
                name = p[p.index(">")+1:p.index("</a>")]
		print(name)
                p = p[p.index("</td>")+5:]
		team = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gs = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ip = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                h = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                r = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                er = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                bb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                so = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                w = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                l = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sv = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                blsv = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                war = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                whip = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                era = p[p.index(">")+1:find_nth(p, "<", 2)]
                if gp != "" and not pitchers.hasPitcher(name):
                        newPitcher = Pitcher(name,team,gp,gs,ip,h,r,er,bb,so,w,l,sv,blsv,war,whip,era)
			print("Added: " + newPitcher.toString())
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
                era = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                cg = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sho = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                tbf = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gf = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                svo = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sh = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sf = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                hbp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gdp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                wp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                bk = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                qs = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                qsp = p[p.index(">")+1:find_nth(p, "<", 2)]
                if era != "" and not pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addExpandedData1(cg,sho,tbf,gf,svo,sh,sf,hbp,gdp,wp,bk,qs,qsp)

for pl in expanded2Links:
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
                era = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                k2bb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                k29 = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                pit = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                p2pa = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                p2ip = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                wp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ags = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                gb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                fb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                g2f = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                rs = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                whip = p[p.index(">")+1:find_nth(p, "<", 2)]
                if k2bb != "" and not pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addExpandedData2(k2bb,k29,pit,p2pa,p2ip,wp,ags,gb,fb,g2f,rs,whip)

for pl in saberPitcherLinks:
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
                era = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                erc = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ercr = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                dips = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                dipr = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                tloss = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                cwin = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                pfr = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                babip = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                k29 = p[p.index(">")+1:find_nth(p, "<", 2)]
                if erc != "" and not pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addSaberData(erc,ercr,dips,dipr,tloss,cwin,pfr,babip,k29)
                    
for pl in oppPitcherLinks:
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
                era = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                tb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                b2 = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                b3 = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                hr = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                rbi = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ibb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                sb = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                cs = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                csp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                baa = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                obp = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                slg = p[p.index(">")+1:find_nth(p, "<", 2)]
                p = p[p.index("</td>")+5:]
                ops = p[p.index(">")+1:find_nth(p, "<", 2)]
                if tb != "" and not pitchers.hasPitcher(name):
                    pitchers.getPitcher(name).addOppBattingStats(tb,b2,b3,hr,rbi,ibb,sb,cs,csp,baa,slg,ops)
		    
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
        hld = p[p.index('>')+1:p.index('<')]
        if hld != "":
	    print(name)
            pitchers.getPitcher(name).addOther(hld)

pitchers.calculateScores()

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

pickle.dump(pitchers, open("/home/joshua/programming/baseball/playerData/pitchingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb"))

csv = open("/home/joshua/programming/baseball/playerData/csvFiles/pitchingDataFile_" + yesterday.strftime("%Y-%m-%d"), "wb")
csv.write(pitchers.toCSV())
