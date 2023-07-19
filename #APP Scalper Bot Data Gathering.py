#APP Scalper Bot Data Gathering
import numpy as np
import seaborn as sns
#import matplotlib as plt#
import matplotlib.pyplot as plt
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
    '''
    def __init__(self, status):
        self.IArrivalT = None
        self.ServiceT = None
        self.status = status
        self.Power = None
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
        return str(self.IArrivalT) + ", " + str(self.ServiceT) + ", " + self.status + ", " + str(self.power)
    
    def takePower(self):
        if self.status == "human":
            self.Power = random.randint(1,5)
        if self.status == "autofill":
            self.Power = random.randint(1,5)
        if self.status == "bots":
            self.Power = random.randint(1,20)


class Queue():
    '''
    Class that defines the queue and the timing of different aspects 
    Initialization parameters - None
    '''
    def __init__(self, capacity):
        self.waitList = {}
        self.capacity = capacity 
        
        self.customerLine = []
        self.arrivalLine = []
        self.serviceLine = [] 
        self.departureLine = []
        self.waitLine = []
        self.powerLine = []
        self.statusLine = []

    def waitTime(self):
        '''
        '''
        self.departureLine.append(self.arrivalLine[0] + self.serviceLine[0])

        self.waitLine.append(0)

        if len(self.arrivalLine) == 0:
            return 0 
        else:
            for i in range(1, len(self.arrivalLine)):
                self.waitLine.append(self.departureLine[i-1] - self.arrivalLine[i])

                self.departureLine.append(self.departureLine[i-1] + self.serviceLine[i])
            
    
    def __str__(self):
        toPrint = "["
        Cust = "Customer " + str(len(self.waitList))
        for i in self.waitList:
            if Cust == i:
                toPrint = toPrint + i + "]"
            else:
                toPrint = toPrint + i + ", "
        return toPrint
    

    def generateCustomer(self, amount, status):   
        if status == "human":
            #Creates a human customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer("human")
                Cust.arrivalTime()
                Cust.serviceTime()
                Cust.takePower()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                self.powerLine.append(Cust.Power)
                self.statusLine.append(Cust.status)
                
        if status == "autofill":
            #Creates a autofill customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer("autofill")
                Cust.arrivalTime()
                Cust.serviceTime()
                Cust.takePower()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                self.powerLine.append(Cust.Power)
                self.statusLine.append(Cust.status)


            
        if status == "bots":
            #Creates a bots customer and calls back to the function to generate a arrival time and service time,
            #and append them to the customer. Customer holds arrival and service times values.
            for i in range(amount):    
                Cust = Customer("bots")
                Cust.arrivalTime()
                Cust.serviceTime()
                Cust.takePower()
                self.serviceLine.append(Cust.ServiceT)
                self.arrivalLine.append(Cust.IArrivalT)
                self.powerLine.append(Cust.Power)
                self.statusLine.append(Cust.status)

    def minusCap(self, ToTake):
        if self.capacity > 0:
            if self.capacity >= ToTake:
                self.capacity -= ToTake
            else:
                ToTake -= self.capacity
                self.capacity = 0
        else:
            return 0


    def appendQueue(self):
        length = len(self.waitList)
        Cust = "Customer " + str(len(self.waitList) + 1)
        self.waitList[Cust] = [self.arrivalLine[length], self.waitLine[length] ,self.serviceLine[length], self.departureLine[length], self.powerLine[length], self.statusLine[length]]


    def simulateQueue(self, amountH, amountA, amountB):
        self.generateCustomer(amountH, "human")
        self.generateCustomer(amountA, "autofill")
        self.generateCustomer(amountB, "bots")
        self.waitTime()
        
        for i in range((amountH + amountA + amountB)):
            self.appendQueue()
        CustomerList = list(self.waitList.keys())
        random.shuffle(CustomerList)
        #print(CustomerList)
        #for i in range(len(self.waitList)):
            #time.sleep(self.waitList[CustomerList[i]][0])
            #print ("b")
        served = []
        CustNum = 0
        flag = False
        '''
        while self.capacity > 0 and CustNum <= (len(self.waitList) - 1):
            if self.waitList[CustomerList[CustNum]][4] > self.capacity:
                self.waitList[CustomerList[CustNum]][4] -= self.capacity
                print("Customer " + str(CustNum + 1) + " did not get served completely. Missing " + str((self.waitList[CustomerList[CustNum]][4] - self.capacity)) + " resources.")
                self.capacity = 0 #correct this
                served.append(self.waitList[CustomerList[CustNum]])
                flag = True
            else:
                self.minusCap(CustNum)
            served.append(self.waitList[CustomerList[CustNum]])
            CustNum += 1
            if CustNum == len(self.waitList):
                break
        '''
        while flag == False:
            #print (str(self.capacity) + ": capacity")
            if (self.capacity <= 0) or (CustNum >= (len(self.waitList)-1)):
                flag = True
            elif self.waitList[CustomerList[CustNum]][4] > self.capacity:
                # print(str(CustNum) + "custNum")
                #print(str(self.waitList[CustomerList[CustNum]][4]) + ": Take Power(before)")
                self.waitList[CustomerList[CustNum]][4] = self.capacity
                #print(self.waitList[CustomerList[CustNum]][4])
                self.capacity = 0
                served.append(self.waitList[CustomerList[CustNum]])
                flag = True
            else:
                self.minusCap(self.waitList[CustomerList[CustNum]][4])
                served.append(self.waitList[CustomerList[CustNum]])
                CustNum += 1
            


        #print('a')
        notServed = []    
        for i in range(CustNum + 1, len(self.waitList)):
            notServed.append(self.waitList[CustomerList[i]])
        
        return [served, notServed, self.capacity]
        #print("a")

        
def splitServed(served):
    amountServed = [0,0]
    for i in range(len(served)):
        if served[i][5] == "bots":
            amountServed[0] += served[i][4]
        if served[i][5] == "human": 
            amountServed[1] += served[i][4]
        if served[i][5] == "autofill":
            amountServed[1] += served[i][4]
    return amountServed


def noServeSplit(notServed):
    amountNotServed = [0,0] 
    for i in range(len(notServed)):
        if notServed[i][5] == "bots":
            amountNotServed[0] += notServed[i][4]
        if notServed[i][5] == "human":
            amountNotServed[1] += notServed[i][4]
        if notServed[i][5] == "autofill":
            amountNotServed[1] += notServed[i][4]
    return amountNotServed        





humans = 60
bots = 20
autofill = 20

Q = Queue(300)

result = Q.simulateQueue(humans, bots, autofill)
#print(result) 
#print(splitServed(result[0]))
#print(noServeSplit(result[1]))


'''
Q.generateCustomer(2, "human")
Q.generateCustomer(2, "autofill")
Q.generateCustomer(2, "bots")
Q.waitTime()
for i in range(6):
    Q.appendQueue()

