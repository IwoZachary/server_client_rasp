import paho.mqtt.client as mqtt
import time
broker_adress="192.168.69.139"
client = mqtt.Client("P1") #create new instance
client.connect(broker_adress) #connect to broker
#while True:
client.publish("test","hello5")
time.sleep(2)