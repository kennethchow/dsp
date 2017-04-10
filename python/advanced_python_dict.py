import csv
import re 
from itertools import islice


with open('/Users/RGD/ds/metis/metisgh/dsp/python/faculty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    faculty_dict = {rows[0]:[rows[1],rows[2],rows[3]] for rows in reader}

def first_no(n, iterable): # Return first n items of the iterable as a list
    return list(islice(iterable, n))

print(first_no(3, faculty_dict.items()))


with open('faculty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    professor_dict = {}
    for rows in reader:
    	if len(rows[0].split(' ')) == 1:
    		professor_dict.update({(rows[0].split(' ', 1)[0]):[rows[1],rows[2],rows[3]]})
    	if len(rows[0].split(' ')) == 2:
    		professor_dict.update({(rows[0].split(' ', 1)[0], rows[0].split(' ', 2)[1]):[rows[1],rows[2],rows[3]]})
    	if len(rows[0].split(' ')) == 3:
    		professor_dict.update({(rows[0].split(' ', 1)[0], rows[0].split(' ', 3)[2]):[rows[1],rows[2],rows[3]]})

print(first_no(3, professor_dict.items()))

with open('faculty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    professor_dict = {}
    for rows in reader:
    	if len(rows[0].split(' ')) == 1:
    		professor_dict.update({(rows[0].split(' ', 1)[0]):[rows[1],rows[2],rows[3]]})
    	if len(rows[0].split(' ')) == 2:
    		professor_dict.update({(rows[0].split(' ', 2)[1], rows[0].split(' ', 1)[0]):[rows[1],rows[2],rows[3]]})
    	if len(rows[0].split(' ')) == 3:
    		professor_dict.update({(rows[0].split(' ', 3)[2], rows[0].split(' ', 1)[0]):[rows[1],rows[2],rows[3]]})

for key in sorted(professor_dict.keys(), key = lambda t:t[-1]):
    print ("%s: %s" % (key, professor_dict[key]))
