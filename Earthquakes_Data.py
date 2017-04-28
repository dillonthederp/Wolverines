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
with open('KansasQuakes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

'''
This formats the times in the time column i.e. 2009-11-02T03:16:45.290Z becomes 2009. This also
counts the number of earthquakes before 2013 and after the start of 2013 within the two if-statements.
'''
counter1 = 0
counter2 = 0
times = []
for time in columns['time']:
    s = time.split("-")
    times.append(int(s[0]))
    if int(s[0]) < 2013:
        counter1 += 1
    elif int(s[0]) >= 2013:
        counter2 += 1

"""
This iterates through the magnitude column in the dataset and first counts the number of earthquakes
pre-2013 with magnitude greater than 4.0 (or whatever the condition is changed to) and then counts
the number of earthquakes after the start of 2013 greater than with magnitude 4.0. Then the number of
total earthquakes pre and post the start of 2013 is printed out followed by the number of earthquakes
for both time periods that were greater than the given magnitudes in the if-statement conditions.
"""
magQuakes1 = 0
magQuakes2 = 0
Counter = 0
for mag in columns['mag']:
    if Counter < counter1:
        if float(mag) > 4.0:
            magQuakes1 += 1
    if Counter > counter1:
        if float(mag) > 4.0:
            magQuakes2 += 1
    Counter += 1

print("Earthquakes before 2013: " + str(counter1))
print("Earthquakes after/in 2013: " + str(counter2))
print("Earthquakes >4.0 magnitude before 2013: " + str(magQuakes1))
print("Earthquakes >4.0 magnitude after/in 2013: " + str(magQuakes2))


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