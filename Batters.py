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

	def getStadiumRank(self, team):
		rank = 0
		if 'WSH' in team:
			rank = 1
		elif 'TOR' in team:
			rank = 1
		elif 'TEX' in team:
			rank = 1
		elif 'TB' in team:
			rank = 1
		elif 'STL' in team:
			rank = 1
		elif 'SF' in team:
			rank = 1
		elif 'SEA' in team:
			rank = 1
		elif 'SD' in team:
			rank = 1
		elif 'PIT' in team:
			rank = 1
		elif 'PHI' in team:
			rank = 1
		elif 'OAK' in team:
			rank = 1
		elif 'NYY' in team:
			rank = 1
		elif 'NYM' in team:
			rank = 1
		elif 'MIN' in team:
			rank = 1
		elif 'MIL' in team:
			rank = 1
		elif 'MIA' in team:
			rank = 1
		elif 'LAD' in team:
			rank = 1
		elif 'LAA' in team:
			rank = 1
		elif 'KC' in team:
			rank = 1
		elif 'HOU' in team:
			rank = 1
		elif 'DET' in team:
			rank = 1
		elif 'COL' in team:
			rank = 1
		elif 'CLE' in team:
			rank = 1
		elif 'CIN' in team:
			rank = 1
		elif 'CHW' in team:
			rank = 1
		elif 'CHC' in team:
			rank = 1
		elif 'BOS' in team:
			rank = 1
		elif 'BAL' in team:
			rank = 1
		elif 'ATL' in team:
			rank = 1
		elif 'ARI' in team:
			rank = 1

	def getPlayer(self, playerName):
		for player in self.batters:
			if player.name == playerName:
				return player

	def sortBy(self, index):
		self.index = index
		if index == 'score':
			self.batters.sort(key=lambda x: x.score, reverse=True)
		elif index == 'team':
			self.batters.sort(key=lambda x: x.team, reverse=True)
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

	def toCSV(self):
		batterStringFile = "name,ab,r,h,2b,3b,hr,rbi,sb,cs,bb,so,avg,obp,slg,ops,war,score\n"
		for batter in self.batters:
			batterStringFile = batterStringFile + batter.toCSV() + '\n'
	
		return batterStringFile

	def toString(self):
		batterString = ""
		for batter in self.batters:
			if self.index == 'gp':
				batterString = batterString + batter.toString() + "\t" + str(batter.gp) + '\n'
			elif self.index == 'tpa':
				batterString = batterString + batter.toString() + "\t" + str(batter.tpa) + '\n'
			elif self.index == 'pit':
				batterString = batterString + batter.toString() + "\t" + str(batter.pit) + '\n'
			elif self.index == 'p2pa':
				batterString = batterString + batter.toString() + "\t" + str(batter.p2pa) + '\n'
			elif self.index == 'tb':
				batterString = batterString + batter.toString() + "\t" + str(batter.tb) + '\n'
			elif self.index == 'xbh':
				batterString = batterString + batter.toString() + "\t" + str(batter.xbh) + '\n'
			elif self.index == 'hbp':
				batterString = batterString + batter.toString() + "\t" + str(batter.hbp) + '\n'
			elif self.index == 'ibb':
				batterString = batterString + batter.toString() + "\t" + str(batter.ibb) + '\n'
			elif self.index == 'gdp':
				batterString = batterString + batter.toString() + "\t" + str(batter.gdp) + '\n'
			elif self.index == 'sh':
				batterString = batterString + batter.toString() + "\t" + str(batter.sh) + '\n'
			elif self.index == 'sf':
				batterString = batterString + batter.toString() + "\t" + str(batter.sf) + '\n'
			elif self.index == 'rc':
				batterString = batterString + batter.toString() + "\t" + str(batter.rc) + '\n'
			elif self.index == 'rc27':
				batterString = batterString + batter.toString() + "\t" + str(batter.rc27) + '\n'
			elif self.index == 'isop':
				batterString = batterString + batter.toString() + "\t" + str(batter.isop) + '\n'
			elif self.index == 'seca':
				batterString = batterString + batter.toString() + "\t" + str(batter.seca) + '\n'
			elif self.index == 'gb':
				batterString = batterString + batter.toString() + "\t" + str(batter.gb) + '\n'
			elif self.index == 'fb':
				batterString = batterString + batter.toString() + "\t" + str(batter.fb) + '\n'
			elif self.index == 'g2f':
				batterString = batterString + batter.toString() + "\t" + str(batter.g2f) + '\n'
			elif self.index == 'ab2hr':
				batterString = batterString + batter.toString() + "\t" + str(batter.ab2hr) + '\n'
			elif self.index == 'bb2pa':
				batterString = batterString + batter.toString() + "\t" + str(batter.bb2pa) + '\n'
			elif self.index == 'bb2k':
				batterString = batterString + batter.toString() + "\t" + str(batter.bb2k) + '\n'
			elif self.index == 'team':
				batterString = batterString + batter.toString() + "\t" + str(batter.team) + '\n'
			else:
				batterString = batterString + batter.toString() + '\n'
		return batterString


	def toStringInRange(self, rang):
		batterString = ""
		for i in rang:
			if self.index == 'gp':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].gp) + '\n'
			elif self.index == 'tpa':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].tpa) + '\n'
			elif self.index == 'pit':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].pit) + '\n'
			elif self.index == 'p2pa':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].p2pa) + '\n'
			elif self.index == 'tb':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].tb) + '\n'
			elif self.index == 'xbh':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].xbh) + '\n'
			elif self.index == 'hbp':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].hbp) + '\n'
			elif self.index == 'ibb':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].ibb) + '\n'
			elif self.index == 'gdp':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].gdp) + '\n'
			elif self.index == 'sh':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].sh) + '\n'
			elif self.index == 'sf':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].sf) + '\n'
			elif self.index == 'rc':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].rc) + '\n'
			elif self.index == 'rc27':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].rc27) + '\n'
			elif self.index == 'isop':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].isop) + '\n'
			elif self.index == 'seca':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].seca) + '\n'
			elif self.index == 'gb':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].gb) + '\n'
			elif self.index == 'fb':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].fb) + '\n'
			elif self.index == 'g2f':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].g2f) + '\n'
			elif self.index == 'ab2hr':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].ab2hr) + '\n'
			elif self.index == 'bb2pa':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].bb2pa) + '\n'
			elif self.index == 'bb2k':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].bb2k) + '\n'
			elif self.index == 'team':
				batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].team) + '\n'
			else:
				batterString = batterString + self.batters[i].toString() + '\n'
		return batterString
