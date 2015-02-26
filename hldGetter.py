import urllib2

pitcherLinks = []
pl = "http://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=c,114&season=2014&month=0&season1=2014&ind=0&team=0&rost=0&age=0&filter=&players=0&sort=3,d"

response = urllib2.urlopen(pl)
html = response.read()

htmlLines = []
lineToAdd = ""
#work here, it wont cut the crap off the top of the first player.
for char in html:
    if '\n' in char or '\r' in char or '<cf.' in char:
        if "statss.aspx?playerid=" in lineToAdd:
            htmlLines.append(lineToAdd)
            lineToAdd = ""
    else:
            lineToAdd = lineToAdd + char

print(len(htmlLines))
count = 1
for h in htmlLines[1:]:
    print(count)
    print(h)
    count = count + 1


for pl in pitcherLinks:
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
			if newPitcher.hasData():
				newPitcher.addExpandedData1(0,0,0,0,0,0,0,0,0,0,0,0,0)
				newPitcher.addExpandedData2(0,0,0,0,0,0,0,0,0,0,0,0)
				newPitcher.addSaberData(0,0,0,0,0,0,0,0,0)
                                newPitcher.addOppBattingStats(0,0,0,0,0,0,0,0,0,0,0,0,0)
                        	pitchers.addPitcher(newPitcher)
