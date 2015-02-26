class Pitchers:
	def __init__(self):
		self.pitchers = []

	def __iter__(self):
		return iter(self.pitchers)

	def __getitem__(self, key):
		return self.pitchers[key]

	def __len__(self):
		return len(self.pitchers)

	def indexOf(self, player):
		index = 0
		for p in self.pitchers:
			if p == player:
				return index
			else:
				index = index + 1
		return -1

	def addPitcher(self, pitcher):
		self.pitchers.append(pitcher)

	def hasPitcher(self, playerName):
		for p in self.pitchers:
			if p.getStat('name') == playerName:
				return True

	def calculateScores(self):
                w = 7
                l = -3
                k = 1
                er = -1
                hld = 2
                sv = 5
                blsv = -3
                
                for pitcher in self.pitchers:
                    pitcher.statDict['score'] = pitcher.statDict['w']*w + pitcher.statDict['l']*l + pitcher.statDict['k']*k + pitcher.statDict['er']*er + pitcher.statDict['hld']*hld + pitcher.statDict['sv']*sv + pitcher.statDict['blsv']*blsv 

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

	def getPitcher(self, playerName):
		for player in self.pitchers:
			if player.getStat('name') == playerName:
				return player

	def sortBy(self, index):
		self.index = index
		self.pitchers.sort(key=lambda x: x.statDict[index], reverse=True)

	def toCSV(self):
		pitcherStringFile = "name,team,score,gp,gs,ip,h,r,er,bb,so,w,l,sv,blsv,war,whip,era,hld,cg,sho,tbf,gf,svo,sh,sf,hbp,gdp,wp,bk,qs,qsp,k2bb,k29,pit,p2pa,p2ip,wp,ags,gb,fb,g2f,rs,erc,ercr,dips,dipr,tloss,cwin,pfr,babip,obtb,obb2,obb3,obhr,obrbi,opibb,obsb,obcs,obcsp,obbaa,obobp,obslg,obops\n"

		for pitcher in self.pitchers:
			pitcherStringFile = pitcherStringFile + pitcher.toCSV() + '\n'
		return pitcherStringFile

	def toString(self):
		pitcherString = ""
		for pitcher in self.pitchers:
			pitcherString = pitcherString + pitcher.toString() + "\t" + str(pitcher.getStat(self.index)) + '\n'
		return pitcherString


	def toStringInRange(self, rang):
		pitcherString = ""
		for i in rang:
			pitcherString = pitcherString + self.pitchers[i].toString() + "\t" + str(self.pitchers[i].getStat(self.index)) + '\n'
		return pitcherString
