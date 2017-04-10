import csv
import re

reader = csv.reader(open('/Users/RGD/ds/metis/metisgh/dsp/python/faculty.csv'), skipinitialspace=True)
reader.__next__()

names = []
details = []

for r in reader:
	names.append(r[0])
	details.append(r[1:4])

listoflastnames = sorted(names, key=lambda x: x.split(" ")[-1])

uniquelastnames = set([lastname.split()[-1] for lastname in listoflastnames])

predic = {el:0 for el in uniquelastnames}

print(len(details))
print(len(uniquelastnames))