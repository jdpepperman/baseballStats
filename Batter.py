#Joshua Pepperman

class Batter:
	def __init__(self, name, team, ab, r, h, b2, b3, hr, rbi, sb, cs, bb, so, avg, obp, slg, ops):
		self.mainStats = ['ab','r','h','b2','b3','hr','rbi','sb','cs','bb','so','avg','obp','slg','ops'] 
		self.statDict = {
				'name'	:	name,
				'team'	:	team,
				'ab'	:	int(ab),
				'r'	:	int(r),
				'h'	:	int(h),
				'b2'	:	int(b2),
				'b3'	:	int(b3),
				'hr'	:	int(hr),
				'rbi'	:	int(rbi),
				'sb'	:	int(sb),
				'cs'	:	int(cs),
				'bb'	:	int(bb),
				'so'	:	int(so),
				'avg'	:	float(avg),
				'obp'	:	float(obp),
				'slg'	:	float(slg),
				'ops'	:	float(ops),
				'rc'	:	0,
				'rc27'	:	0,
				'isop'	:	0,
				'seca'	:	0,
				'gb'	:	0,
				'fb'	:	0,
				'g2f'	:	0,
				'ab2hr'	:	0,
				'bb2pa'	:	0,
				'bb2k'	:	0,
				'gp'	:	0,
				'tpa'	:	0,
				'pit'	:	0,
				'p2pa'	:	0,
				'tb'	:	0,
				'xbh'	:	0,
				'hbp'	:	0,
				'gdp'	:	0,
				'sh'	:	0,
				'sf'	:	0,
				'score'	:	0
			}

	def __eq__(self, other):
		return self.statDict['name'] == other.getStat('name') and self.statDict['team'] == other.getStat('team') 
	
	def __ne__(self, other):
		return self.statDict['name'] != other.getStat('name') or self.statDict['team'] != other.getStat('team') 

	def calculateScore(self):
		r = 1
	        h = 1
	        b2 = 2
	        b3 = 3
	        hr = 4
	        rbi = 1
	        sb = 2
	        cs = -1
	        bb = 1

		self.statDict['score']= self.statDict['r']*r + self.statDict['h']*h + self.statDict['b2']*b2 + self.statDict['b3']*b3 + self.statDict['hr']*hr + self.statDict['rbi']*rbi + self.statDict['sb']*sb + self.statDict['cs']*cs + self.statDict['bb']*bb 

	def addSaberData(self, rc, rc27, isop, seca, gb, fb, g2f, ab2hr, bb2pa, bb2k):
		self.statDict['rc']= float(rc)
		self.statDict['rc27']= float(rc27)
		self.statDict['isop']= float(isop)
		self.statDict['seca']= float(seca)
		self.statDict['gb']= int(gb)
		self.statDict['fb']= int(fb)
		self.statDict['g2f']= float(g2f)
		self.statDict['ab2hr']= float(ab2hr)
		self.statDict['bb2pa']= float(bb2pa)
		self.statDict['bb2k']= float(bb2k)

	def addExpandedData(self, gp, tpa, pit, p2pa, tb, xbh, hbp, ibb, gdp, sh, sf):
		self.statDict['gp']= int(gp)
		self.statDict['tpa']= int(tpa)
		self.statDict['pit']= int(pit)
		self.statDict['p2pa']= float(p2pa)
		self.statDict['tb']= int(tb)
		self.statDict['xbh']= int(xbh)
		self.statDict['hbp']= int(hbp)
		self.statDict['ibb']= int(ibb)
		self.statDict['gdp']= int(gdp)
		self.statDict['sh']= int(sh)
		self.statDict['sf']= int(sf)

	def getStat(self, stat):
		return self.statDict[stat]

	def hasData(self):
		for stat in self.mainStats:
			if self.statDict[stat] != 0:
				return True

		return False

	def toString(self):
                playerString = ""
		if len(self.statDict['name']) > 15:
                    playerString = playerString + self.statDict['name'] + "\t\t"
                    for key in self.mainStats:
                    	playerString = playerString + str(self.statDict[key]) + "\t"
		else:
		    playerString = playerString + self.statDict['name'] + "\t\t\t"
                    for key in self.mainStats:
                    	playerString = playerString + str(self.statDict[key]) + "\t"
		return playerString

	def toCSV(self):
                playerString = ""

                for key in self.statDict:
                    playerString = playerString + str(self.statDict[key]) + ","

                return playerString[:-1]
