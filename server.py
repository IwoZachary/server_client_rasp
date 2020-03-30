import datetime
import os
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
    def __init__(self,):
        self.file=open("/home/iwo/Desktop/server_client/server_client_rasp/Unidentified/"+"Unauthorisied"+".txt","a")
        self.file.wirte("List of unauthorisied attempts to connect to the server valid from "+format(datetime.datetime.now())+'\n')
        self.file.close()
        self.setOfUnident={}
        print("Done1")
        
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
       # p=Unidentified()
       # self.unidentified=p
        
    def addWorker(self,cardNum,name):
        self.workerList.append(Worker(cardNum,name))
        #if cardNum in self.unidentified.setOfUnitendent:
           # self.unidentified.setOfUnitendent.remove(cardNum)
    
    def removeWorker(self,num):
        for el in self.workerList:
            if el.cardNumb ==num:
               # try:
                    
                    os.remove("/home/iwo/Desktop/server_client/server_client_rasp/workerFiles/"+format(el.cardNumb)+".txt")
                #except:
                    #print("Error occured during expeling "+el.name+" from work!")
                    self.workerList.remove(el)
        
   
s=Server()
s.addWorker(111,"Adam")
s.addWorker(112,"Wiki")
s.addWorker(123,"Iwo")
s.removeWorker(111)
            
        
                

    
    