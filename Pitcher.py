class Pitcher:
	def __init__(self, name, team, gp, gs, ip, h, r, er, bb, so, w, l, sv, blsv, war, whip, era):
                self.mainStats = ['gp','gs','ip','h','r','er','bb','so','w','l','sv','blsv','war','whip','era','hld']
		self.statDict = {
				'name'	:	name,
				'team'	:	team,
                                'score' :       0,
                                'gp'    :       gp,
                                'gs'    :       gs,
                                'ip'    :       ip,
                                'h'     :       h,
                                'r'     :       r,
                                'er'    :       er,
                                'bb'    :       bb,
                                'so'    :       so,
                                'w'     :       w,
                                'l'     :       l,
                                'sv'    :       sv,
                                'blsv'  :       blsv,
                                'war'   :       war,
                                'whip'  :       whip,
                                'era'   :       era,
                                'hld'   :       0,
                                'cg'    :       0,
                                'sho'   :       0,
                                'tbf'   :       0,
                                'gf'    :       0,
                                'svo'   :       0,
                                'sh'    :       0,
                                'sf'    :       0,
                                'hbp'   :       0,
                                'gdp'   :       0,
                                'wp'    :       0,
                                'bk'    :       0,
                                'qs'    :       0,
                                'qsp'   :       0.0,
                                'k2bb'  :       0.0,
                                'k29'   :       0.0,
                                'pit'   :       0,
                                'p2pa'  :       0.0,
                                'p2ip'  :       0.0,
                                'wp'    :       0.0,
                                'ags'   :       0.0,
                                'gb'    :       0,
                                'fb'    :       0,
                                'g2f'   :       0.0,
                                'rs'    :       0.0,
                                'erc'   :       0,
                                'ercr'  :       0,
                                'dips'  :       0,
                                'dipr'  :       0,
                                'tloss' :       0,
                                'cwin'  :       0,
                                'pfr'   :       0,
                                'babip' :       0,
                                'obtb'  :       0,
                                'obb2'  :       0,
                                'obb3'  :       0,
                                'obhr'  :       0,
                                'obrbi' :       0,
                                'opibb' :       0,
                                'obsb'  :       0,
                                'obcs'  :       0,
                                'obcsp' :       0,
                                'obbaa' :       0,
                                'obobp' :       0,
                                'obslg' :       0,
                                'obops' :       0
			}
            

	def __eq__(self, other):
		return self.statDict['name'] == other.getStat('name') and self.statDict['team'] == other.getStat('team') 
	
	def __ne__(self, other):
		return self.statDict['name'] != other.getStat('name') or self.statDict['team'] != other.getStat('team') 

	def calculateScore(self):
                w = 7
                l = -3
                k = 1
                er = -1
                hld = 2
                sv = 5
                blsv = -3

		self.statDict['score'] = self.statDict['w']*w + self.statDict['l']*l + self.statDict['k']*k + self.statDict['er']*er + self.statDict['hld']*hld + self.statDict['sv']*sv + self.statDict['blsv']*blsv 

	def addSaberData(self, erc, ercr, dips, dipr, tloss, cwin, pfr, babip, k29):
		self.statDict['erc']= float(erc)
		self.statDict['ercr']= float(ercr)
		self.statDict['dips']= float(dips)
		self.statDict['dipr']= float(dipr)
		self.statDict['tloss']= int(tloss)
		self.statDict['cwin']= int(cwin)
		self.statDict['pfr']= float(pfr)
		self.statDict['babip']= float(babip)
		self.statDict['k29']= float(k29)

	def addExpandedData1(self, cg, sho, tbf, gf, svo, sh, sf, hbp, gdp, wp, bk, qs, qsp):
		self.statDict['cg']= int(cg)
		self.statDict['sho']= int(sho)
		self.statDict['tbf']= int(tbf)
		self.statDict['gf']= int(gf)
		self.statDict['svo']= int(svo)
		self.statDict['sh']= int(sh)
		self.statDict['sf']= int(sf)
		self.statDict['hbp']= int(hbp)
		self.statDict['gdp']= int(gdp)
		self.statDict['wp']= int(wp)
		self.statDict['bk']= int(bk)
		self.statDict['qs']= int(qs)
		self.statDict['qsp']= float(qsp)

        def addExpandedData2(self, k2bb, k29, pit, p2pa, p2ip, wp, ags, gb, fb, g2f, rs, whip):
		self.statDict['k2bb']= float(k2bb)
		self.statDict['k29']= float(k29)
		self.statDict['pit']= float(pit)
		self.statDict['p2pa']= float(p2pa)
		self.statDict['p2ip']= float(p2ip)
		self.statDict['wp']= float(wp)
		self.statDict['ags']= float(ags)
		self.statDict['gb']= float(gb)
		self.statDict['fb']= float(fb)
		self.statDict['g2f']= float(g2f)
		self.statDict['rs']= float(rs)

        def addOppBattingStats(self, tb, b2, b3, hr, rbi, ibb, sb, cs, csp, baa, obp, slg, ops):
		self.statDict['obtb']= int(tb)
		self.statDict['obb2']= int(b2)
		self.statDict['obb3']= int(b3)
		self.statDict['obhr']= int(hr)
		self.statDict['obrbi']= int(rbi)
		self.statDict['obibb']= int(ibb)
		self.statDict['obsb']= int(sb)
		self.statDict['obcs']= int(cs)
		self.statDict['obcsp']= float(csp)
		self.statDict['obbaa']= float(baa)
		self.statDict['obobp']= float(obp)
		self.statDict['obslg']= float(slg)
		self.statDict['obops']= float(ops)

        def addOther(self, hld):
            self.statDict['hld'] =  int(hld)


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
                    playerString = playerString + self.statDict['name']
                        for key in self.mainStats:
                            playerString = playerString + "\t\t" + self.statDict[key] + "\t"
		else:
		    playerString = playerString + self.statDict['name']
                        for key in self.mainStats:
                            playerString = playerString + "\t\t\t" + self.statDict[key] + "\t"
		return playerString

	def toCSV(self):
                playerString = ""

                for key in self.statDict:
                    playerString = playerString + self.statDict[key] + ","

                return playerString[:-1]
