# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:50:33 2017

@author: ravreeland
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN as DBS
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin
import csv
from collections import defaultdict as dd


"""
Sample Code for K means clustering.


iris = datasets.load_iris()
dat_data = iris.data[:,2:]

km = KMeans(n_clusters = 3)
km.fit(dat_data)

centroids = km.cluster_centers_
dat_label = pairwise_distances_argmin(dat_data, centroids)
colors = ['b', 'c', 'r']

for k, col in zip(range(3), colors):
    mems = dat_label == k
    cent = centroids[k]
    plt.plot(dat_data[mems, 0], dat_data[mems, 1], 'w', markerfacecolor=col, marker='.')
    plt.plot(cent[0], cent[1], 'o', markerfacecolor=col, markersize = 16)

plt.show()
"""

"""
Goal: To find several good points to represent several wells
First Task, getting data into python and seperatting for oil, gas, injection, water injection, brine disposal wells

"""

TWD = csv.DictReader(open("wellsKS.csv")) #TWB means total well dataset

"""
Initiating arrays for each of the types I want (so i can just use those or all of them)
This also will cut down on amount of data points as well
Ignoring the dry and abandoned wells right now. want to cut down on data. Keeping track of abandoned is really only for pollution 
Using a 5th array to hold all the points together in case i want to look at all of them at once
BDW = Brine Disposal Well
OW= Oil Well
GW = Gas Well
Inj = Injection Well

this gets all the data i want, after will grab just the latitudes and longitudes
"""
BDW = []
OW = []
GW = []
INJ = []
Total = []


for well in TWD:
    if well["Type"]=="Brine Disposal Well":
        BDW.append(well)
        Total.append(well)
    elif well["Type"] == "Oil Well":
        OW.append(well)
        Total.append(well)
    elif well["Type"]== "Gas Well":
        GW.append(well)
        Total.append(well)
    elif well["Type"]== "Injection Well":
        INJ.append(well)
        Total.append(well)
    
        
"""
print "BDW: ", len(BDW) --> 4343
print "OW: ", len(OW)   --> 65510
print "GW: ", len(GW)   --> 20889
print "INJ: ", len(INJ) --> 7293
print "Total: ", len(Total) --> 98035
"""

lat_long_Data =[]
latitudes= []
longitudes = []
"""
getting the latitude and longitude data and then implementing the KMC
Storing it as a list of lat, long pairs (latidude first, then longitude)
"""

for well in Total: 
    lat_long_Data.append([float(well["Latitude"]), float(well["Longitude"])])
    latitudes.append(float(well["Latitude"]))
    longitudes.append(float(well["Longitude"]))

BDW_Cord_Data = []    
for well in BDW: 
    BDW_Cord_Data.append([float(well["Latitude"]), float(well["Longitude"])])
    latitudes.append(float(well["Latitude"]))
    longitudes.append(float(well["Longitude"]))
"""
Needed the data to be in a matrix like thing   
   
"""
Matrix_Lat_Long = np.matrix(lat_long_Data)
Matrix_BDW = np.matrix(BDW_Cord_Data)
#print "Matrix: ", Matrix_BDW


"""
Main attempt, attempt with Mean shift next.
Issue: doing heigharcal and DBS has made our memory go to 100% and crash my laptop.
trying with a smalled set, BDW
"""
"""
km = DBS(eps = 0.75, min_samples=50)
km.fit(Matrix_Lat_Long)

centroids = km.components_
dat_label = pairwise_distances_argmin(Matrix_Lat_Long, centroids)
colors = ['b', 'c', 'r', 'g', 'k','y','m','b', 'c', 'r', 'g', 'k','y','g', 'k','y']

print km.components_
"""
"""
mems-> the points in the groupings, basically goes through the matrix, and finds the lat and longitude
and plots them according to color
"""
"""
for k, col in zip(range(4), colors):
    mems = dat_label == k
    cent = centroids[k]
    plt.plot(Matrix_Lat_Long[mems, 0], Matrix_Lat_Long[mems, 1], 'w', markerfacecolor=col, marker='.')
    plt.plot(cent[0], cent[1], 'o', markerfacecolor=col, markersize = 10)
"""



"""
------------------------------------------------------------------------------------------------------------------------
Looking at example from http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html
Attempt at DBSCAN, not what I was looking for. 
"""
"""
db = DBS(eps=0.1, min_samples=10).fit(Matrix_Lat_Long)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print set(labels)

unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = Matrix_Lat_Long[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = Matrix_Lat_Long[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)


plt.show()
#end of DBSCAN attempt
----------------------------------------------------------------------------------
    
"""


#plt.show() 