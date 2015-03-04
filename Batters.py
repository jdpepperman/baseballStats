#Joshua Pepperman

class Batters:
	def __init__(self):
		self.batters = []

	def __iter__(self):
		return iter(self.batters)

	def __getitem__(self, key):
		return self.batters[key]

	def __len__(self):
		return len(self.batters)

	def indexOf(self, player):
		index = 0
		for p in self.batters:
			if p == player:
				return index
			else:
				index = index + 1
		return -1

	def addBatter(self, batter):
		self.batters.append(batter)

	def hasBatter(self, playerName):
		for p in self.batters:
			if p.getStat('name') == playerName:
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
			player.statDict['score'] = player.getStat('r')*r + player.getStat('h')*h + player.getStat('b2')*b2 + player.getStat('b3')*b3 + player.getStat('hr')*hr + player.getStat('rbi')*rbi + player.getStat('sb')*sb + player.getStat('cs')*cs + player.getStat('bb')*bb

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

	def getBatter(self, playerName):
		for player in self.batters:
			if player.getStat('name') == playerName:
				return player

	def sortBy(self, index):
		self.index = index
		self.batters.sort(key=lambda x: x.statDict[index], reverse=True)

	def toCSV(self):
		batterStringFile = "name,ab,r,h,2b,3b,hr,rbi,sb,cs,bb,so,avg,obp,slg,ops,war,score\n"
		for batter in self.batters:
			batterStringFile = batterStringFile + batter.toCSV() + '\n'
		return batterStringFile

	def toString(self):
		batterString = ""
		for batter in self.batters:
			batterString = batterString + batter.toString() + "\t" + str(batter.getStat(self.index)) + '\n'
		return batterString


	def toStringInRange(self, rang):
		batterString = ""
		for i in rang:
			batterString = batterString + self.batters[i].toString() + "\t" + str(self.batters[i].getStat(self.index)) + '\n'
		return batterString
