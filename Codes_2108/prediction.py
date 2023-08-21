
#this code takes the value from the sensor and predicts the bend angle (among 3 classes), using joblib to access the svm model 

import time
import joblib
import serial
import numpy as np
Arduino = serial.Serial('COM24', 9600)

model_svm = joblib.load(r'C:\Users\vyvas\Desktop\BTP\Codes\Serial\trained_svm.pkl')

def classify_sensor_data(data):
    data = data.reshape(1, -1)  
    predicted_class = model_svm.predict(data)
    return predicted_class
 
while True:

    if (Arduino.inWaiting()>0):
    
        myData = Arduino.readline()
        myData = str(Arduino.readline(), 'utf-8')
        myData = myData.strip('\r\n')
        data = [float(x) for x in myData.split()]
        data = np.asarray(data)


        predicted_class = classify_sensor_data(data)
    
        print(f"Sensor Data: {data}, Predicted Class: {predicted_class}")
        if predicted_class == 0:
            cs = 'A'
            print("No bend")
        elif predicted_class == 1:
            cs = 'B'
            print("Half bent")
        elif predicted_class == 2:
            cs = 'C'
            print("Fully bent")

        Arduino.write(cs.encode())
        
    
    time.sleep(1) 
