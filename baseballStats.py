import urllib2
from Player import *

def find_nth(haystack, needle, n):
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

response = urllib2.urlopen('http://espn.go.com/mlb/stats/batting/_/sort/homeRuns/order/true')
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

players = []
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
	newPlayer = Player(name,ab,r,h,b2,b3,hr,rbi,sb,cs,bb,so,avg,obp,slg,ops,war)
	if newPlayer.war != "":
		players.append(newPlayer)

for player in players:
	print(player.toString())
