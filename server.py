import datetime
import os
from threading import Thread
import paho.mqtt.client as mqtt
class Worker:
    def __init__(self,cardNumb,name):
        self.cardNumb=cardNumb
        self.name=name
        self.isPresent=False
        self.file=open("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(cardNumb)+".txt","a")
        self.file.write(name+" added at "+format(datetime.datetime.now())+'\n')
        self.file.close()
        print("Done")

class Unidentified:
    def __init__(self):
        self.file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
        self.file.write("List of unauthorisied attempts to connect to the server valid from "+format(datetime.datetime.now())+'\n')
        self.file.close()
        self.setOfUnident={}
        print("Done")
        
    def addUndefined(self,cardNumb):
        self.setOfUnitendent.add(cardNumb)
        try:
            self.file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
            self.file.wirte(format(cardNumb)+"  "+format(datetime.datetime.now())+'\n')
            self.file.close()
        except:
            print("Sorry an error occured, which can makes your list leaking data")

class Server:
    


    def __init__(self):
        self.workerList=[]
        self.undidentified=Unidentified()
        

    
        
    def addWorker(self,cardNum,name):
        self.workerList.append(Worker(cardNum,name))
        if cardNum in self.unidentified.setOfUnitendent:
            self.unidentified.setOfUnitendent.remove(cardNum)
    
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
s.reading_func()



            
        
                

    
    