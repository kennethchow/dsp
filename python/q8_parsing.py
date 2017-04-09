# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

reader = csv.reader(open('/Users/RGD/ds/metis/metisgh/untitled folder/dsp/python/football.csv'), skipinitialspace=True)
reader.__next__()
difference = 10
smallest = "Team"

for r in reader:
    if abs(int(r[5])-int(r[6])) < difference:
    	difference = abs(int(r[5])-int(r[6]))
    	smallest = r[0]

print(smallest)