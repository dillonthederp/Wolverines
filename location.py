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
i=str(input("Enter values manually? (y/n) ")) #User choice
while i is not "y" or "n":
    i=input("Enter values manually? (y/n) ")
if (i=="n"):
    l=2000
    u=2012
    el=2000
    eu=2012
elif (i=="y"):
    l=int(input("Enter the lower bound year for well spud date: ")) #Lower bound year for wells
    u=int(input("Enter the upper bound year for well spud date: ")) #Upper bound year for wells
    el=int(input("Enter the lower bound year for earthquakes: ")) #Lower bound year for earthquakes
    eu=int(input("Enter the upper bound year for earthquakes: ")) #Upper bound year for earthquakes

with open("wellsKS.csv", "rb") as csvfile: #Get wells data
    dataset = csv.DictReader(csvfile)
    print "Reading Wells data..."
    for row in dataset: #Iterate through dataset
        if (row["Type"]=="Injection Well"): #Only gets injection wells
            ### This makes sure the date is between the lower and upper bounds ###
            if (l<float(row["Spud Date"][-4:]) <= u): #Checks if date is in desired range
                lon.append(float(row["Longitude"])) #Add the longitude of the well to list lon
                lat.append(float(row["Latitude"])) #Add the latidude of the well to list lat
eqlon = [] #Earthquake longitude
eqlat = [] #Earthquake latitude
eqmag= [] #Earthquake magnitude
with open ("KansasQuakes.csv", "rb") as csvfile: #Get earthquake data
    data = csv.DictReader(csvfile)
    print "Reading Earthquake data..."
    for row in data:
        if (float(row["mag"]) >= 0 and eu >= float(row["time"][:4]) > el): #Filter by magnitude and time
                                                                        #The the right side of the if-statement 
                                                                        #checks if the time is in desired range
            eqlon.append(float(row["longitude"])) #Add the longitude of the quake to the list eqlon
            eqlat.append(float(row["latitude"])) #Add the latitude of the quake to the list eqlat
            eqmag.append(float(row["mag"]))
### Create the map ###
print "Creating Basemap..."
my_map = Basemap(projection='merc', 
                 lat_0=50, lon_0=-100, #Set view angle
              resolution='h', area_thresh=1000.0,
               llcrnrlon=-102.3, llcrnrlat=36.5, urcrnrlon=-94.2, urcrnrlat=40.4) #Set boundaries of zoom
                 #llcrnr = "lowerleft corner"
                 #urcrnr = "upper-right corner"
                 
### Add attributes to the map ###
print "Drawing outlines and rivers..."
my_map.drawcounties() #Draws outline of counties
my_map.drawrivers() #Draws rivers
my_map.drawcoastlines() #Draws coastlines
my_map.drawcountries() #Draws outline of countries
my_map.drawstates(3) #Draws outline of states
my_map.fillcontinents(color='coral') #Fills continents with color
my_map.drawmapboundary() #Draws outline of globe (only visible if you zoom way out)

print "Drawing lat/lon lines..."
my_map.drawmeridians(np.arange(0, 360, 30)) #Draw longitude lines
my_map.drawparallels(np.arange(-90, 90, 30)) #Draw latitude lines

print "Converting Coordinates..."
x,y = my_map(lon, lat) #Translate lon,lat coordinates to map coordinates (accounting for curvature?)

print "Plotting wells..."
my_map.plot(x, y, 'bo', markersize=2) #Plot well locations

print "Plotting earthquakes..."
min_marker_size = 2.5 #Smallest size the marker can be
### This for-loop sizes the earthquake points based on magnitude ###
for lons, lats, mag in zip(eqlon, eqlat, eqmag): #Notice this for-loop plots each point individually as its size is calculated
    ex,ey = my_map(lons, lats) #Translate lon,lat coordinates to map coordinates (accounting for curvature?)
    msize = mag*mag * min_marker_size # msize is the size the markers will be. Notice the formula used to calculate it.
    my_map.plot(ex, ey, 'ro', markersize=msize, c="yellow") #Plot earthquake location

#my_map.plot(ex, ey, 'bo', markersize=5, c="yellow") #Plot earthquake locations
plt.rcParams["figure.figsize"] = [20,10]    #Change size of the figure. Second parameter doesn't matter.
                                            #The figure will maintain aspect ratio and scale up with the first parameter as necessary.
print "ALL DONE!"
print "Wells from "+str(l)+"-"+str(u)+": " + str(len(lon)) #Prints time window and how many wells were created within it.
plt.show() #Show the figure
"""
x = np.arange(0, 5, .1);
y = np.sin(x)
x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]
"""
#plt.plot(x,y)
#plt.scatter(lon,lat)