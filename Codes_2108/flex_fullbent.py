
#sensor-->arduino--->python---->prediction---->arduino---->actuation

import serial
import time
import numpy as np
import csv
Arduino = serial.Serial('COM24', 9600)
time.sleep(1)

f = open("fullBent.csv", "w", newline = '')
f.truncate()
#kmax = 5
while(True):
#for k in range(kmax):

    if (Arduino.inWaiting()>0):
    
        myData = Arduino.readline()
        myData = str(Arduino.readline(), 'utf-8')
        myData = myData.strip('\r\n')
        dataArray = [float(x) for x in myData.split()]
        print(dataArray) 
        f = open("fullBent.csv", "a", newline = '')
        writer = csv.writer(f, delimiter=",")
        writer.writerow(dataArray) 


f.close() 

