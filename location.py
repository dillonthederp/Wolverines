# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 13:37:55 2017
basemap available at: https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/
@author: Jonathan Hunt, Dillon Fitzgerald, Ryan Vreeland
"""
### Basemap API: http://matplotlib.org/basemap/api/basemap_api.html
### Download: https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/
from mpl_toolkits.basemap import Basemap
############################################

import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict as dd

lon = [] #Well longitude
lat = [] #Well latitude
    
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
        if (float(row["mag"]) >= 3.5): #Filter by magnitude. Change "mag" to another field in the csv to filter by that.
            eqlon.append(float(row["longitude"]))
            eqlat.append(float(row["latitude"]))

### Create the map ###
my_map = Basemap(projection='merc', 
                 lat_0=50, lon_0=-100, #Set view angle
              resolution='h', area_thresh=1000.0,
               llcrnrlon=-103, llcrnrlat=36, urcrnrlon=-94, urcrnrlat=41) #Set boundaries of zoom
                 #llcrnr = "lowerleft corner"
                 #urcrnr = "upper-right corner"
                 
### Add attributes to the map ###
my_map.drawcounties() #Draws outline of counties
my_map.drawrivers() #Draws rivers
my_map.drawcoastlines() #Draws coastlines
my_map.drawcountries() #Draws outline of countries
my_map.drawstates() #Draws outline of states
my_map.fillcontinents(color='coral') #Fills continents with color
my_map.drawmapboundary() #Draws outline of globe (only visible if you zoom way out)
my_map.drawmeridians(np.arange(0, 360, 30)) #Draw longitude lines
my_map.drawparallels(np.arange(-90, 90, 30)) #Draw latitude lines
ex,ey = my_map(eqlon, eqlat) #Translate lon,lat coordinates to map coordinates (accounting for curvature?)
x,y = my_map(lon, lat) #Translate lon,lat coordinates to map coordinates (accounting for curvature?)
my_map.plot(x, y, 'bo', markersize=2)
my_map.plot(ex, ey, 'bo', markersize=3, c="yellow")
plt.rcParams["figure.figsize"] = [40,10]    #Change size of the figure. Second parameter doesn't matter.
                                            #The figure will maintain aspect ratio and scale up with the first parameter as necessary.
plt.show() #Show the figure
"""
x = np.arange(0, 5, .1);
y = np.sin(x)
x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]
"""
#plt.plot(x,y)
#plt.scatter(lon,lat)