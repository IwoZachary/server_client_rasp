import datetime
import os
import time
from threading import Thread
import paho.mqtt.client as mqtt
class Worker:
    def __init__(self,cardNumb,name):
        self.cardNumb=cardNumb
        self.name=name
        self.isPresent=False
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(cardNumb)+".txt","a")
            file.write(name+" added at "+format(datetime.datetime.now())+'\n')
            file.close()
        except:
           print("Worker init failed")
        print("Worker "+self.name+" added")
    def identified(self):
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(self.cardNumb)+".txt","a")
            if self.isPresent==False:
                file.write(" arrived at "+format(datetime.datetime.now()))
                self.isPresent=True
            else:
                file.write(" ||  log out at "+format(datetime.datetime.now())+'\n')
                self.isPresent=False
            file.close()
        except:
            print("ERROR")

class Unidentified:
    def __init__(self):
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
            file.write("List of unauthorisied attempts to connect to the server valid from "+format(datetime.datetime.now())+'\n')
            file.close()
        except:
            print("Undefined list initializing faile")
        self.setOfUnident={0}
        print("Done")
        
    def addUndefined(self,num):
        
        self.setOfUnident.add(int(num))
        #print("un")
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
            
            print(str(num))
            print(format(num))
            file.wirte(str(num))
            file.write("beka XD\n")
            print("b")
            file.close()
        except:
            print("Sorry an error occured, which can makes your list leaking data")

class Server:
    


    def __init__(self):
        self.workerList=[]
        self.unidentified=Unidentified()
        
        
        
    def connect(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))
            client.subscribe("test")
    
        
        def on_message(client,userdata , message):
            print("message received " ,str(message.payload.decode("utf-8")))
            check=False
            
            for el in self.workerList:
                #print("i")
                if int(message.payload.decode("utf-8"))==el.cardNumb:
                    #print("a")
                    el.identified()
                    check=True
                    break
                    
            if check==False:
                
                self.unidentified.addUndefined(int(message.payload.decode("utf-8")))
               
                   
        broker_adress="192.168.69.139"
        client = mqtt.Client()
        
        client.on_connect = on_connect
        client.on_message = on_message
        
        client.connect(broker_adress)
        client.loop_forever()
        

        
        
    def addWorker(self,cardNum,name):
        self.workerList.append(Worker(cardNum,name))
        #print(len(self.workerList))
        if cardNum in self.unidentified.setOfUnident:
            self.unidentified.setOfUnident.remove(cardNum)
    
    def removeWorker(self,num):
        for el in self.workerList:
            if el.cardNumb ==num:
                try:
                    
                    os.remove("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(el.cardNumb)+".txt")
                    self.workerList.remove(el)
                    print("Done")
                except:
                    print("Error occured during expeling "+el.name+" from work!")
                    
    def reading_func(self):
        print("Welcome!!! Press 'help' if you don't know what to do!")
        while True:
            command = input()
            if command=="add":
                name=input("New Worker name: ")
                cardNum=input("Workers assigned card: ")
                try:
                    self.addWorker(int(cardNum),name)
                except:
                    print("Try again")
            
            if command=="delete":
                cardNum=input("Woreker assigned card: ")
                try:
                    self.removeWorker(int(cardNum))
                except:
                    print("Try again")
            if command=="help":
                print ("Press 'add' to add new employe or 'delete' to remove him")
                print ("If you want to exit type 'end'")
                
            if command=="end":
                break
                    
                
            
s=Server()
s.addWorker(123,"Marek")
s.addWorker(124,"Wika")
#s.reading_func()
s.connect()



            
        
                

    
    