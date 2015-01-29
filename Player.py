class Player:
	def __init__(self, name, ab, r, h, b2, b3, hr, rbi, sb, cs, bb, so, avg, obp, slg, ops, war):
		self.name = name
		self.ab = int(ab)
		self.r = int(r)
		self.h = int(h)
		self.b2 = int(b2)
		self.b3 = int(b3)
		self.hr = int(hr)
		self.rbi = int(rbi)
		self.sb = int(sb)
		self.cs = int(cs)
		self.bb = int(bb)
		self.so = int(so)
		self.avg = float(avg)
		self.obp = float(obp)
		self.slg = float(slg)
		self.ops = float(ops)
		self.war = float(war)
		self.score = 0

	def toString(self):
#		statString = "NAME\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR"
		if len(self.name) > 15:
			playerString = self.name + "\t\t" + str(self.ab) + "\t" + str(self.r) + "\t" + str(self.h) + "\t" + str(self.b2) + "\t" + str(self.b3) + "\t" + str(self.hr) + "\t" + str(self.rbi) + "\t" + str(self.sb) + "\t" + str(self.cs) + "\t" + str(self.bb) + "\t" + str(self.so) + "\t" + str(self.avg) + "\t" + str(self.obp) + "\t" + str(self.slg) + "\t" + str(self.ops) + "\t" + str(self.war) + "\t" + str(self.score)
		else:
			playerString = self.name + "\t\t\t" + str(self.ab) + "\t" + str(self.r) + "\t" + str(self.h) + "\t" + str(self.b2) + "\t" + str(self.b3) + "\t" + str(self.hr) + "\t" + str(self.rbi) + "\t" + str(self.sb) + "\t" + str(self.cs) + "\t" + str(self.bb) + "\t" + str(self.so) + "\t" + str(self.avg) + "\t" + str(self.obp) + "\t" + str(self.slg) + "\t" + str(self.ops) + "\t" + str(self.war) + "\t" + str(self.score)
			
		return playerString
