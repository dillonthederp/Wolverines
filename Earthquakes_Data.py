'''
This program takes a cleaned up earthquakes dataset of earthquakes 2.5 magnitude and greater and stores the necessary
columns into lists for combined use with the wells dataset.
'''
import csv
from collections import defaultdict

columns = defaultdict(list)

"""
For each row in the data, this appends the elements of a row to their respective columns.
"""
with open('Earthquakes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

'''
This formats the times in the time column i.e. 2009-11-02T03:16:45.290Z becomes 2009. This also
gives the total number of earthquakes of 2.5 magnitude or greater for the given year in the if-statement
condition check.
'''
counter = 0
times = []
for time in columns['time']:
    s = time.split("-")
    times.append(int(s[0]))
    if int(s[0]) == 2015:
        counter += 1

print counter

"""
This sets latitude, longitude, and magnitude equal to those columns from the dataset.
"""
latitude = columns['latitude']
longitude = columns['longitude']
magnitude = columns['mag']
# print latitude
# print longitude
# print magnitude
# print times
