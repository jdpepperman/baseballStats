import os
import datetime
from datetime import timedelta

stats = ['ab','r','h','b2','b3','hr','rbi','sb','cs','bb','so','avg','obp','slg','ops','war','rc','rc27','isop','seca','gb','fb','g2f','ab2hr','bb2pa','bb2k','gp','tpa','pit','p2pa','tb','xbh','hbp','gdp','sh','sf','score']

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

for stat in stats:
	os.system("python /home/joshua/programming/baseball/compareBattingData.py " + yesterday.strftime("%Y-%m-%d")  + " " + today.strftime("%Y-%m-%d") + " " + stat + " | mail -s \"Baseball Statistics Changes From " + yesterday.strftime("%Y-%m-%d") + " to " + today.strftime("%Y-%m-%d") + "\" joshuapepperman@gmail.com")
