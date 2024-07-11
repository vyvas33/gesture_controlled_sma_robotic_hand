import requests
import joblib
import serial
import numpy as np
import time

nodeMCU_ip = '172.20.10.5'
Arduino = serial.Serial('COM24', 9600)

model_svm = joblib.load(r'INSERT_PATH_HERE_FOR_THIS_FILE\trained_model_svm2.pkl')

def classify_sensor_data(data):
    data = data.reshape(1, -1)
    predicted_class = model_svm.predict(data)
    return predicted_class

start_time = time.time()

while True:
    if Arduino.inWaiting() > 0:
        myData = Arduino.readline()
        myData = str(myData, 'utf-8').strip('\r\n')
        data = [float(x) for x in myData.split()]
        data = np.asarray(data)
        print(f"Raw Sensor Data: {data}")

        predicted_class = classify_sensor_data(data)

        print(f"Sensor Data: {data}, Predicted Class: {predicted_class}")
        if predicted_class == 0:
            cs = '0'
            print("Control: Hold")
        elif predicted_class == 1:
            cs = '1'
            print("Control: One")
        elif predicted_class == 2:
            cs = '2'
            print("Control: Two")
        elif predicted_class == 3:
            cs = '3'
            print("Control: Three")
        elif predicted_class == 4:
            cs = '4'
            print("Control: Four")
        elif predicted_class == 5:
            cs = '5'
            print("Control: Open")

        
        data_to_send = cs
        response = requests.post(f'http://{nodeMCU_ip}/send', data=data_to_send)
        
        if response.status_code == 200:
           print('Data sent successfully to NodeMCU')
        else:
           print('Failed to send data to NodeMCU')

        break  # Break out of the loop after printing the data once

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")
