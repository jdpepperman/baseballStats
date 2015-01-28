class Player:
	def __init__(self, name, ab, r, h, b2, b3, hr, rbi, sb, cs, bb, so, avg, obp, slg, ops, war):
		self.name = name
		self.ab = ab
		self.r = r
		self.h = h
		self.b2 = b2
		self.b3 = b3
		self.hr = hr
		self.rbi = rbi
		self.sb = sb
		self.cs = cs
		self.bb = bb
		self.so = so
		self.avg = avg
		self.obp = obp
		self.slg = slg
		self.ops = ops
		self.war = war

	def toString(self):
#		statString = "NAME\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR"
		if len(self.name) > 15:
			playerString = self.name + "\t\t" + self.ab + "\t" + self.r + "\t" + self.h + "\t" + self.b2 + "\t" + self.b3 + "\t" + self.hr + "\t" + self.rbi + "\t" + self.sb + "\t" + self.cs + "\t" + self.bb + "\t" + self.so + "\t" + self.avg + "\t" + self.obp + "\t" + self.slg + "\t" + self.ops + "\t" + self.war
		else:
			playerString = self.name + "\t\t\t" + self.ab + "\t" + self.r + "\t" + self.h + "\t" + self.b2 + "\t" + self.b3 + "\t" + self.hr + "\t" + self.rbi + "\t" + self.sb + "\t" + self.cs + "\t" + self.bb + "\t" + self.so + "\t" + self.avg + "\t" + self.obp + "\t" + self.slg + "\t" + self.ops + "\t" + self.war
			
		return playerString
