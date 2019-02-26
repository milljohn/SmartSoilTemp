#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:35:08 2018

@author: jmiller

1.) Read data from csv
2.) Compute max, min, average for each day
3.) Print message if average is above threshold for three days.

"""

import csv
import matplotlib.pyplot as plt

# empty dictionary for temperature data
temp = {}

"""
The csv file is opened and read, the contents are put in a dictionary.

NOTE: this file only contains data from one device. 
"""


# with statement will guarantee file closure
with open('DataCollector - DataLogger.csv', 'r') as csvfile:
    temp_reader = csv.reader(csvfile, delimiter = ',')
    
    # skip the first row of the csv
    for row in list(temp_reader)[1:]:
        key         = row[0]         # The first column with primary key 
        time        = row[1]         # Second column with date & time
        tag         = row[2]         # Third column with the MAC address
        temperature = float(row[3])  # Fourth column with temperature data
        
        
        # This ultimately builds a list for each line,
        # with the each element of the date being a list element
        # 11/23/2018 10:29:06 becomes ['11', '23', '2018', '10:29:06']
        data = time.split('/')       # Build a list by removing the '/' from the date
        data = ' '.join(data)        # Convert back to string with ' ' replacing '/'
        data = data.split(' ')       # Build the list again, separate with ' '
        data.append(temperature)     # Add the temperature data to the list
        #data.insert(0, tag)          # Add the tag (MAC address) to the list
        
        # build the date without the time stamp
        date = data[0] + '/' + data[1] + '/' + data[2]

        # dictionary with the tag (MAC address as key)
        if tag not in temp:
            temp[tag] = {}
        # dictionary with date as the key with a list of temperatures for the day
        else:
            if date not in temp[tag]:    
                temp[tag][date] = []
            else: 
                temp[tag][date] += [temperature]

"""
The temp data needs to be in a useful form, which is the daily average.
The dictionary is modified.

NOTE: This is a nested dictionary. The outer dictionary is of devices. 
The inner dictionary is of the dates with the temperature readings.
"""

# print the unmodified dictionary
print('This is the dictionary just built')
print(temp)

# tag is a dictionary of devices;
# dates is a dictionary of dates with a list of temperatures as the values.
# This updates the dictionary to a daily average
for tag, dates in temp.items():
    for date, temps in dates.items():
        # Highest and lowest temp dropped
        dates[date] = (sum(temps) - max(temps) - min(temps)) / ( len(temps) - 2 )


# print the modified dictionary with daily averages
print('This is the devices along with daily agerage temperatures')
print(temp)


"""
Graph the data and determine if desired crops should be planted.
"""
# Ideal planting temp
peas    = 30
corn    = 37
lettuce = 28

# counting variables, this is the number of consecutive days a temp is reached
peaCount     = 0
cornCount    = 0
lettuceCount = 0

# Empty dictionary that is built below
plantCrops = {}
colors = list('rgbcmyk')
count = 0

# go through dictionary, plot daily averages, build new dictionary that 
# tells if a crop is ready to plant
for tag, dates in temp.items():
    
    # Build dictionary of devices and crops
    if tag not in plantCrops: 
        plantCrops[tag] = {}
    if tag in plantCrops:
        plantCrops[tag]['plantPeas'] = False
        plantCrops[tag]['plantCorn'] = False
        plantCrops[tag]['plantLettuce'] = False
        
        # change the color for each device, up to 7 devices
        c = colors[count]
        count +=1
    # parse dictionary further to get daily averages    
    for date, temps in dates.items():
        # build scatter plot
        plt.scatter(date, temps, color = c)
        
        # if the temp is high enough for 3 days, reset count if temp drops
        if temps > peas:
            peaCount +=1
        else: peaCount = 0
       
        if temps > corn:
            cornCount +=1
        else: cornCount = 0

        if temps > lettuce:
            lettuceCount +=1
        else: lettuceCount = 0
        
        # update dictionary if the temp is high enough for 3 consecutive days
        if peaCount > 2:
            plantCrops[tag]['plantPeas'] = True
        if cornCount > 2:
            plantCrops[tag]['plantCorn'] = True
        if lettuceCount > 2:
            plantCrops[tag]['plantLettuce'] = True
        
            
# labels for x and y on plot
plt.xlabel('Date')
plt.ylabel('Average Daily Temperature')

#changes the direction of the x axis points to 45 degrees
locs, labels = plt.xticks()
plt.setp(labels, rotation=45)

# show the legend and plot everything
plt.legend(temp.keys())
plt.show()

# print dictionary of devices and if it is safe to plant each crop
print(plantCrops)

"""
Prepare to send the data to another service

print statements used in place of functions that will post the data
"""

for tag, crops in plantCrops.items():
    # send each tag
    print(tag)
    for crop, canPlant in crops.items():
        # send the crop and if it can be planted
        print (crop)
        print(canPlant)
    