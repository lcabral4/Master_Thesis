# citifile data parser/plotter, JWANG Nov 2021
# modified based on https://github.com/feph/citidata
# datalist contains all data np arrays

import citidata
import glob
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

t = []
keyslist = []       # data name
datalist = []       # data arrays
M = N = 0

all_my_files = glob.glob("*.citi")
for filename in all_my_files:
    M += 1
#   print("=== %s ===" % filename)
    citi_file = citidata.genfromfile(filename)
    for package in citi_file.packages:
#       print(package)
#       print(package.indep)
        #print(package.deps)    # suppress screen output
        for key in package.deps:
            N += 1
            value = package.deps[key]       # get data 
#           print(value)
            keyslist.append(key)            # append key
            datalist.append(value['data'])  # append np array data
#(datalist)
name_dict = {
    0: "S11 Log Magnitude",
    1: "S21 Log Magntitude",
    2: "S12 Log Magnitude",
    3: "S22 Log magnitude",
    4: "S11 Log Magnitude",
    5: "S21 Log Magntitude",
    6: "S12 Log Magnitude",
    7: "S22 Log magnitude",
    8: "S11 Log Magnitude",
    9: "S21 Log Magntitude",
    10: "S12 Log Magnitude",
    11: "S22 Log magnitude",
    12: "S11 Log Magnitude",
    13: "S21 Log Magntitude",
    14: "S12 Log Magnitude",
    15: "S22 Log magnitude",
    16: "S11 Log Magnitude",
    17: "S21 Log Magntitude",
    18: "S12 Log Magnitude",
    19: "S22 Log magnitude"
    }
#print('\n ', M, 'files read;', N, 'datasets recorded.')
#print('dataset : name')
#plt.figure(0)
w = []
x = np.linspace(8, 12, 201)
for i in range(N):
    if i == 1:
        continue
    if i == 2:
        continue
    if i ==3:
        continue
    if i == 5:
        continue
    if i == 6:
        continue
    if i == 7:
        continue
    if i == 9:
        continue
    if i == 10:
        continue
    if i == 11:
        continue
    if i == 13:
        continue
    if i == 14:
        continue
    if i == 15:
        continue
    if i == 17:
        continue
    if i == 18:
        continue
    if i == 19:
        continue
       
    fig = plt.figure(0)
#    print(i, ':', keyslist[i])
    y = datalist[i]             # data 
#    print(y)
    f = np.abs(y)
#    f = sqrt(test)
#    t.append(f)
#    w.append(f)
    mag = 20*log10(f)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz')
    plt.ylabel('Log Magnitude (dB')
    plt.plot(x, mag)
    plt.title(name_dict[i])
#print(f)
for i in range(N):
    if i == 0:
        continue
    if i == 2:
        continue
    if i ==3:
        continue
    if i == 4:
        continue
    if i == 6:
        continue
    if i == 7:
        continue
    if i == 8:
        continue
    if i == 10:
        continue
    if i == 11:
        continue
    if i == 12:
        continue
    if i == 14:
        continue
    if i == 15:
        continue
    if i == 16:
        continue
    if i == 18:
        continue
    if i == 19:
        continue
    
    
    fig = plt.figure(1)
#    print(i, ':', keyslist[i])
    y = datalist[i]             # data 
#    print(y)
    f = np.abs(y)
#    f = sqrt(test)
    mag = 20*log10(f)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz')
    plt.ylabel('Log Magnitude (dB')
    plt.plot(x, mag)
    plt.title(name_dict[i])
    
for i in range(N):
    if i == 0:
        continue
    if i == 1:
        continue
    if i ==3:
        continue
    if i == 4:
        continue
    if i == 5:
        continue
    if i == 7:
        continue
    if i == 8:
        continue
    if i == 9:
        continue
    if i == 11:
        continue
    if i == 12:
        continue
    if i == 13:
        continue
    if i == 15:
        continue
    if i == 16:
        continue
    if i == 17:
        continue
    if i == 19:
        continue
    
    
    fig = plt.figure(2)
#    print(i, ':', keyslist[i])
    y = datalist[i]             # data 
#    print(y)
    f = np.abs(y)
#    f = sqrt(test)
    mag = 20*log10(f)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz')
    plt.ylabel('Log Magnitude (dB')
    plt.plot(x, mag)
    plt.title(name_dict[i])

for i in range(N):
    if i == 0:
        continue
    if i == 1:
        continue
    if i ==2:
        continue
    if i == 4:
        continue
    if i == 5:
        continue
    if i == 6:
        continue
    if i == 8:
        continue
    if i == 9:
        continue
    if i == 10:
        continue
    if i == 12:
        continue
    if i == 13:
        continue
    if i == 14:
        continue
    if i == 16:
        continue
    if i == 17:
        continue
    if i == 18:
        continue
    
    
    fig = plt.figure(4)
#    print(i, ':', keyslist[i])
    y = datalist[i]             # data 
#    print(y)
#    test = i*conj(i)
    f = np.abs(y)
#    f = sqrt(test)
    mag = 20*log10(f)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz')
    plt.ylabel('Log Magnitude (dB')
    plt.plot(x, mag)
    plt.title(name_dict[i])
plt.show()


        
        

        
        
    

        