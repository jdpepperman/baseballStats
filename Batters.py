class Batters:
	def __init__(self):
		self.batters = []

	def __iter__(self):
		return iter(self.batters)

	def __getitem__(self, key):
		return self.batters[key]

	def __len__(self):
		return len(self.batters)

	def addPlayer(self, batter):
		self.batters.append(batter)

	def hasPlayer(self, playerName):
		for p in self.batters:
			if p.name == playerName:
				return True

	def calculateScores(self):
		r = 1
		h = 1
		b2 = 2
		b3 = 3
		hr = 4
		rbi = 1
		sb = 2
		cs = -1
		bb = 1
		
		for player in self.batters:
			player.score = player.r*r + player.h*h + player.b2*b2 + player.b3*b3 + player.hr*hr + player.rbi*rbi + player.sb*sb + player.cs*cs + player.bb*bb

	def getPlayer(self, playerName):
		for player in self.batters:
			if player.name == playerName:
				return player

	def sortBy(self, index):
		self.index = index
		if index == 'score':
			self.batters.sort(key=lambda x: x.score, reverse=True)
		elif index == 'ab':
			self.batters.sort(key=lambda x: x.ab, reverse=True)
		elif index == 'r':
			self.batters.sort(key=lambda x: x.r, reverse=True)
		elif index == 'h':
			self.batters.sort(key=lambda x: x.h, reverse=True)
		elif index == '2b':
			self.batters.sort(key=lambda x: x.b2, reverse=True)
		elif index == '3b':
			self.batters.sort(key=lambda x: x.b3, reverse=True)
		elif index == 'hr':
			self.batters.sort(key=lambda x: x.hr, reverse=True)
		elif index == 'rbi':
			self.batters.sort(key=lambda x: x.rbi, reverse=True)
		elif index == 'sb':
			self.batters.sort(key=lambda x: x.sb, reverse=True)
		elif index == 'cs':
			self.batters.sort(key=lambda x: x.cs, reverse=True)
		elif index == 'bb':
			self.batters.sort(key=lambda x: x.bb, reverse=True)
		elif index == 'so':
			self.batters.sort(key=lambda x: x.so, reverse=True)
		elif index == 'avg':
			self.batters.sort(key=lambda x: x.avg, reverse=True)
		elif index == 'obp':
			self.batters.sort(key=lambda x: x.obp, reverse=True)
		elif index == 'slg':
			self.batters.sort(key=lambda x: x.slg, reverse=True)
		elif index == 'war':
			self.batters.sort(key=lambda x: x.war, reverse=True)
		elif index == 'gp':
			self.batters.sort(key=lambda x: x.gp, reverse=True)
		elif index == 'tpa':
			self.batters.sort(key=lambda x: x.tpa, reverse=True)
		elif index == 'pit':
			self.batters.sort(key=lambda x: x.pit, reverse=True)
		elif index == 'p2pa':
			self.batters.sort(key=lambda x: x.p2pa, reverse=True)
		elif index == 'tb':
			self.batters.sort(key=lambda x: x.tb, reverse=True)
		elif index == 'xbh':
			self.batters.sort(key=lambda x: x.xbh, reverse=True)
		elif index == 'hbp':
			self.batters.sort(key=lambda x: x.hbp, reverse=True)
		elif index == 'ibb':
			self.batters.sort(key=lambda x: x.ibb, reverse=True)
		elif index == 'gdp':
			self.batters.sort(key=lambda x: x.gdp, reverse=True)
		elif index == 'sh':
			self.batters.sort(key=lambda x: x.sh, reverse=True)
		elif index == 'sf':
			self.batters.sort(key=lambda x: x.sf, reverse=True)
		elif index == 'rc':
			self.batters.sort(key=lambda x: x.rc, reverse=True)
		elif index == 'rc27':
			self.batters.sort(key=lambda x: x.rc27, reverse=True)
		elif index == 'isop':
			self.batters.sort(key=lambda x: x.isop, reverse=True)
		elif index == 'seca':
			self.batters.sort(key=lambda x: x.seca, reverse=True)
		elif index == 'gb':
			self.batters.sort(key=lambda x: x.gb, reverse=True)
		elif index == 'fb':
			self.batters.sort(key=lambda x: x.fb, reverse=True)
		elif index == 'g2f':
			self.batters.sort(key=lambda x: x.g2f, reverse=True)
		elif index == 'ab2hr':
			self.batters.sort(key=lambda x: x.ab2hr, reverse=True)
		elif index == 'bb2pa':
			self.batters.sort(key=lambda x: x.bb2pa, reverse=True)
		elif index == 'bb2k':
			self.batters.sort(key=lambda x: x.bb2k, reverse=True)
		else:
			pass

	def toString(self):
		battersString = ""
		for batter in self.batters:
			batterString = batterString + batter.toString() + '\n'
		return batterString
