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

lon = []
lat = []
for i in range(6):
    with open("wells"+str(i+1)+".csv", "rb") as csvfile:
        dataset = csv.DictReader(csvfile)
        for row in dataset:
            if (float(row["Longitude"]) > -130 and float(row["Longitude"]) < -40 and float(row["Latitude"]) < 50):
                lon.append(float(row["Longitude"]))
                lat.append(float(row["Latitude"]))

### Create the map ###
my_map = Basemap(projection='merc', lat_0=50, lon_0=-100,
              resolution='l', area_thresh=1000.0,
               llcrnrlon=-130, llcrnrlat=24, urcrnrlon=-62, urcrnrlat=50)

### Add attributes to the map ###
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawstates()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

x,y = my_map(lon, lat)
my_map.plot(x, y, 'bo', markersize=5)
 
plt.show()
"""
x = np.arange(0, 5, .1);
y = np.sin(x)
x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]
"""
#plt.plot(x,y)
#plt.scatter(lon,lat)