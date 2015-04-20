#Joshua Pepperman

import os
import re
import sys
import subprocess
import datetime
from datetime import timedelta

pitchingStats = ['score','gp','gs','ip','h','r','er','bb','so','w','l','sv','hld','blsv','whip','era','cg','sho','tbf','gf','svo','sh','sf','hbp','gdp','wp','bk','qs','qsp','k2bb','k29','pit','p2pa','p2ip','wper','ags','gb','fb','g2f','rs','erc','ercr','dips','dipr','tloss','cwin','pfr','babip','obtb','obb2','obb3','obhr','obrbi','obibb','obsb','obcs','obcsp','obbaa','obobp','obslg','obops']

battingStats = ['score','ab','r','h','b2','b3','hr','rbi','sb','cs','bb','so','avg','obp','slg','ops','rc','rc27','isop','seca','gb','fb','g2f','ab2hr','bb2pa','bb2k','gp','tpa','pit','p2pa','tb','xbh','hbp','gdp','sh','sf']

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
dayBeforeYesterday = yesterday - timedelta(days=1)

output = "BATTING DATA\n\n"

for stat in battingStats:
	command = "python " + os.getcwd() + "/sqlCompareBattingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	out = process.stdout.read()
	#print(out)
        output = output + out

output = output + "\nPITCHING DATA\n\n"
for stat in pitchingStats:
	command = "python " + os.getcwd() + "/sqlComparePitchingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	out = process.stdout.read()
	#print(out)
        output = output + out

if len(sys.argv) == 2 and re.match(r"[^@]+@[^@]+\.[^@]+", sys.argv[1]):
        os.system("echo \"" + output + "\" | mail -s \"Baseball Statistics Changes From " + dayBeforeYesterday.strftime("%Y-%m-%d") + " to " + yesterday.strftime("%Y-%m-%d") + "\" " + sys.argv[1])
else:
	print(output)
