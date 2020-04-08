import datetime
import os
import time
import threading
from threading import Thread
import multiprocessing as mp
from multiprocessing import Process
from datetime import datetime
import csv


import paho.mqtt.client as mqtt
class Worker:
    def __init__(self,cardNumb,name):
        self.cardNumb=cardNumb
        self.name=name
        self.isPresent=False
        self.hour=0
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(cardNumb)+".txt","a")
            file.write(name+" added at "+dt_string+'\n')
            file.close()
        except:
           print("Worker init failed")
        print("Worker "+self.name+" added")
    def identified(self,name):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(self.cardNumb)+".txt","a")
            if self.isPresent==False:
                file.write("ARRIVE used station: "+name+ " at "+"|"+dt_string+"|")
                self.isPresent=True
            else:
                file.write("LEAVE used station: "+name+" at |"+dt_string+"|\n")
                self.isPresent=False
            file.close()
        except:
            print("ERROR")
    def p_hour(self):
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(self.cardNumb)+".txt","r")
            content=file.read().splitlines()
            for line in content:
                
                date=line.split("|")
                if len(date)>=4:
                    d1=date[1].replace("/"," ")
                    d1_2=d1.replace(":"," ")
                    fdate1=d1_2.split(" ")
                    d2=date[3].replace("/"," ")
                    d2_2=d2.replace(":"," ")
                    fdate2=d2_2.split(" ")
                    first=datetime(int(fdate1[2]),int(fdate1[1]),int(fdate1[0]),int(fdate1[3]),int(fdate1[4]),int(fdate1[5]))
                    second=datetime(int(fdate2[2]),int(fdate2[1]),int(fdate2[0]),int(fdate2[3]),int(fdate2[4]),int(fdate2[5]))
                    duration=second-first
                    dur_sec=duration.total_seconds()
                    dur_hour=(dur_sec/3600)
                    self.hour=self.hour+dur_hour
            file.close()
        except:
            print(str(self.cardNumb)+" counting hours went wrong")
class Unidentified:
    def __init__(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
            file.write("List of unauthorisied attempts to connect to the server valid from "+dt_string+'\n')
            file.close()
        except:
            print("Undefined list initializing faile")
        self.setOfUnident={0}
        print("Done")
        
    def addUndefined(self,num,name=""):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.setOfUnident.add(int(num))
        try:
            file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
            file.write(name+": "+format(num)+"  "+dt_string+'\n')
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
            client.subscribe("RFID")
    
        
        def on_message(client,userdata , message):
            print("message received " ,str(message.payload.decode("utf-8")))
            check=False
            number=message.payload.decode("utf-8").split(":")
            
            
            for el in self.workerList:
                if int(number[1])==el.cardNumb:
                    el.identified(number[0])
                    check=True
                    break
                    
            if check==False:
                
                self.unidentified.addUndefined(int(number[1]),number[0])
               
                   
        #broker_adress="192.168.69.139" //to od rasp
        broker_adress="192.168.233.128"
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message     
        client.connect(broker_adress)
        print("Welcome!!! Press 'help' if you don't know what to do!")
        while True:
            client.loop_start()
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
                print ("Press 'add' to add new employe or 'delete' to remove him or 'raport' to create csv file")
                print ("If you want to exit type 'end'")
            if command=="raport":
                self.create_raport()
            if command=="end":
                break
            client.loop_stop()
                

        
        
    def addWorker(self,cardNum,name):
       
        self.workerList.append(Worker(cardNum,name))
        if cardNum in self.unidentified.setOfUnident:
            self.unidentified.setOfUnident.remove(cardNum)
    
    def removeWorker(self,num):
        for el in self.workerList:
            if el.cardNumb ==num:
                try:
                    
                    os.remove("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(el.cardNumb)+".txt")
                    self.workerList.remove(el)
                    print("Done")
                    break
                except:
                    print("Error occured during expeling "+el.name+" from work!")
                    
    
    def create_raport(self):
        for worker in self.workerList:
            worker.p_hour()
        try:
            with open('raport.csv', 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['CardNumb', 'Name','HoursInWork'])
                for worker in self.workerList:
                    filewriter.writerow([worker.cardNumb , worker.name , int(worker.hour)])
            csvfile.close()
        except:
            print("Creating raport failed!")
            

        
            
                    
                
            
s=Server()

t1 = threading.Thread(target=s.connect())




            
        
                

    
    