Q.minusCap(5)
print(Q.capacity)
'''
'''
print(Q)
print(Q.waitList["Customer 5"])
print(Q.waitLine)
print(Q.departureLine)
print(Q.serviceLine)
print(Q.arrivalLine)
print(Q.powerLine)
'''



#y = np.array(noServeSplit(result[1]))
#plt.pie(y)

 #Queue(30000)
humans1 = 10      #random.randint(17400,18600)
autofill1 = 5     #random.randint(5400,6600)
bots1 = 5         #random.randint(5400, 6600)

test_results_served_bots = []
test_results_served_ha = []
test_results_notServed_bots = []
test_results_notServed_ha = []


for i in range(10):
    print (i)
    test = Queue(50)
    test_results = test.simulateQueue(humans1,autofill1, bots1)
    t1_bots = splitServed(test_results[0])[0]
    t1_ha = splitServed(test_results[0])[1]
    t1_noBots = noServeSplit(test_results[1])[0]
    t1_noHa = noServeSplit(test_results[1])[1]

    test_results_served_bots.append(t1_bots)
    test_results_served_ha.append(t1_ha)
    test_results_notServed_bots.append(t1_noBots)
    test_results_notServed_ha.append(t1_noHa)



avg_S_bots = sum(test_results_served_bots) / (len(test_results_served_bots))
avg_S_ha = sum(test_results_served_ha) / (len(test_results_served_ha))
avg_NS_bots = sum(test_results_notServed_bots) / (len(test_results_notServed_bots))
avg_NS_ha = sum(test_results_notServed_ha) / (len(test_results_notServed_ha))



print(avg_S_bots)
print(avg_S_ha)
print(avg_NS_bots)
print(avg_NS_ha)
print(test_results_served_bots)
print(test_results_served_ha)
print(test_results_notServed_bots)
print(test_results_notServed_ha)



x = np.array([avg_S_bots,avg_S_ha,avg_NS_bots,avg_NS_ha])
myLabels = ["Bots ", "Human and Autofill", "Bots Not Served", "Humans and Autofill Not Served"]
myColors = ["Purple", "Orange","Green", "Blue"]
fracs = [avg_S_bots,avg_S_ha,avg_NS_bots,avg_NS_ha]
total = sum(fracs)



plt.pie(x, labels = myLabels, colors = myColors,
autopct=lambda p: '{:.0f}%'.format(p * total / 100))

plt.legend(title = "Bots served Vs Humans and Autofill users served")
plt.show()

