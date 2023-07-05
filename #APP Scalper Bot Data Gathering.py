#APP Scalper Bot Data Gathering
import numpy as np
import seaborn as sns
import matplotlib as plt
import random
import time

#Establish Customer Classes
class Customer():
    '''
    Class that defines the different types of customers to be processed in the queue.
    Initialization Parameters:
    IArrivalT - None,
    ServiceT - None,
    status - string,
    served - boolean
    '''
    def __init__(self, IArrivalT, ServiceT, status, served):
        self.IArrivalT = None
        self.ServiceT = None
        self.status = status
        self.served = False
    #Calculate Arrival time, Service time per class

    def arrivalTime(self):
        '''
        Randomly generates the arrival time of the current customer object, differentiated by class.
        
        Arguments: None
        Returns: None
        '''
        if self.status == "human":
            self.IArrivalT = random.randint(30,60)
        if self.status == "autofill":
            self.IArrivalT = random.randint(45,75)
        if self.status == "bots": 
            self.IArrivalT = random.randint(90,180)
    
    def serviceTime(self):
        '''
        Randomly generates the service time of the current customer object, differentiated by class.
        
        Arguments: None
        Returns: None
        '''
        if self.status == "human":
            self.ServiceT = random.randint(60,120)
        if self.status == "autofill":
            self.ServiceT = random.randint(15,30)
        if self.status == "bots":
            self.ServiceT = random.randint(5,10)
    
    def __str__(self):
        return str(self.IArrivalT) + ", " + str(self.ServiceT) + ", " + self.status + ", " + str(self.status)



class Queue():
    '''
    Class that defines the queue and the timing of different aspects 
    Initialization parameters - None
    '''
    def __init__(self):
        self.waitList = {}
        self.arrivalLine = []
        self.serviceLine = [] 
        self.departureLine = []
        self.waitLine = []
        

    def waitTime(self):
        '''
        '''
        if len(self.waitList) == 0:
            return 0 
        else:
            for i in range(len(self.waitList)):
                self.departureLine.append(self.arrivalLine[0] + self.serviceLine[0])

                self.waitLine.append(self.departureLine[i-1] - self.arrivalLine[i])

                self.departureLine.append(self.arrivalLine[i] + self.serviceLine[i] + self.waitLine[i])
            
    
    def __str__(self):
        toPrint = ""
        for i in self.waitList:
            toPrint = toPrint + i + " "
        return toPrint
    

    def generateCustomer(self, amount, status):   
        if status == "human":
            #Creates a human customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "human",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                
        if status == "autofill":
            #Creates a autofill customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "autofill",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
            
        if status == "bots":
            #Creates a bots customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "bots",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                
    def appendQueue(self):
        Cust = "Customer " + (len(self.waitList) + 1)
        self.waitList[Cust] = [self.arrivalLine[len(self.waitList)], self.serviceLine[len(self.waitList)], self.waitLine[len(self.waitList)], self.departureLine[len(self.waitList)]]

Q = Queue()
Q.generateCustomer(1, "human")
print(Q.serviceLine[0])
#APP Scalper Bot Data Gathering
import numpy as np
import seaborn as sns
import matplotlib as plt
import random
import time

#Establish Customer Classes
class Customer():
    '''
    Class that defines the different types of customers to be processed in the queue.
    Initialization Parameters:
    IArrivalT - None,
    ServiceT - None,
    status - string,
    served - boolean
    '''
    def __init__(self, IArrivalT, ServiceT, status, served):
        self.IArrivalT = None
        self.ServiceT = None
        self.status = status
        self.served = False
    #Calculate Arrival time, Service time per class

    def arrivalTime(self):
        '''
        Randomly generates the arrival time of the current customer object, differentiated by class.
        
        Arguments: None
        Returns: None
        '''
        if self.status == "human":
            self.IArrivalT = random.randint(30,60)
        if self.status == "autofill":
            self.IArrivalT = random.randint(45,75)
        if self.status == "bots": 
            self.IArrivalT = random.randint(90,180)
    
    def serviceTime(self):
        '''
        Randomly generates the service time of the current customer object, differentiated by class.
        
        Arguments: None
        Returns: None
        '''
        if self.status == "human":
            self.ServiceT = random.randint(60,120)
        if self.status == "autofill":
            self.ServiceT = random.randint(15,30)
        if self.status == "bots":
            self.ServiceT = random.randint(5,10)
    
    def __str__(self):
        return str(self.IArrivalT) + ", " + str(self.ServiceT) + ", " + self.status + ", " + str(self.status)



class Queue():
    '''
    Class that defines the queue and the timing of different aspects 
    Initialization parameters - None
    '''
    def __init__(self):
        self.waitList = {}
        self.arrivalLine = []
        self.serviceLine = [] 
        self.departureLine = []
        self.waitLine = []
        

    def waitTime(self):
        '''
        '''
        if len(self.waitList) == 0:
            return 0 
        else:
            for i in range(len(self.waitList)):
                self.departureLine.append(self.arrivalLine[0] + self.serviceLine[0])

                self.waitLine.append(self.departureLine[i-1] - self.arrivalLine[i])

                self.departureLine.append(self.arrivalLine[i] + self.serviceLine[i] + self.waitLine[i])
            
    
    def __str__(self):
        toPrint = ""
        for i in self.waitList:
            toPrint = toPrint + i + " "
        return toPrint
    

    def generateCustomer(self, amount, status):   
        if status == "human":
            #Creates a human customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "human",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                
        if status == "autofill":
            #Creates a autofill customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "autofill",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
            
        if status == "bots":
            #Creates a bots customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer(0, 0, "bots",False)
                Cust.arrivalTime()
                Cust.serviceTime()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                
    def appendQueue(self):
        Cust = "Customer " + (len(self.waitList) + 1)
        self.waitList[Cust] = [self.arrivalLine[len(self.waitList)], self.serviceLine[len(self.waitList)], self.waitLine[len(self.waitList)], self.departureLine[len(self.waitList)]]

Q = Queue()
Q.generateCustomer(1, "human")
print(Q.serviceLine[0])

