#install the libraries - joblib, numpy
#this code takes the value from the sensor and predicts the hand gesture (among 6 classes), 
#using joblib to access the trained svm model and then sends the control signal to node mcu

import requests
import time
import joblib
import serial
import numpy as np
nodeMCU_ip = '172.20.10.5'  

Arduino = serial.Serial('COM24', 9600)

model_svm = joblib.load(r'INSERT_PATH_HERE_FOR_THIS_FILE\trained_model_svm2.pkl')


def classify_sensor_data(data):
    data = data.reshape(1, -1)  
    predicted_class = model_svm.predict(data)
    return predicted_class
 
# time.sleep(0.1)
   

if (Arduino.inWaiting()>0):
       

        myData = Arduino.readline()
        myData = str(Arduino.readline(), 'utf-8')
        myData = myData.strip('\r\n')
        data = [float(x) for x in myData.split()]
        data = np.asarray(data)
        print(f"Raw Sensor Data: {myData}")

        print(data)
        

        predicted_class = classify_sensor_data(data)
    
        print(f"Sensor Data: {data}, Predicted Class: {predicted_class}")
        if predicted_class == 0:
            cs = '0'
            print("Hold")
        elif predicted_class == 1:
            cs = '1'
            print("One")
        elif predicted_class == 2:
            cs = '2'
            print("Two")
        elif predicted_class == 3:
            cs = '3'
            print("Three")
        elif predicted_class == 4:
            cs = '4'
            print("Four")
        elif predicted_class == 5:
            cs = '5'
            print("Open")


        data_to_send = cs
        response = requests.post(f'http://{nodeMCU_ip}/send', data=data_to_send)
    

        if response.status_code == 200:
            print('Data sent successfully to NodeMCU')
        else:
            print('Failed to send data to NodeMCU')    
        
        
    
 






