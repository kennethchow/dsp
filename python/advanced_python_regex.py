import csv
from collections import Counter
import re

reader = csv.reader(open('/Users/RGD/ds/metis/metisgh/dsp/python/faculty.csv'), skipinitialspace=True)
reader.__next__()
degrees = []
titles = []
emails = []
emaildomains = []
for r in reader:
	degrees.append(r[1])
	titles.append(r[2])
	emails.append(r[3])

numberofuniquedegrees = len(set(degrees))
frequencyofeachdegree = Counter(degrees)

numberofuniquetitles = len(set(titles))
frequencyofeachtitle = Counter(titles)

for domain in emails:
	domainsearch = re.search("@[\w.]+", domain)
	emaildomains.append(domainsearch.group())

uniqueemaildomains = set(emaildomains)


print("number of titles is:\n", numberofuniquetitles)

print("frequency of each title is:\n", frequencyofeachtitle)

print("number of unique degrees:\n", numberofuniquedegrees)

print("frequency of each degree:\n", frequencyofeachdegree)

print("number of unique email addresses:\n", len(uniqueemaildomains))

print("list of email domains:\n", uniqueemaildomains)