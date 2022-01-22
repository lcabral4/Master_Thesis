#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 19:36:41 2021

@author: lcabral4
"""

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
#    print(mag, 'mag')
    tunnelS11 = np.array([-21.606979677499996, -21.7701966025, -21.720956575, -21.498432785, -21.0656974475, -21.3253900925, -21.573780900000003, -22.0004095975, -22.06549244, -21.761000905000003, -21.87486409, -21.8741588925, -22.123646025, -22.1367207075, -22.075691505, -21.894631715, -21.891007375, -21.9151409225, -22.098641035, -21.9335173, -21.6497048425, -21.394490197499998, -21.2341361425, -21.1223048975, -21.3183144625, -21.438549475, -21.307777684999998, -21.594841657499998, -21.7339387275, -22.42003148, -22.88199376, -23.0535870375, -23.53027775, -23.890789480000002, -24.191753204999998, -24.116554004999998, -24.382481255, -24.3796252575, -24.088863045, -23.185698725, -22.8722588775, -23.33346288, -23.352306625, -23.58603183, -23.3589758575, -23.0216656025, -23.176802462499996, -23.101810565, -22.728022324999998, -22.7743526625, -22.416756799999998, -22.745903229999996, -23.346220674999998, -23.0209651275, -22.9700334325, -23.293295105, -23.6074980525, -24.187823972500002, -23.621391770000002, -22.51112138, -22.2428022625, -21.805513247500002, -22.39518267, -23.141200970000003, -21.9044868675, -21.0580430575, -20.9056236325, -21.2222190275, -21.702548245, -21.05043989, -19.66165089, -18.578667475000003, -17.665802295000002, -17.4576088275, -17.285263387500002, -16.25491197, -15.2016640025, -14.730033165, -14.691716397499999, -14.7705794425, -14.271508372500001, -13.37031227, -13.0586619775, -12.7682967725, -12.77423409, -12.6298697225, -11.739944312499999, -11.20957213, -10.869866817499998, -10.833042080000002, -10.941093315, -10.639468735, -10.04698264, -9.86554527, -9.751199385, -9.662629567500002, -9.6565794175, -9.185144305000001, -8.673324635, -8.4239302125, -8.41984883, -8.6477952125, -8.6749541825, -8.309857560000001, -8.333755392499999, -8.330568575000001, -8.481018265, -8.686797214999999, -8.59402521, -8.5165511975, -8.37944817, -8.300650220000001, -8.581935415, -8.906270427499999, -8.876572845, -8.812342395, -8.9725199275, -9.186784585, -9.6090147225, -9.9257782, -10.016138752500002, -9.854661245, -9.884978162500001, -10.42567545, -11.099412565, -11.309853190000002, -11.223544727500002, -11.27178322, -11.9816820125, -13.01859746, -14.0355785275, -14.17155526, -13.713939522499999, -13.751830177499999, -14.849307005, -16.434728879999998, -17.9417305025, -17.701465915, -17.086313665000002, -17.777599815, -19.3921695475, -22.788027125, -25.526839825000003, -23.8486657075, -22.3820728475, -21.745833047500003, -22.844909565000002, -26.1874501725, -27.3950576925, -26.0234018075, -25.9072685575, -25.996036455, -30.778796032499997, -37.824928315, -40.36225194, -35.6941879875, -29.8170647325, -30.804015077500004, -34.113556259999996, -40.29908379, -39.66944332, -44.4540536975, -34.9752145975, -29.537346355, -26.25293398, -27.0948314225, -28.401201564999997, -26.778544009999997, -23.578168859999998, -21.727627802500002, -23.412819024999997, -26.2480283025, -25.0353983875, -22.2809693975, -20.814908935000002, -20.548265054999998, -23.254910345, -23.5587500875, -21.2105512, -19.12494823, -17.553828205, -18.687173927499998, -20.6190502575, -19.80033706, -18.182129999999997, -16.9996259875, -16.5479747675, -18.61072441, -19.2354199125, -18.0905535975, -16.6919741875, -15.048197945, -15.7148726225, -16.75653128, -16.259931587500002, -15.365818052500002, -14.024189867499999, -13.700621889999999, -15.4340249375, -16.137201909999998, -15.61166894])
#    print(tunnelS11, 'tunnel')
    mag1 = mag - tunnelS11
#    print(mag1, 'mag1')
    S11 = 10**mag
    S11_Sub = 10**mag1
#    print(mag)
#    print(mag1)
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
#    plt.plot(x, mag)
    if i == 0:
        plt.plot(x, mag, label = 'Sample1')
#        plt.plot(x, mag1, label = 'subtracted')
#        plt.plot(x, tunnelS11, label = 'Average')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 4:
        plt.plot(x, mag, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 8:
        plt.plot(x, mag, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 12:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 0:
        plt.plot(x, mag1, label = 'subtracted 1')
        plt.plot(x, tunnelS11, label = 'Average')
    if i == 4:
        plt.plot(x, mag1, label = 'subtratced 2')
    if i == 8:
        plt.plot(x, mag1, label = 'subtracted 3')
    if i == 16:
        plt.plot(x, mag1, label = 'subtracted 4')
#    plt.plot(x, tunnelS11, 'Avegrage S11')
#    plt.plot(x, mag1, 'subtracted')
    plt.title(name_dict[i])
    fig = plt.figure(11)
    SER = np.log10((1 - (np.abs(S11))**2)**(-10))
    SER1 = np.log10((1 - (np.abs(S11_Sub))**2)**(-10))
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
#    if i == 12:
#        plt.plot(x, SER, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, SER, label = 'Sample 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 0:
        plt.plot(x, SER1, label = 'Subtracted 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 4:
        plt.plot(x, SER1, label = 'Subtracted 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 8:
        plt.plot(x, SER1, label = 'Subtracted 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 12:
#        plt.plot(x, SER, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 16:
        plt.plot(x, SER1, label = 'Subtracted 4')
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
    TunnelS21 = np.array([-0.042166557675, 0.013481247825, -0.049459250974999994, -0.025752039475000002, -0.004492886242, -0.0006923011700000001, 0.12766992975000002, 0.13523201325, 0.058998158275, 0.068658591025, 0.009321966125000001, 0.078738169075, 0.1417895145, -0.0054071679475, -0.026968958850000002, -0.030930619499999996, -0.048020247425, 0.08318755652500001, 0.024373908275, -0.07409303915, -0.07171843744999999, -0.173748139, -0.1000147632, -0.0452185891, -0.152664573, -0.10438240447500001, -0.134304047, -0.1397101415, 0.04531703455, 0.0430655974, 0.011320436775, 0.01254756205, -0.072262785675, -0.0358818526, -0.03168826205, -0.12017051025, -0.15100381075, -0.22901815175, -0.20933042475000002, -0.12528451575, -0.18168411350000002, -0.15990706575, -0.165250868, -0.20138607675, -0.093964073375, -0.1384871285, -0.18479073925, -0.1617840225, -0.26496896974999995, -0.23016759675, -0.09914176705000001, -0.10514210874999999, -0.0436760434, -0.050052478525000006, -0.12025504249999999, -0.043582675725, -0.06168387407499999, -0.073182912725, -0.08371289515000001, -0.23588307, -0.20100520624999998, -0.10703525875, -0.09769880105, 0.03761804170000001, 0.020577289425, -0.11139663175, 0.0080444582, 0.00303347606, -0.024772297999999998, -0.036656235375, -0.275447875, -0.30038304125, -0.24698379250000002, -0.31198871650000004, -0.161543686, -0.14771166300000002, -0.210405852, 0.009491503450000001, -0.032903324925, -0.032900009875, 0.17531155199999998, 0.012091683874999998, -0.076186747625, -0.2235485175, -0.50170650875, -0.24749950950000002, -0.267218709, -0.521896839, -0.29798942349999996, -0.39138117099999997, -0.2853658335, 0.036233945975, -0.32535290099999997, -0.5589885087500001, -0.65590193, -0.93018722425, -0.759356957, -0.90723886, -1.0349111375, -0.6531706905, -0.6055021792499999, -0.44354032499999996, -0.1588369925, -0.29625812125, -0.1959837055, -0.28984052025, -0.75826635575, -0.74216471525, -0.8359590505, -0.91709490675, -0.9089854417500001, -1.1145605425, -0.88757475525, -0.6372497585000001, -0.6319891317499999, -0.5828569557500001, -0.7776586500000001, -0.83215253375, -0.790295492, -0.9344773497500001, -0.8018856255, -0.7177978227499999, -0.7217293997500001, -0.5376647602500001, -0.5257218815, -0.385211883, -0.19576779075, -0.16947985449999997, -0.18356710400000004, -0.31194319425, -0.3084352535, -0.118605798, -0.1436548115, -0.1022658425, -0.08412038535000001, -0.152150385, 0.007395682595, -0.015519320400000002, -0.11718182325, -0.134845969, -0.22480829925, -0.20059617, -0.15720732775, -0.20224105350000002, -0.1492468275, -0.17193593375, -0.18324056500000002, -0.050583623800000005, -0.11735890624999999, -0.14822978325, -0.2461468075, -0.302003265, -0.26704118975, -0.26365525175, -0.26204732475, -0.30154418499999996, -0.30397313525, -0.25409941275, -0.280396626, -0.2786981355, -0.29069542075, -0.29892213325, -0.13868947125, -0.14362559849999998, -0.06849413755, -0.0173972498, -0.09016244885, 0.0461770998, -0.005772388077499999, -0.05788350955, -0.0982655004, -0.28073706499999995, -0.22820326875000002, -0.06982513704999999, -0.07884461225, -0.006367394475, -0.1608519405, -0.2038802735, 0.04379737655, -0.04699253002499999, -0.07535485060000001, -0.17732468725, -0.37074819999999997, -0.25278859249999996, -0.168809861, -0.16630247175, -0.0791233313, -0.222229456, -0.19514361725, -0.10469423550000001, -0.18227437675, -0.1767762255, -0.27313607925, -0.31972145075, -0.27578018925000003, -0.31302014375000003, -0.28824327850000003, -0.27540763575, -0.3024109285, -0.199434738, -0.19131393875])
#    print(mag)
    mag1 = mag - TunnelS21
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
#    if i == 13:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    if i == 17:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 1:
        plt.plot(x, mag1, label = 'Subtracted 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 5:
        plt.plot(x, mag1, label = 'Subtracted 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 9:
        plt.plot(x, mag1, label = 'Subtracted 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 13:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 17:
        plt.plot(x, mag1, label = 'Subtracted 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))    

S2 = [] 
S2_Sub = []   
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
    TunnelS12 = np.array([-0.013195458075, 0.032896697, -0.081134195725, -0.0615283309, 0.09870509902499999, 0.03002781995, 0.06535257995, 0.016588878775, -0.03730895845, 0.12126187025000001, 0.0977833326, 0.04606614317499999, 0.0085669505075, -0.10932432075, 0.014627801025, 0.043394458675, -0.034336347375, -0.024070501775, -0.1904875975, -0.1484098395, 0.025895140924999997, -0.0374946795, 0.0096996754075, -0.055123830475, -0.14508625775, 0.047788535475, 0.039798491525, 0.032456828874999996, -0.0061309452425, -0.1391594115, -0.015943985799999998, 0.048669012124999994, 0.02971314055, 0.029619156175, -0.11690592975, -0.104739142, 0.023915054025, 0.0149157971, 0.0233284084, -0.08606393170000001, -0.19149120625, -0.042744661350000004, 0.014494819594999998, 0.029131324575, -0.017935484725, -0.161879622, -0.107687557, -0.02452768075, -0.011565936225, -0.0032870958600000003, -0.15652048075000002, -0.187255905, -0.06425335005, -0.0387395035, 0.01218545585, -0.0750277768, -0.150769814, -0.08798695375000001, -0.0450199263, 0.0195889051, 0.010639967180000001, -0.154342078, -0.1001416535, -0.038962574775, 0.03993789625, 0.091268883175, -0.11586717275, -0.1403086435, -0.017180879875, 0.0101355248425, 0.0831819343, -0.0949564682, -0.32307753575, -0.1467414595, -0.07238205192500001, 0.010644140145, -0.00011789851575, -0.38234372875, -0.28559047600000004, -0.091892300625, 0.02755639365, 0.10984149850000001, -0.34595661125, -0.41934037599999996, -0.18297424950000002, -0.20646201400000003, 0.14859511475, 0.027181190049999998, -0.6089663675, -0.5618783675, -0.5431563634999999, -0.344463128, -0.1582082185, -0.72424810875, -1.003224215, -1.0007797324999999, -0.8568080202499999, -0.31621801, -0.702218646, -1.304505345, -1.2006733625, -1.167047005, -0.7197086082499999, -0.5859898889999999, -1.1102358200000002, -1.073830655, -1.1470216850000001, -1.0442656425, -0.4798274495, -0.71061398125, -1.0485162074999999, -1.0841765875, -1.087916355, -0.5383495395, -0.30577840599999995, -0.62600850575, -0.7146668515000001, -0.8105928357500001, -0.5198217345, -0.057020214124999996, -0.18540533750000002, -0.4104138015, -0.5845953577499999, -0.58218389775, -0.16149284074999998, -0.045040440699999996, -0.2374447225, -0.38751332800000005, -0.499794501, -0.18164291524999998, 0.10798015324999999, -0.0019844266725, -0.187212737, -0.31666576975000005, -0.22380245950000002, -0.00723139282, -0.038404081475000004, -0.11604018925, -0.25848982775, -0.27746139825, -0.1460023305, -0.09887030545, -0.12459866074999999, -0.18026608500000002, -0.254701915, -0.242107462, -0.19249428475, -0.20562222075, -0.24055580125, -0.33838098, -0.31070202225, -0.30584136275, -0.2901830485, -0.287084871, -0.32437399575000003, -0.30463025975, -0.30636898225, -0.30173417925, -0.284491311, -0.27576880425, -0.24041292525, -0.22073047025000003, -0.25353201225, -0.25975894, -0.245769167, -0.20029557899999997, -0.16678624749999998, -0.1937848245, -0.24833990025, -0.35668110675, -0.284046029, -0.1719366885, -0.1743744825, -0.22268005125, -0.31517948025, -0.34971490125000004, -0.186251777, -0.132981548, -0.1591296665, -0.21007241075, -0.3222051805, -0.19193408675, -0.12902602000000002, -0.137112376, -0.11213358000000001, -0.1771905755, -0.16379372725000002, -0.08867555390000001, -0.112796283, -0.058459215950000004, -0.063966659425, -0.0877563801, -0.0220679071, -0.075200561075, -0.1090966145, -0.059495457200000004, -0.007195134959999999, 0.042356218, -0.008100323695, -0.09761810805, -0.13768866975])
#    print(mag)
    mag1 = mag - TunnelS12
    S12 = 10**mag
    S12_Sub = 10**mag1
    S2.append(S12)
    S2_Sub.append(S12_Sub)
    Total_SE = np.log10((np.abs(S12)**2)**(-10))
    Total_SE_Sub = np.log10((np.abs(S12_Sub)**2)**(-10)) 
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
#    if i == 14:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, mag, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 2:
        plt.plot(x, mag1, label = 'Sample1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 6:
        plt.plot(x, mag1, label = 'Sample2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 10:
        plt.plot(x, mag1, label = 'Sample3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 14:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, mag1, label = 'Sample4')
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
#    if i == 14:
#        plt.plot(x, Total_SE, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, Total_SE, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 2:
        plt.plot(x, Total_SE_Sub, label = 'Subtracted 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 6:
        plt.plot(x, Total_SE_Sub, label = 'Subtracted 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 10:
        plt.plot(x, Total_SE_Sub, label = 'Subtracted 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 14:
#        plt.plot(x, Total_SE, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 18:
        plt.plot(x, Total_SE_Sub, label = 'Subtracted 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
print(S2_Sub)
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
    TunnelS22 = np.array([-24.6014931525, -24.1114541625, -23.985789915, -23.3405180725, -22.059248880000002, -22.025822485, -22.1383355475, -22.8806173625, -23.3447500625, -22.4295876475, -21.62667859, -21.14722598, -21.0556701525, -21.3611217375, -21.098464565, -20.46343112, -19.869102915, -19.31225364, -19.309350127499997, -19.191903925, -18.838852415, -18.509827599999998, -18.280982677500003, -18.1909371175, -18.4025096425, -18.9596112275, -19.364124027499997, -19.9402312575, -20.3598544, -21.252459525, -22.446486272499996, -22.9106841425, -23.150491629999998, -23.12151252, -23.13451114, -23.8549652, -24.8045249225, -25.251889575, -25.2007486925, -23.9442485675, -23.683345455, -24.223898305, -24.250854752500004, -24.793695612500002, -24.1548277425, -23.65768361, -22.815823575, -21.321504197499998, -20.5637027, -19.764814044999998, -19.48334567, -19.749420280000002, -19.000699117499998, -18.385249537500002, -18.1004198475, -17.803289534999998, -18.18439629, -18.132956125, -17.554444215, -17.3063424475, -16.5094808775, -16.3183370275, -16.3497500075, -15.78329166, -15.636951625, -15.628806430000001, -15.802502555, -16.658643095, -16.6154947575, -16.17192621, -15.9100803525, -15.224626794999999, -15.22581989, -15.38428658, -14.893440845, -14.4177043575, -13.7793801975, -13.6038336725, -14.167730062499999, -14.349261325, -14.387626975000002, -14.2105647425, -14.0123692475, -13.9873479175, -13.675799269999999, -13.431723425, -13.3801800725, -13.205451127500002, -12.874085885, -12.8950800025, -12.568346089999999, -12.6423864025, -12.6076395075, -12.445452357499999, -12.26574373, -11.66805281, -11.366844175, -11.14373401, -10.487528627500001, -10.1792959975, -10.1646405525, -10.1559963775, -10.412822745, -10.1178718275, -10.120043335, -10.176675037499999, -9.836741700000001, -9.761959484999998, -9.7388498825, -9.555219885, -9.41124392, -9.117485967499999, -9.042497915, -9.1963562525, -9.086156022499999, -9.245205407499999, -9.293404055, -9.269013065, -9.29726687, -9.295617929999999, -9.1667847025, -9.108501287500001, -9.0477191825, -9.294072295, -9.4827973975, -9.357219687499999, -9.281077205, -9.420925715, -9.8313704875, -10.4235685575, -10.794955289999999, -10.6766824225, -10.80099891, -10.9701788275, -11.552787214999999, -12.030165715, -12.250015885000002, -12.833796875, -13.491000427500001, -14.4169784525, -15.6649088675, -16.8677633475, -18.2901565875, -19.6366635225, -20.46798998, -22.21843553, -23.597335567500004, -25.1806040125, -27.9032900325, -29.7735043875, -38.057452624999996, -38.453653537499996, -30.050109120000002, -25.320510262499997, -23.7989495925, -22.932280227499998, -21.027316482499998, -20.167299630000002, -19.2046764025, -18.50112313, -18.5890912725, -17.978417195, -17.2179404, -16.587219717500002, -15.2994022675, -14.7855885575, -14.22253799, -13.3699274875, -13.245014190000001, -13.13909499, -13.257827415, -13.5796143625, -13.38981317, -13.3004762375, -13.361361884999999, -13.5174613025, -13.8846802025, -13.71826797, -13.1685994825, -13.188055802500001, -13.30643105, -13.8830471125, -14.24361238, -14.158221687500001, -14.355198090000002, -14.305514005, -15.268860132499999, -16.4408494675, -16.289200475, -15.8551314475, -15.1568095175, -14.6322367, -15.3944128775, -15.99013299, -16.0542832975, -15.624706512500001, -14.3538002475, -14.844231837499999, -16.526968765, -17.981743859999998, -18.373535947500002])
    mag1 = mag - TunnelS22
#    print(mag)
#    [S11, S21, S12,S22]
#    y = np.append(mag)
    plt.xlabel('Frequancy (Hz)')
    plt.ylabel('Log Magnitude (dB)')
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
#    if i == 15:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 19:
        plt.plot(x, mag1, label = 'Sample4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 3:
        plt.plot(x, mag1, label = 'Subtracted 1')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 7:
        plt.plot(x, mag1, label = 'Subtracted 2')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 11:
        plt.plot(x, mag1, label = 'Subtracted 3')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    if i == 15:
#        plt.plot(x, mag1, label = 'Sample4')
#        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if i == 19:
        plt.plot(x, mag1, label = 'Subtracted 4')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        
S1 = []  
S1_Sub = []    
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
    tunnelS11 = np.array([-21.606979677499996, -21.7701966025, -21.720956575, -21.498432785, -21.0656974475, -21.3253900925, -21.573780900000003, -22.0004095975, -22.06549244, -21.761000905000003, -21.87486409, -21.8741588925, -22.123646025, -22.1367207075, -22.075691505, -21.894631715, -21.891007375, -21.9151409225, -22.098641035, -21.9335173, -21.6497048425, -21.394490197499998, -21.2341361425, -21.1223048975, -21.3183144625, -21.438549475, -21.307777684999998, -21.594841657499998, -21.7339387275, -22.42003148, -22.88199376, -23.0535870375, -23.53027775, -23.890789480000002, -24.191753204999998, -24.116554004999998, -24.382481255, -24.3796252575, -24.088863045, -23.185698725, -22.8722588775, -23.33346288, -23.352306625, -23.58603183, -23.3589758575, -23.0216656025, -23.176802462499996, -23.101810565, -22.728022324999998, -22.7743526625, -22.416756799999998, -22.745903229999996, -23.346220674999998, -23.0209651275, -22.9700334325, -23.293295105, -23.6074980525, -24.187823972500002, -23.621391770000002, -22.51112138, -22.2428022625, -21.805513247500002, -22.39518267, -23.141200970000003, -21.9044868675, -21.0580430575, -20.9056236325, -21.2222190275, -21.702548245, -21.05043989, -19.66165089, -18.578667475000003, -17.665802295000002, -17.4576088275, -17.285263387500002, -16.25491197, -15.2016640025, -14.730033165, -14.691716397499999, -14.7705794425, -14.271508372500001, -13.37031227, -13.0586619775, -12.7682967725, -12.77423409, -12.6298697225, -11.739944312499999, -11.20957213, -10.869866817499998, -10.833042080000002, -10.941093315, -10.639468735, -10.04698264, -9.86554527, -9.751199385, -9.662629567500002, -9.6565794175, -9.185144305000001, -8.673324635, -8.4239302125, -8.41984883, -8.6477952125, -8.6749541825, -8.309857560000001, -8.333755392499999, -8.330568575000001, -8.481018265, -8.686797214999999, -8.59402521, -8.5165511975, -8.37944817, -8.300650220000001, -8.581935415, -8.906270427499999, -8.876572845, -8.812342395, -8.9725199275, -9.186784585, -9.6090147225, -9.9257782, -10.016138752500002, -9.854661245, -9.884978162500001, -10.42567545, -11.099412565, -11.309853190000002, -11.223544727500002, -11.27178322, -11.9816820125, -13.01859746, -14.0355785275, -14.17155526, -13.713939522499999, -13.751830177499999, -14.849307005, -16.434728879999998, -17.9417305025, -17.701465915, -17.086313665000002, -17.777599815, -19.3921695475, -22.788027125, -25.526839825000003, -23.8486657075, -22.3820728475, -21.745833047500003, -22.844909565000002, -26.1874501725, -27.3950576925, -26.0234018075, -25.9072685575, -25.996036455, -30.778796032499997, -37.824928315, -40.36225194, -35.6941879875, -29.8170647325, -30.804015077500004, -34.113556259999996, -40.29908379, -39.66944332, -44.4540536975, -34.9752145975, -29.537346355, -26.25293398, -27.0948314225, -28.401201564999997, -26.778544009999997, -23.578168859999998, -21.727627802500002, -23.412819024999997, -26.2480283025, -25.0353983875, -22.2809693975, -20.814908935000002, -20.548265054999998, -23.254910345, -23.5587500875, -21.2105512, -19.12494823, -17.553828205, -18.687173927499998, -20.6190502575, -19.80033706, -18.182129999999997, -16.9996259875, -16.5479747675, -18.61072441, -19.2354199125, -18.0905535975, -16.6919741875, -15.048197945, -15.7148726225, -16.75653128, -16.259931587500002, -15.365818052500002, -14.024189867499999, -13.700621889999999, -15.4340249375, -16.137201909999998, -15.61166894])
    mag1 = mag - tunnelS11
    S11 = 10**mag
    S11_Sub = 10**mag1
#    print(S11, 'S11')
    S1.append(S11)
    S1_Sub.append(S11_Sub)
fig = plt.figure(901)
plt.title('Sheilding Effectivness Due To Absorption')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Shielding Due To Absorption (dB)')
SEA1 = np.log10((np.abs(S2[0])**2 / (1 - np.abs(S1[0])**2))**(-10))
plt.plot(x, SEA1, label = 'Sample1')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


SEA2 = np.log10((np.abs(S2[1])**2 / (1 - np.abs(S1[1])**2))**(-10))
plt.plot(x, SEA2, label = 'Sample2')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


SEA3 = np.log10((np.abs(S2[2])**2 / (1 - np.abs(S1[2])**2))**(-10))
plt.plot(x, SEA3, label = 'Sample3')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#SEA4 = -10 * log10(np.abs(S2[3])**2 / (1 - np.abs(S1[3])**2))
#plt.plot(x, SEA4, label = 'Sample4')
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

SEA5 = np.log10((np.abs(S2[4])**2 / (1 - np.abs(S1[4])**2))**(-10))
plt.plot(x, SEA5, label = 'Sample4')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

SEA1_Sub = np.log10((np.abs(S2_Sub[0])**2 / (1 - np.abs(S1_Sub[0])**2))**(-10))
plt.plot(x, SEA1_Sub, label = 'Subtracted 1')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


SEA2_Sub = np.log10((np.abs(S2_Sub[1])**2 / (1 - np.abs(S1_Sub[1])**2))**(-10))
plt.plot(x, SEA2_Sub, label = 'Subtracted 2')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


SEA3_Sub = np.log10((np.abs(S2_Sub[2])**2 / (1 - np.abs(S1_Sub[2])**2))**(-10))
plt.plot(x, SEA3_Sub, label = 'Subtracted 3')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#SEA4 = -10 * log10(np.abs(S2[3])**2 / (1 - np.abs(S1[3])**2))
#plt.plot(x, SEA4, label = 'Sample4')
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

SEA5_Sub = np.log10((np.abs(S2_Sub[4])**2 / (1 - np.abs(S1_Sub[4])**2))**(-10))
plt.plot(x, SEA5_Sub, label = 'Subtracted 4')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


print(S2_Sub[4])
plt.show()