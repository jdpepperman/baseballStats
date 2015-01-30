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

	def addSaberData(self, rc, rc27, isop, seca, gb, fb, g2f, ab2hr, bb2pa, bb2k):
		self.rc = float(rc)
		self.rc27 = float(rc27)
		self.isop = float(isop)
		self.seca = float(seca)
		self.gb = int(gb)
		self.fb = int(fb)
		self.g2f = float(g2f)
		self.ab2hr = float(ab2hr)
		self.bb2pa = float(bb2pa)
		self.bb2k = float(bb2k)

	def addExpandedData(self, gp, tpa, pit, p2pa, tb, xbh, hbp, ibb, gdp, sh, sf):
		self.gp = int(gp)
		self.tpa = int(tpa)
		self.pit = int(pit)
		self.p2pa = float(p2pa)
		self.tb = int(tb)
		self.xbh = int(xbh)
		self.hbp = int(hbp)
		self.ibb = int(ibb)
		self.gdp = int(gdp)
		self.sh = int(sh)
		self.sf = int(sf)

	def hasData(self):
		if self.ab != 0: 
			return True
		elif self.r != 0: 
			return True
		elif self.h != 0: 
			return True
		elif self.b2 != 0: 
			return True
		elif self.b3 != 0: 
			return True
		elif self.hr != 0: 
			return True
		elif self.rbi != 0: 
			return True
		elif self.sb != 0: 
			return True
		elif self.cs != 0: 
			return True
		elif self.bb != 0: 
			return True
		elif self.so != 0: 
			return True
		elif self.avg != 0: 
			return True
		elif self.obp != 0: 
			return True
		elif self.slg != 0: 
			return True
		elif self.ops != 0: 
			return True
		elif self.war != 0: 
			return True
		else:
			return False

	def toString(self):
#		statString = "NAME\tAB\tR\tH\t2B\t3B\tHR\tRBI\tSB\tCS\tBB\tSO\tAVG\tOBP\tSLG\tOPS\tWAR"
		if len(self.name) > 15:
			playerString = self.name + "\t\t" + str(self.ab) + "\t" + str(self.r) + "\t" + str(self.h) + "\t" + str(self.b2) + "\t" + str(self.b3) + "\t" + str(self.hr) + "\t" + str(self.rbi) + "\t" + str(self.sb) + "\t" + str(self.cs) + "\t" + str(self.bb) + "\t" + str(self.so) + "\t" + str(self.avg) + "\t" + str(self.obp) + "\t" + str(self.slg) + "\t" + str(self.ops) + "\t" + str(self.war) + "\t" + str(self.score)
		else:
			playerString = self.name + "\t\t\t" + str(self.ab) + "\t" + str(self.r) + "\t" + str(self.h) + "\t" + str(self.b2) + "\t" + str(self.b3) + "\t" + str(self.hr) + "\t" + str(self.rbi) + "\t" + str(self.sb) + "\t" + str(self.cs) + "\t" + str(self.bb) + "\t" + str(self.so) + "\t" + str(self.avg) + "\t" + str(self.obp) + "\t" + str(self.slg) + "\t" + str(self.ops) + "\t" + str(self.war) + "\t" + str(self.score)
			
		return playerString
