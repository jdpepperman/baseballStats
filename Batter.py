#Joshua Pepperman

class Batter:
	def __init__(self, name, team, ab, r, h, b2, b3, hr, rbi, sb, cs, bb, so, avg, obp, slg, ops, war):
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
				'war'	:	float(war),
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
		if self.statDict['ab'] != 0: 
			return True
		elif self.statDict['r'] != 0: 
			return True
		elif self.statDict['h'] != 0: 
			return True
		elif self.statDict['b2'] != 0: 
			return True
		elif self.statDict['b3'] != 0: 
			return True
		elif self.statDict['hr'] != 0: 
			return True
		elif self.statDict['rbi'] != 0: 
			return True
		elif self.statDict['sb'] != 0: 
			return True
		elif self.statDict['cs'] != 0: 
			return True
		elif self.statDict['bb'] != 0: 
			return True
		elif self.statDict['so'] != 0: 
			return True
		elif self.statDict['avg'] != 0: 
			return True
		elif self.statDict['obp'] != 0: 
			return True
		elif self.statDict['slg'] != 0: 
			return True
		elif self.statDict['ops'] != 0: 
			return True
		elif self.statDict['war'] != 0: 
			return True
		else:
			return False

	def toString(self):
#		statString = "NAME\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR"
		if len(self.statDict['name']) > 15:
			playerString = self.statDict['name'] + "\t\t" + str(self.statDict['ab']) + "\t" + str(self.statDict['r']) + "\t" + str(self.statDict['h']) + "\t" + str(self.statDict['b2']) + "\t" + str(self.statDict['b3']) + "\t" + str(self.statDict['hr']) + "\t" + str(self.statDict['rbi']) + "\t" + str(self.statDict['sb']) + "\t" + str(self.statDict['cs']) + "\t" + str(self.statDict['bb']) + "\t" + str(self.statDict['so']) + "\t" + str(self.statDict['avg']) + "\t" + str(self.statDict['obp']) + "\t" + str(self.statDict['slg']) + "\t" + str(self.statDict['ops']) + "\t" + str(self.statDict['war']) + "\t" + str(self.statDict['score'])
		else:
			playerString = self.statDict['name'] + "\t\t\t" + str(self.statDict['ab']) + "\t" + str(self.statDict['r']) + "\t" + str(self.statDict['h']) + "\t" + str(self.statDict['b2']) + "\t" + str(self.statDict['b3']) + "\t" + str(self.statDict['hr']) + "\t" + str(self.statDict['rbi']) + "\t" + str(self.statDict['sb']) + "\t" + str(self.statDict['cs']) + "\t" + str(self.statDict['bb']) + "\t" + str(self.statDict['so']) + "\t" + str(self.statDict['avg']) + "\t" + str(self.statDict['obp']) + "\t" + str(self.statDict['slg']) + "\t" + str(self.statDict['ops']) + "\t" + str(self.statDict['war']) + "\t" + str(self.statDict['score'])
			
		return playerString

	def toCSV(self):
		playerString = self.statDict['name'] + "," + str(self.statDict['ab']) + "," + str(self.statDict['r']) + "," + str(self.statDict['h']) + "," + str(self.statDict['b2']) + "," + str(self.statDict['b3']) + "," + str(self.statDict['hr']) + "," + str(self.statDict['rbi']) + "," + str(self.statDict['sb']) + "," + str(self.statDict['cs']) + "," + str(self.statDict['bb']) + "," + str(self.statDict['so']) + "," + str(self.statDict['avg']) + "," + str(self.statDict['obp']) + "," + str(self.statDict['slg']) + "," + str(self.statDict['ops']) + "," + str(self.statDict['war']) + "," + str(self.statDict['score'])

                return playerString
