# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 13:37:55 2017

@author: pbair
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
lon = []
lat = []
for i in range(6):
    with open("wells"+str(i+1)+".csv", "rb") as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            lon.append(row["Longitude"])
            lat.append(row["Latitude"])

x = np.arange(0, 5, .1);

y = np.sin(x)

x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]

#plt.plot(x,y)
plt.scatter(lon,lat)
