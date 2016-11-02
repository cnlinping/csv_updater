#python 3.5
#update csv

import csv

with open('/Users/linping/Documents/git/csv_updater/s.csv') as f:
    f_csv = csv.DictReader(f)
    records = []
    for row in f_csv:
	    print(row)
	    records.append(row)
