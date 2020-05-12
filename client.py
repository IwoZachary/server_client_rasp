import paho.mqtt.client as mqtt
import time
import os
broker_adress="DESKTOP-F4BSBEP" #Maszyna na której jest zainstalowany broker
port=8883                        #port z którego korzysta broker
print("Identyficator of workstation> ")
name=input()                      #nazwa terminala
client = mqtt.Client("P1")       #stworzenie instacji klienta
client.tls_set("ca.crt")          #wykorzystanie certyfiaktu ca.crt wymaganego przez broker
client.username_pw_set(username='client', password='iwo123')       #autoryzacja użytkownika
client.connect(broker_adress,port)          #połaczenie do brokera
while True:
    number=input()
    if number:
        client.publish("RFID",name+":"+number)
        time.sleep(1)
