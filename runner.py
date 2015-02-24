import os
import subprocess
import datetime
from datetime import timedelta

stats = ['score','ab','r','h','b2','b3','hr','rbi','sb','cs','bb','so','avg','obp','slg','ops','war','rc','rc27','isop','seca','gb','fb','g2f','ab2hr','bb2pa','bb2k','gp','tpa','pit','p2pa','tb','xbh','hbp','gdp','sh','sf']

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)

output = ""

for stat in stats:
	command = "python /home/joshua/programming/baseball/compareBattingData.py " + yesterday.strftime("%Y-%m-%d")  + " " + today.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + stat + "\n" + process.stdout.read() + "\n"

os.system("echo \"" + output + "\" | mail -s \"Baseball Statistics Changes From " + yesterday.strftime("%Y-%m-%d") + " to " + today.strftime("%Y-%m-%d") + "\" joshuapepperman@gmail.com")
