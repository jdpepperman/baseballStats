import urllib2
from Pitchers import *
from Pitcher import *

def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
                start = haystack.find(needle, start+len(needle))
                n -= 1
        return start
    
pitcherLinks = ["http://www.sportingcharts.com/mlb/stats/pitching-holds-leaders/2014/#"]


for pl in pitcherLinks:
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

    print(len(playerHtmlLines))

    for p in playerHtmlLines:
        p = p[p.index("/mlb/players/")+13:]
        p = p[p.index(">")+1:]
        name = p[:p.index("</a>")]
        p = p[find_nth(p, "center", 3):]
        hld = p[p.index('>')+1:p.index('<')]
        if hld != "":
            pitchers.getPitcher(name).addOther(hld)
