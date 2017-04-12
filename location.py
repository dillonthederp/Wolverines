# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 13:37:55 2017

@author: pbair
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

with open("wells1.csv", "rb") as csvfile:
    read = csv.reader(csvfile, delimiter' ', quotechar='|')
    for row in read:
        print ','.join(row)
        
    

x = np.arange(0, 5, .1);

y = np.sin(x)

x = [1,2,3,3,5,6,7,3,9]
y = [1,3,4,2,7,8,9,5,4]

#plt.plot(x,y)
plt.scatter(x,y)
