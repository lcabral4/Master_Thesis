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
    S11 = 10**mag
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
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
    if i == 12:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, mag, label = 'Sample5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(name_dict[i])
    fig = plt.figure(11)
    SER = -10* log10(1 - np.abs(S11)**2)
#    plt.plot(x, SER)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('SER (dB)')
    plt.title('Shielding Due To Reflection')
    if i == 0:
        plt.plot(x, SER, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 4:
        plt.plot(x, SER, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 8:
        plt.plot(x, SER, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 12:
        plt.plot(x, SER, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, SER, label = 'Sample5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
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
#    plt.plot(x, mag)
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
    S12 = 10**mag
    Total_SE = -10*log10(np.abs(S12)**2)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
#    plt.plot(x, mag)
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
        
    if i == 2:
        plt.plot(x, Total_SE, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 6:
        plt.plot(x, Total_SE, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 10:
        plt.plot(x, Total_SE, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 14:
        plt.plot(x, Total_SE, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, Total_SE, label = 'Sample5')
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
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz')
    plt.ylabel('Log Magnitude (dB')
#    plt.plot(x, mag)
    plt.title(name_dict[i])
    if i == 3:
        plt.plot(x, mag, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 7:
        plt.plot(x, mag, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 11:
        plt.plot(x, mag, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 15:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 19:
        plt.plot(x, mag, label = 'Sample5')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.show()


        
        
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
#    print(y)
    f = np.abs(y)
#    f = sqrt(test)
#    t.append(f)
#    w.append(f)
    mag = 20*log10(f)
    S11 = 10**mag
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    for j in range(N):
        if j == 0:
            continue
        if j == 1:
            continue
        if j ==3:
            continue
        if j == 4:
            continue
        if j == 5:
            continue
        if j == 7:
            continue
        if j == 8:
            continue
        if j == 9:
            continue
        if j == 11:
            continue
        if j == 12:
            continue
        if j == 13:
            continue
        if j == 15:
            continue
        if j == 16:
            continue
        if j == 17:
            continue
        if j == 19:
            continue
        
        
        fig = plt.figure(900)
    #    print(i, ':', keyslist[i])
        y = datalist[j]             # data 
    #    print(y)
        f = np.abs(y)
    #    f = sqrt(test)
        mag = 20*log10(f)
        S12 = 10**mag
        SEA = -10 * log10(np.abs(S12)**2 / (1 - np.abs(S11)**2))
    #    print(mag)
    #    [S11, S21, S12,S22]
    #    y = np.append(mag)
        plt.title('SE Due To Absorption')
        plt.xlabel('Frequancy (Hz)')
        plt.ylabel('SEA (dB)')
#        plt.plot(x, SEA)
        if j == 2:
            plt.plot(x, mag, label = 'Sample1')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if j == 6:
            plt.plot(x, mag, label = 'Sample2')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if j == 10:
            plt.plot(x, mag, label = 'Sample3')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if j == 14:
            plt.plot(x, mag, label = 'Sample4')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if j == 18:
            plt.plot(x, mag, label = 'Sample5')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#        plt.title(name_dict[i])
        

plt.show()


