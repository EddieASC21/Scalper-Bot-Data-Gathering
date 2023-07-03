#APP Scalper Bot Data Gathering
import numpy as np
import seaborn as sns
import matplotlib as plt
import random
import time

#Establish Customer Classes
class Customer():
    def __init__(self, ArrivalT, ServiceT, status, served):
        self.ArrivalT = None
        self.ServiceT = None
        self.status = status
        self.served = False
    #Calculate Arrival time, Service time per class

    def arrivalTime(self, status):
        if status == "human":
            self.ArrivalT = random.randint(30,60)
        if status == "autofill":
            self.ArrivalT = random.randint(45,75)
        if self == "bots": 
            self.ArrivalT = random.randint(90,180)
    
    def serviceTime(self, status):
        if status == "human":
            self.ServiceT = random.randint(60,120)
        if status == "autofill":
            self.ServiceT = random.randint(15,30)
        if status == "bots":
            self.ServiceT = random.randint(5,10)



class Queue():
    def __init__(self, waitList):
        self.WaitList = {}

    def waitTime(self, waitList):
        if len(self.WaitList) == 0:
            return 0 
        else:
            pass






wait = []
for i in range(random.randint(75,100)):    
    wait.append(Customer(Customer.arrivalTime(Customer.self, "human"), Customer.serviceTime(Customer.self, "human"), "human", False))       

for i in range(random.randint(50,75)):    
    wait.append(Customer(Customer.arrivalTime(Customer.self, "autofill"), Customer.serviceTime(Customer.self, "autofill"), "autofill", False))       
          
for i in range(random.randint(10,25)):    
    wait.append(Customer(Customer.arrivalTime(Customer.self, "bots"), Customer.serviceTime(Customer.self, "bots"), "bots", False))       
    
random.shuffle(wait)
