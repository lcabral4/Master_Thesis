#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:40:47 2022

@author: lcabral4
"""

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
    S11 = 10**mag
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
#    plt.plot(x, mag)
    if i == 0:
        plt.plot(x, mag, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 4:
        plt.plot(x, mag, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 8:
        plt.plot(x, mag, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 12:
#        plt.plot(x, mag, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(name_dict[i])
    fig = plt.figure(11)
    SER = -10* log10(1 - np.abs(S11)**2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('SER (dB)')
    plt.title('Shielding Due To Reflection')
    SER_Tunnel = np.array([-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0])
    SER = SER - SER_Tunnel
    if i == 0:
        plt.plot(x, SER, label = 'Sample1')
#        plt.plot(x, SER_Tunnel, label = 'tunnel 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 4:
        plt.plot(x, SER, label = 'Sample2')
#        plt.plot(x, SER_Tunnel, label = 'tunnel 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 8:
        plt.plot(x, SER, label = 'Sample3')
#        plt.plot(x, SER_Tunnel, label = 'tunnel 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 12:
        plt.plot(x, SER, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, SER, label = 'Sample5')
#        plt.plot(x, SER_Tunnel, label = 'tunnel 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
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
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
    plt.title(name_dict[i])
    if i == 1:
        plt.plot(x, mag, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 5:
        plt.plot(x, mag, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 9:
        plt.plot(x, mag, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 13:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 17:
        plt.plot(x, mag, label = 'Sample5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
S2 = []    
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
#    print(mag, 'S12')
    S12 = 10**mag
    S2.append(S12)
    Total_SE = -10*log10(np.abs(S12)**2)
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
    if i == 2:
        plt.plot(x, mag, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 6:
        plt.plot(x, mag, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 10:
        plt.plot(x, mag, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 14:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, mag, label = 'Sample5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(name_dict[i])
    fig = plt.figure(9)
    plt.title('Total SE')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Total SE (dB)')
#    plt.legend((Total_SE[i]),loc='center left')
    Total_SE_Tunnel = np.array([0.26390914375, -0.6579339479999999, 1.6226839100000001, 1.2305666225, -1.9741019625, -0.6005563842499999, -1.3070515950000001, -0.331777603, 0.7461791664999999, -2.4252373599999997, -1.955666665, -0.9213228785, -0.17133898525000002, 2.1864864225, -0.29255602575, -0.8678891557499999, 0.68672696, 0.48141001549999995, 3.8097519825, 2.9681968125, -0.51790282375, 0.74989355275, -0.193993510525, 1.1024766000000001, 2.9017251225000003, -0.9557707472500001, -0.795969856, -0.6491365847499999, 0.12261888474999999, 2.7831882425000005, 0.31887973599999997, -0.97338023475, -0.5942628015, -0.59238309375, 2.338118625, 2.0947828375000004, -0.47830107075, -0.298315982, -0.46656814025000004, 1.7212786249999998, 3.8298241125, 0.85489321225, -0.289896382, -0.5826264590000001, 0.35870968225, 3.2375924375, 2.1537511225, 0.49055363525, 0.23131869900000002, 0.06574192225, 3.13040963, 3.745118105, 1.2850670124999999, 0.77479005025, -0.2437091345, 1.500555545, 3.0153963074999997, 1.7597390675, 0.900398521, -0.3917781145, -0.21279932099999999, 3.0868415450000004, 2.0028330825, 0.77925151075, -0.79875792775, -1.8253776824999999, 2.3173434475000003, 2.8061728500000003, 0.34361762225000003, -0.202710494325, -1.6636387, 1.8991293949999999, 6.4615507325, 2.9348292024999996, 1.4476410325, -0.21288281050000002, 0.002357972814999998, 7.646874605, 5.7118095475, 1.83784605, -0.55112788775, -2.1968299874999997, 6.9191321925, 8.386807525, 3.659485015, 4.1292402425, -2.9719022899999996, -0.5436238112499999, 12.1793273525, 11.2375673625, 10.863127255, 6.889262565, 3.1641643624999998, 14.4849621725, 20.064484315, 20.0155946625, 17.136160385, 6.3243602050000005, 14.044372895, 26.09010688, 24.013467285, 23.340940125, 14.394172185, 11.71979777, 22.204716400000002, 21.4766130425, 22.9404336875, 20.88531286, 9.5965489725, 14.2122796375, 20.9703241325, 21.68353177, 21.75832708, 10.766990794999998, 6.1155681225, 12.5201700925, 14.293337005, 16.2118567, 10.396434697499998, 1.14040427, 3.70810673, 8.2082760675, 11.691907180000001, 11.643677912500001, 3.2298568525, 0.9008088590000001, 4.7488944275, 7.750266524999999, 9.9958899975, 3.632858315, -2.1596030324999997, 0.039688513450000004, 3.7442547425, 6.33331538, 4.476049225, 0.144627844, 0.76808162225, 2.3208037625, 5.16979658, 5.5492279374999995, 2.920046645, 1.9774061274999999, 2.49197324, 3.605321685, 5.0940382975, 4.842149215, 3.8498856949999998, 4.112444445, 4.8111160150000005, 6.76761958, 6.2140404625, 6.116827227500001, 5.80366099, 5.741697415, 6.48747991, 6.0926051825, 6.1273796250000006, 6.034683585000001, 5.689826235, 5.51537609, 4.808258475000001, 4.414609400000001, 5.070640245, 5.195178802499999, 4.915383364999999, 4.00591159, 3.3357249500000004, 3.8756964524999997, 4.966797987500001, 7.1336221175, 5.680920609999999, 3.43873378, 3.4874896475000003, 4.4536010325, 6.3035896425, 6.9942980175, 3.7250355424999997, 2.659630935, 3.18259333, 4.20144821, 6.44410364, 3.8386817449999997, 2.5805204, 2.7422475325, 2.242671615, 3.543811505, 3.2758745174999997, 1.773511045, 2.25592567, 1.1691843075000001, 1.279333225, 1.75512759, 0.4413581825, 1.5040112375, 2.181932285, 1.189909175, 0.14390269175, -0.847124365, 0.162006471375, 1.952362165, 2.7537733675])
    sample = Total_SE - Total_SE_Tunnel    
    if i == 2:
#        plt.plot(x, Total_SE, label = 'Sample1')
        plt.plot(x, sample, label = 'Sample 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 6:
#        plt.plot(x, Total_SE, label = 'Sample2')
        plt.plot(x, sample, label = 'Sample 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 10:
#        plt.plot(x, Total_SE, label = 'Sample3')
        plt.plot(x, sample, label = 'Sample 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 14:
        plt.plot(x, sample, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
#        plt.plot(x, Total_SE, label = 'Sample4')
        plt.plot(x, sample, label = 'Sample 5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

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
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
    plt.title(name_dict[i])
    if i == 3:
        plt.plot(x, mag, label = 'Sample 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 7:
        plt.plot(x, mag, label = 'Sample 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 11:
        plt.plot(x, mag, label = 'Sample 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 15:
        plt.plot(x, mag, label = 'Sample 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 19:
        plt.plot(x, mag, label = 'Sample 5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.show()


        
S1 = []      
'----------------------------------------------'
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
       
#    fig = plt.figure(100)
#    print(i, ':', keyslist[i])
    y = datalist[i]             # data 
    f = np.abs(y)
    mag = 20*log10(f)
    S11 = 10**mag
    S1.append(S11)
fig = plt.figure(901)
plt.title('Sheilding Effectivness Due To Absorption')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Shielding Due To Absorption (dB)')

SEA_Tunnel = np.array([0.26390914375, -0.6579339479999999, 1.6226839100000001, 1.2305666225, -1.9741019625, -0.6005563842499999, -1.3070515950000001, -0.331777603, 0.7461791664999999, -2.4252373599999997, -1.955666665, -0.9213228785, -0.17133898525000002, 2.1864864225, -0.29255602575, -0.8678891557499999, 0.68672696, 0.48141001549999995, 3.8097519825, 2.9681968125, -0.51790282375, 0.74989355275, -0.193993510525, 1.1024766000000001, 2.9017251225000003, -0.9557707472500001, -0.795969856, -0.6491365847499999, 0.12261888474999999, 2.7831882425000005, 0.31887973599999997, -0.97338023475, -0.5942628015, -0.59238309375, 2.338118625, 2.0947828375000004, -0.47830107075, -0.298315982, -0.46656814025000004, 1.7212786249999998, 3.8298241125, 0.85489321225, -0.289896382, -0.5826264590000001, 0.35870968225, 3.2375924375, 2.1537511225, 0.49055363525, 0.23131869900000002, 0.06574192225, 3.13040963, 3.745118105, 1.2850670124999999, 0.77479005025, -0.2437091345, 1.500555545, 3.0153963074999997, 1.7597390675, 0.900398521, -0.3917781145, -0.21279932099999999, 3.0868415450000004, 2.0028330825, 0.77925151075, -0.79875792775, -1.8253776824999999, 2.3173434475000003, 2.8061728500000003, 0.34361762225000003, -0.202710494325, -1.6636387, 1.8991293949999999, 6.4615507325, 2.9348292024999996, 1.4476410325, -0.21288281050000002, 0.002357972814999998, 7.646874605, 5.7118095475, 1.83784605, -0.55112788775, -2.1968299874999997, 6.9191321925, 8.386807525, 3.659485015, 4.1292402425, -2.9719022899999996, -0.5436238112499999, 12.1793273525, 11.2375673625, 10.863127255, 6.889262565, 3.1641643624999998, 14.4849621725, 20.064484315, 20.0155946625, 17.136160385, 6.3243602050000005, 14.044372895, 26.09010688, 24.013467285, 23.340940125, 14.394172185, 11.71979777, 22.204716400000002, 21.4766130425, 22.9404336875, 20.88531286, 9.5965489725, 14.2122796375, 20.9703241325, 21.68353177, 21.75832708, 10.766990794999998, 6.1155681225, 12.5201700925, 14.293337005, 16.2118567, 10.396434697499998, 1.14040427, 3.70810673, 8.2082760675, 11.691907180000001, 11.643677912500001, 3.2298568525, 0.9008088590000001, 4.7488944275, 7.750266524999999, 9.9958899975, 3.632858315, -2.1596030324999997, 0.039688513450000004, 3.7442547425, 6.33331538, 4.476049225, 0.144627844, 0.76808162225, 2.3208037625, 5.16979658, 5.5492279374999995, 2.920046645, 1.9774061274999999, 2.49197324, 3.605321685, 5.0940382975, 4.842149215, 3.8498856949999998, 4.112444445, 4.8111160150000005, 6.76761958, 6.2140404625, 6.116827227500001, 5.80366099, 5.741697415, 6.48747991, 6.0926051825, 6.1273796250000006, 6.034683585000001, 5.689826235, 5.51537609, 4.808258475000001, 4.414609400000001, 5.070640245, 5.195178802499999, 4.915383364999999, 4.00591159, 3.3357249500000004, 3.8756964524999997, 4.966797987500001, 7.1336221175, 5.680920609999999, 3.43873378, 3.4874896475000003, 4.4536010325, 6.3035896425, 6.9942980175, 3.7250355424999997, 2.659630935, 3.18259333, 4.20144821, 6.44410364, 3.8386817449999997, 2.5805204, 2.7422475325, 2.242671615, 3.543811505, 3.2758745174999997, 1.773511045, 2.25592567, 1.1691843075000001, 1.279333225, 1.75512759, 0.4413581825, 1.5040112375, 2.181932285, 1.189909175, 0.14390269175, -0.847124365, 0.162006471375, 1.952362165, 2.7537733675])
SEA1 = np.log10(((np.abs(S2[0]))**2 / (1 - (np.abs(S1[0]))**2))**(-10))
SEA2 = np.log10(((np.abs(S2[1]))**2 / (1 - (np.abs(S1[1]))**2))**(-10))
SEA3 = log10(((np.abs(S2[2]))**2 / (1 - (np.abs(S1[2]))**2))**(-10))
SEA4 = np.log10(((np.abs(S2[3]))**2 / (1 - (np.abs(S1[3]))**2))**(-10))
SEA5 = np.log10(((np.abs(S2[4]))**2 / (1 - (np.abs(S1[4]))**2))**(-10))
sample1 = SEA1 - SEA_Tunnel
sample2 = SEA2 - SEA_Tunnel
sample3 = SEA3 - SEA_Tunnel
sample4 = SEA4 - SEA_Tunnel
sample5 = SEA5 - SEA_Tunnel


#plt.plot(x, SEA1, label = 'Sample1')
plt.plot(x, sample1, label = 'Sample 1')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#print(SEA1)


#plt.plot(x, SEA2, label = 'Sample2')
plt.plot(x, sample2, label = 'Sample 2')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


#plt.plot(x, SEA3, label = 'Sample3')
plt.plot(x, sample3, label = 'Sample 3')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#SEA4 = np.log10(((np.abs(S2[3]))**2 / (1 - (np.abs(S1[3]))**2))**(-10))
plt.plot(x, sample4, label = 'Sample 4')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#SEA5 = np.log10(((np.abs(S2[4]))**2 / (1 - (np.abs(S1[4]))**2))**(-10))
#plt.plot(x, SEA5, label = 'Sample4')
plt.plot(x, sample5, label = 'Sample 5')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#print(S1, 'S11')
#print(S2, 'S22')




#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.title('Shielding Due To Absorption (dB) minus tunnel')
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('Shielding Due To Absorption (dB)')



        

plt.show()


