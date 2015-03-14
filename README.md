# Baseball Stats 
Uses python to gather baseball stats and compare them.

# How To Use
First, you have to run dataUpdater.py on at least two different days. This will save a file in playerData/battingDataFile_yyyy-mo-dd for batters and playerData/pitchingDataFile_yyyy-mo-dd for pitchers.
Once you have data for the current day, you can use battingStats.py and pitchingStats.py to see the statistics from the previous day's games.
Usage:

python battingStats.py ab

This will list all the batters sorted by the number of at bats they had.


python battingStats.py h 10

This will list the top ten batters in the hits category.


python pitchingStats.py tbf -10

This will list the ten pitchers who faced the fewest number of batters.


Once you have batting or pitcher data for more than one day, you can see who moved positions from the first day to the second day.
Usage:

python comparePitchingData.py 2015-03-02 2015-03-03


This would show how pitchers moved in their ranks from March 2, 2015 to March 3, 2015.

For myself, I run all these on a server I have running in my home. It runs dataUpdater.py every morning at 4:00am to get the data from the previous day's games, and then it runs runner.py after that.

runner.py runs the compare program on every statistic over the last two days' data and prints it. If you supply an email address as an argument, it will send the results to that address. 
