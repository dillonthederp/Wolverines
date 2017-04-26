# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 13:37:55 2017
basemap available at: https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/
@author: Jonathan Hunt
"""
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict as dd

lon = [] #Well longitude
lat = [] #Well latitude
"""
for i in range(6): #Loops through 7 csv files
    with open("wells"+str(i+1)+".csv", "rb") as csvfile: #Get wells data
        dataset = csv.DictReader(csvfile)
        for row in dataset: #Iterate through dataset
            if (float(row["Longitude"]) > -103 and float(row["Longitude"]) < -94 and float(row["Latitude"]) < 41 and float(row["Latitude"] > 36)):# Constrain by well type and location
                if(row["Type"] == "Injection Well" and row["State"]=="KS"):
                    lon.append(float(row["Longitude"]))
                    lat.append(float(row["Latitude"]))
               """     
with open("wellsKS.csv", "rb") as csvfile: #Get wells data
    dataset = csv.DictReader(csvfile)
    for row in dataset: #Iterate through dataset
        if (row["Type"]=="Injection Well"):
                lon.append(float(row["Longitude"]))
                lat.append(float(row["Latitude"]))
eqlon = [] #Earthquake longitude
eqlat = [] #Earthquake latitude
with open ("KansasQuakes.csv", "rb") as csvfile: #Get earthquake data
    data = csv.DictReader(csvfile)
    for row in data:
        eqlon.append(float(row["longitude"]))
        eqlat.append(float(row["latitude"]))

### Create the map ###
my_map = Basemap(projection='merc', 
                 lat_0=50, lon_0=-100, #Set view angle
              resolution='h', area_thresh=1000.0,
               llcrnrlon=-103, llcrnrlat=36, urcrnrlon=-94, urcrnrlat=41) #Set boundaries of zoom

### Add attributes to the map ###
my_map.drawcounties()
my_map.drawrivers()
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawstates()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))
ex,ey = my_map(eqlon, eqlat)
x,y = my_map(lon, lat)
my_map.plot(x, y, 'bo', markersize=2)
my_map.plot(ex, ey, 'bo', markersize=3, c="yellow")
plt.show()
"""
x = np.arange(0, 5, .1);
y = np.sin(x)
x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]
"""
#plt.plot(x,y)
#plt.scatter(lon,lat)