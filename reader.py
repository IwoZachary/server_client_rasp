import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")
def on_message(client,userdata , message):
            print("message received " ,str(message.payload.decode("utf-8")))
            
broker_adress="192.168.69.139"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_adress)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()