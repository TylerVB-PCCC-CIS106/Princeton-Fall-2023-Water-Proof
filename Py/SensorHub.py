import serial
import numpy as np
import time
from datetime import date
import requests

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



class SensorHub:
    recordDate = date.today()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    url = ""
    ph = 0.0
    city = "Paterson"
    def __init__(self, vec, running):
        self.vec = np.array(vec)
        self.running = running

        
        
    def mintNFT(self):
       url = "https://api.verbwire.com/v1/nft/mint/quickMintFromFile"

       files = {"filePath": ("Log.txt", open("Log.txt", "rb"), "text/plain")}
       payload = {
           "allowPlatformToOperateToken": "true",
            "chain": "goerli",
            "name": "Sensor",
            "description": "Sensor data collected on " + str(self.recordDate),
            "data": [{"trait_type": "City","value": self.city},{"trait_type": "Date","value": str(self.recordDate)}]
    
            
            
        }
       headers = {
            "accept": "application/json",
            "X-API-Key": "sk_live_990a5e0b-ae24-49fc-bd59-bd903693aa4a"
        }
        
       response = requests.post(url, data=payload, files=files, headers=headers)
        
       print(response.text)
                

    def activeSensor(self):
        #while self.running:
        ser = serial.Serial("/dev/ttyACM0")
        time.sleep(0) #take a reading every 30 minutes
        pH = float(ser.readline())
        f = open("Log.txt", 'w')
        f.write("PH:" + str(5.55))
        f.write("\nDate::" +str(self.recordDate))
        f.write("\nTime:" + self.current_time)
        f.close()
        self.mintNFT()


test = SensorHub([1, 2, 3, 4],True)
test.activeSensor()




