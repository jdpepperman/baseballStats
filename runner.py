import os
import subprocess
import datetime
from datetime import timedelta

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
dayBeforeYesterday = yesterday - timedelta(days=1)

output = "BATTING DATA\n\n"

for stat in battingStats:
	command = "python /home/joshua/programming/baseball/compareBattingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + process.stdout.read() + "\n"

output = output + "\nPITCHING DATA\n\n"
for stat in pitchingStats:
	command = "python /home/joshua/programming/baseball/comparePitchingData.py " + dayBeforeYesterday.strftime("%Y-%m-%d")  + " " + yesterday.strftime("%Y-%m-%d") + " " + stat

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = output + process.stdout.read() + "\n"


os.system("echo \"" + output + "\" | mail -s \"Baseball Statistics Changes From " + dayBeforeYesterday.strftime("%Y-%m-%d") + " to " + yesterday.strftime("%Y-%m-%d") + "\" joshuapepperman@gmail.com")
