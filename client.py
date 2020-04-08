import paho.mqtt.client as mqtt
import time
import os
broker_adress="192.168.69.139"
print("Identyficator of workstation> ")
name=input()
client = mqtt.Client("P1") #create new instance
client.connect(broker_adress) #connect to broker
while True:
    number=input()
    if number:
        client.publish("RFID",name+":"+number)
        time.sleep(5)
