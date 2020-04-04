import paho.mqtt.client as mqtt
import time
def on_message(client,userdata , message):
            print("message received " ,str(message.payload.decode("utf-8")))
            
broker_adress="192.168.233.128"
client = mqtt.Client("P1") #create new instance
client.connect(broker_adress) #connect to broker
client.subscribe("test")
client.on_message=on_message
while True:
    client.loop_start()
    #client.subscribe("test")
    client.on_message=on_message