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
        
    if i == 12:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
    if i == 16:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('S11.png', bbox_inches='tight')
        
    plt.title(name_dict[i])
    fig = plt.figure(11)
    SER = -10* log10(1 - np.abs(S11)**2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('SER (dB)')
    plt.title('Shielding Due To Reflection')
#    print(SER, 'SER')
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
    plt.savefig('SER.png', bbox_inches='tight')
    
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
    plt.savefig('S21.png', bbox_inches='tight')
        
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
#    print(Total_SE)
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
    plt.savefig('S12.png',  bbox_inches='tight')
    plt.title(name_dict[i])
    fig = plt.figure(9)
    plt.title('Total SE')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Total SE (dB)')
#    print(Total_SE)
#    plt.legend((Total_SE[i]),loc='center left')
    Total_SE_Tunnel = np.array([1.1231416275, 0.53950342, 2.041020575, 2.1539709925, 0.2572726345, 1.2235351475, 0.9014833522500001, 1.9500486000000001, 1.9880438725, 0.157729689625, 1.4645482375000003, 2.1538961925, 3.2186800775, 3.9632626875000003, 1.09228358, 2.03517349, 3.1463959374999995, 3.5523321249999995, 6.166210485000001, 2.4515346649999996, -0.3252221995, 1.7476820075, 0.3279507897499999, 2.86382761, 2.1833415824999998, -2.837556825, -1.3158808725, -1.2996621474999999, 0.24806499025, 2.87765338, -1.60390367, -3.0352022725, -2.5063302875000004, -1.605952475, 3.2474328150000003, 0.94990672, -3.3500538150000003, -2.4705782024999996, -2.3933177, 1.8257771725, 3.2999499525000004, -1.684742065, -2.6145157625, -3.0055233825000003, -0.90483183175, 3.189104705, 0.630123956, -1.5838957974999999, -1.5256581725, -1.313342645, 3.0783144174999997, 2.761985905, -0.0893230076225, -0.5177982965, -1.8111744375, 0.9961494200000001, 2.7651596300000003, -0.0219216898675, -0.7767444510000001, -1.9550865675, -0.4605035985, 3.2287415800000003, 0.06664620525, -2.0568293625, -3.385426165, -3.34133831, 2.643879315, 1.6859721075, -2.354636165, -2.7511354075, -4.1315896500000004, 1.7174740075, 5.809744745, -0.675398514, -2.4382120124999997, -4.426756425, -3.598179425, 4.4177352675, 1.2831998675, -3.1476370425, -6.0293101675, -7.29326864, 2.5053141375, 3.8075778675, -1.78499626, -1.2646085325, -8.222473777500001, -6.326156155, 6.213127165, 5.623527480000001, 5.103844544999999, 2.0149133050000003, -2.1399696324999997, 7.67259266, 14.258852335, 14.8714720075, 13.1259757575, 3.8755808800000002, 8.346913022499999, 19.364819999999998, 18.658450719999998, 18.644200665, 12.551333204999999, 8.945807895, 17.094779884999998, 18.1356848125, 19.1063130375, 19.166983967500002, 10.648288112500001, 12.09030499, 17.527642002500002, 18.303763682499998, 18.517040910000002, 11.221767807499997, 6.0369709799999995, 10.32752505, 11.737533325000001, 12.802722342500001, 8.639967147499998, 1.064488655, 1.6734113975, 4.8286254775, 7.175964102499999, 5.6090134475, -1.03195234275, -3.1266400675000003, -0.749468185, 1.4232521274999999, 2.0371598375, -4.9982721575, -9.4980770675, -6.8212989125000005, -3.0329328825, -1.250347915, -5.536313365000001, -9.900874825, -8.149877637500001, -5.7343698375, -2.0164184824999998, -2.8832991550000004, -7.3034072, -7.524956852500001, -6.054506045, -2.9026037125, -0.843800656, -3.306368355, -3.9984857199999997, -3.1596947225, -0.8448678270000001, 1.9051085125, -0.71503182725, -2.8569501300000004, -2.2989277675000004, -1.4459719224999998, -0.69256552325, -1.86650978, -2.8771726775, -2.766004265, -2.7732159725, -2.98696263, -5.150185205, -5.33216278, -4.1031679175, -3.0847495725000003, -2.23615342, -5.0091719125, -6.9946153725, -5.429407749999999, -4.172503175, -0.341283331875, -1.423243255, -6.300272555, -5.235565644999999, -2.84966158, 1.1657971774999998, 3.035602235, -3.11246075, -5.4856151650000005, -3.038066485, -0.035546824625, 3.703964885, 0.062962324935, -3.8284141525, -2.79327718, -2.0587316275, 1.04061006875, 1.57135904, -1.7615752025, -2.22422013, -2.93810865, -2.7200214075, -1.6598456499999998, -2.075474225, -2.4626682025, -2.6879967675, -3.21106381, -5.47468954, -6.144122267500001, -3.9353822375000003, -2.2114834125000002, 0.132414575625])
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
#    if i == 18:
#        plt.plot(x, Total_SE, label = 'Sample4')
#        plt.plot(x, sample, label = 'Sample 5')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('Total_SE.png',  bbox_inches='tight')

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
    plt.savefig('S22.png', bbox_inches='tight')
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

SEA_Tunnel = np.array([1.1231416275, 0.53950342, 2.041020575, 2.1539709925, 0.2572726345, 1.2235351475, 0.9014833522500001, 1.9500486000000001, 1.9880438725, 0.157729689625, 1.4645482375000003, 2.1538961925, 3.2186800775, 3.9632626875000003, 1.09228358, 2.03517349, 3.1463959374999995, 3.5523321249999995, 6.166210485000001, 2.4515346649999996, -0.3252221995, 1.7476820075, 0.3279507897499999, 2.86382761, 2.1833415824999998, -2.837556825, -1.3158808725, -1.2996621474999999, 0.24806499025, 2.87765338, -1.60390367, -3.0352022725, -2.5063302875000004, -1.605952475, 3.2474328150000003, 0.94990672, -3.3500538150000003, -2.4705782024999996, -2.3933177, 1.8257771725, 3.2999499525000004, -1.684742065, -2.6145157625, -3.0055233825000003, -0.90483183175, 3.189104705, 0.630123956, -1.5838957974999999, -1.5256581725, -1.313342645, 3.0783144174999997, 2.761985905, -0.0893230076225, -0.5177982965, -1.8111744375, 0.9961494200000001, 2.7651596300000003, -0.0219216898675, -0.7767444510000001, -1.9550865675, -0.4605035985, 3.2287415800000003, 0.06664620525, -2.0568293625, -3.385426165, -3.34133831, 2.643879315, 1.6859721075, -2.354636165, -2.7511354075, -4.1315896500000004, 1.7174740075, 5.809744745, -0.675398514, -2.4382120124999997, -4.426756425, -3.598179425, 4.4177352675, 1.2831998675, -3.1476370425, -6.0293101675, -7.29326864, 2.5053141375, 3.8075778675, -1.78499626, -1.2646085325, -8.222473777500001, -6.326156155, 6.213127165, 5.623527480000001, 5.103844544999999, 2.0149133050000003, -2.1399696324999997, 7.67259266, 14.258852335, 14.8714720075, 13.1259757575, 3.8755808800000002, 8.346913022499999, 19.364819999999998, 18.658450719999998, 18.644200665, 12.551333204999999, 8.945807895, 17.094779884999998, 18.1356848125, 19.1063130375, 19.166983967500002, 10.648288112500001, 12.09030499, 17.527642002500002, 18.303763682499998, 18.517040910000002, 11.221767807499997, 6.0369709799999995, 10.32752505, 11.737533325000001, 12.802722342500001, 8.639967147499998, 1.064488655, 1.6734113975, 4.8286254775, 7.175964102499999, 5.6090134475, -1.03195234275, -3.1266400675000003, -0.749468185, 1.4232521274999999, 2.0371598375, -4.9982721575, -9.4980770675, -6.8212989125000005, -3.0329328825, -1.250347915, -5.536313365000001, -9.900874825, -8.149877637500001, -5.7343698375, -2.0164184824999998, -2.8832991550000004, -7.3034072, -7.524956852500001, -6.054506045, -2.9026037125, -0.843800656, -3.306368355, -3.9984857199999997, -3.1596947225, -0.8448678270000001, 1.9051085125, -0.71503182725, -2.8569501300000004, -2.2989277675000004, -1.4459719224999998, -0.69256552325, -1.86650978, -2.8771726775, -2.766004265, -2.7732159725, -2.98696263, -5.150185205, -5.33216278, -4.1031679175, -3.0847495725000003, -2.23615342, -5.0091719125, -6.9946153725, -5.429407749999999, -4.172503175, -0.341283331875, -1.423243255, -6.300272555, -5.235565644999999, -2.84966158, 1.1657971774999998, 3.035602235, -3.11246075, -5.4856151650000005, -3.038066485, -0.035546824625, 3.703964885, 0.062962324935, -3.8284141525, -2.79327718, -2.0587316275, 1.04061006875, 1.57135904, -1.7615752025, -2.22422013, -2.93810865, -2.7200214075, -1.6598456499999998, -2.075474225, -2.4626682025, -2.6879967675, -3.21106381, -5.47468954, -6.144122267500001, -3.9353822375000003, -2.2114834125000002, 0.132414575625])
SEA1 = np.log10(((np.abs(S2[0]))**2 / (1 - (np.abs(S1[0]))**2))**(-10))
SEA2 = np.log10(((np.abs(S2[1]))**2 / (1 - (np.abs(S1[1]))**2))**(-10))
SEA3 = log10(((np.abs(S2[2]))**2 / (1 - (np.abs(S1[2]))**2))**(-10))
SEA4 = np.log10(((np.abs(S2[3]))**2 / (1 - (np.abs(S1[3]))**2))**(-10))
SEA5 = np.log10(((np.abs(S2[4]))**2 / (1 - (np.abs(S1[4]))**2))**(-10))
#print(SEA1, SEA2, SEA3, SEA4, SEA5)
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
plt.savefig('SEA.png', bbox_inches='tight')




#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.title('Shielding Due To Absorption (dB) minus tunnel')
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('Shielding Due To Absorption (dB)')



        

plt.show()



