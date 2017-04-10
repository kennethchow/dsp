import csv

reader = csv.reader(open('/Users/RGD/ds/metis/metisgh/dsp/python/faculty.csv'), skipinitialspace=True)
reader.__next__()

emails = []

for r in reader:
	emails.append(r[3])

with open("emails.csv",'w', newline='') as emailcsv:
    wr = csv.writer(emailcsv, delimiter=',')
    for email in emails:
    	wr.writerow([email])