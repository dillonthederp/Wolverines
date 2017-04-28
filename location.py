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

lon = [] #Well longitude
lat = [] #Well latitude

l=int(input("Well spud date lower bound (year): ")) #Lower bound year for wells
u=int(input("Well spud date upper bound (year): ")) #Upper bound year for wells
el=int(input("Earthquake year lower bound (year): ")) #Lower bound year for earthquakes
eu=int(input("Earthquake year upper bound (year): ")) #Upper bound year for earthquakes
with open("wellsKS.csv", "rb") as csvfile: #Get wells data
    dataset = csv.DictReader(csvfile)
    print "Reading Wells data..."
    for row in dataset: #Iterate through dataset
        if (row["Type"]=="Injection Well"): #Only gets injection wells
            ### This makes sure the date is between the lower and upper bounds ###
            if (l<=float(row["Spud Date"][-4:]) <= u): #Checks if date is in desired range
                lon.append(float(row["Longitude"])) #Add the longitude of the well to list lon
                lat.append(float(row["Latitude"])) #Add the latidude of the well to list lat
eqlon = [] #Earthquake longitude
eqlat = [] #Earthquake latitude
eqmag= [] #Earthquake magnitude
with open ("KansasQuakes.csv", "rb") as csvfile: #Get earthquake data
    data = csv.DictReader(csvfile)
    print "Reading Earthquake data..."
    for row in data:
        if (float(row["mag"]) >= 0 and eu >= float(row["time"][:4]) >= el): #Filter by magnitude and time
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
my_map.plot(x, y, 'bo', markersize=4) #Plot well locations

print "Plotting earthquakes..."
min_marker_size = 2.5 #Smallest size the marker can be
### This for-loop sizes the earthquake points based on magnitude ###
for lons, lats, mag in zip(eqlon, eqlat, eqmag): #Notice this for-loop plots each point individually as its size is calculated
    ex,ey = my_map(lons, lats) #Translate lon,lat coordinates to map coordinates (accounting for curvature?)
    msize = mag * (mag/2) * min_marker_size # msize is the size the markers will be. Notice the formula used to calculate it.
    my_map.plot(ex, ey, 'ro', markersize=msize, c="yellow") #Plot earthquake location

#my_map.plot(ex, ey, 'bo', markersize=5, c="yellow") #Plot earthquake locations
plt.rcParams["figure.figsize"] = [8,4]    #Change size of the figure. Second parameter doesn't matter.
                                            #The figure will maintain aspect ratio and scale up with the first parameter as necessary.
plt.title("Wells (blue) from "+str(l)+"-"+str(u)+"\n&\nEarthquakes (yellow) from "+str(el)+"-"+str(eu)+" (size indicates magnitude)")
print "Wells from "+str(l)+"-"+str(u)+": " + str(len(lon)) #Prints time window and how many wells were created within it.
print "Earthquakes from "+str(el)+"-"+str(eu)+": " + str(len(eqlon))
print "ALL DONE!"
plt.show() #Show the figure
