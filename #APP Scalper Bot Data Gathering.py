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
    def __init__(self, capacity, defense):
        self.waitList = {}
        self.capacity = capacity 
        self.defense = defense
        
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

    def simulateQueue_CA(self, amountH, amountA, amountB):
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
        notServed = []    
        
        while flag == False:
            #print (str(self.capacity) + ": capacity")
            if (self.capacity <= 0) or (CustNum >= (len(self.waitList)-1)):
                flag = True
            elif self.waitList[CustomerList[CustNum]][4] > self.capacity:
                # print(str(CustNum) + "custNum")
                if self.waitList[CustomerList[CustNum]][5] == "bots":
                    print("Final Bot Detected")
                    DefChance = random.randint(1,100)
                    if DefChance <= 25:
                        print("Final Bot removed")
                        notServed.append(self.waitList[CustomerList[CustNum]])
                        CustNum += 1
                        break 
                    else:
                        print("Final Bot Succeeded")
                        #print(str(self.waitList[CustomerList[CustNum]][4]) + ": Take Power(before)")
                        self.waitList[CustomerList[CustNum]][4] = self.capacity
                        #print(self.waitList[CustomerList[CustNum]][4])
                        self.capacity = 0
                        served.append(self.waitList[CustomerList[CustNum]])
                        flag = True
                        break
                else:
                    #print(str(self.waitList[CustomerList[CustNum]][4]) + ": Take Power(before)")
                    self.waitList[CustomerList[CustNum]][4] = self.capacity
                    #print(self.waitList[CustomerList[CustNum]][4])
                    self.capacity = 0
                    served.append(self.waitList[CustomerList[CustNum]])
                    flag = True
            else:
                if self.waitList[CustomerList[CustNum]][5] == "bots":
                        #print(" Bot Detected")
                        DefChance = random.randint(1,100)
                        if DefChance <= 25:
                            #print("Bot removed")
                            notServed.append(self.waitList[CustomerList[CustNum]])
                            CustNum += 1
                        else:
                            self.minusCap(self.waitList[CustomerList[CustNum]][4])
                            served.append(self.waitList[CustomerList[CustNum]])
                            CustNum += 1 
                else:
                    self.minusCap(self.waitList[CustomerList[CustNum]][4])
                    served.append(self.waitList[CustomerList[CustNum]])
                    CustNum += 1
            


        #print('a')
        for i in range(CustNum + 1, len(self.waitList)):
            notServed.append(self.waitList[CustomerList[i]])
        
        return [served, notServed, self.capacity]
        #print("a")
        
    def simulateQueue_PR(self, amountH, amountA, amountB):
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
        notServed = []    
        
        while flag == False:
            #print (str(self.capacity) + ": capacity")
            if (self.capacity <= 0) or (CustNum >= (len(self.waitList)-1)):
                flag = True
            elif self.waitList[CustomerList[CustNum]][4] > self.capacity:
                # print(str(CustNum) + "custNum")
                if self.waitList[CustomerList[CustNum]][5] == "bots":
                    print("Final Bot Detected")
                    DefChance = random.randint(1,100)
                    if DefChance <= 60:
                        print("Final Bot removed")
                        notServed.append(self.waitList[CustomerList[CustNum]])
                        CustNum += 1
                        break 
                    else:
                        print("Final Bot Succeeded")
                        #print(str(self.waitList[CustomerList[CustNum]][4]) + ": Take Power(before)")
                        self.waitList[CustomerList[CustNum]][4] = self.capacity
                        #print(self.waitList[CustomerList[CustNum]][4])
                        self.capacity = 0
                        served.append(self.waitList[CustomerList[CustNum]])
                        flag = True
                        break
                else:
                    #print(str(self.waitList[CustomerList[CustNum]][4]) + ": Take Power(before)")
                    self.waitList[CustomerList[CustNum]][4] = self.capacity
                    #print(self.waitList[CustomerList[CustNum]][4])
                    self.capacity = 0
                    served.append(self.waitList[CustomerList[CustNum]])
                    flag = True
            else:
                if self.waitList[CustomerList[CustNum]][5] == "bots":
                        #print(" Bot Detected")
                        DefChance = random.randint(1,100)
                        if DefChance <= 60:
                            #print("Bot removed")
                            notServed.append(self.waitList[CustomerList[CustNum]])
                            CustNum += 1
                        else:
                            self.minusCap(self.waitList[CustomerList[CustNum]][4])
                            served.append(self.waitList[CustomerList[CustNum]])
                            CustNum += 1 
                else:
                    self.minusCap(self.waitList[CustomerList[CustNum]][4])
                    served.append(self.waitList[CustomerList[CustNum]])
                    CustNum += 1
            


        #print('a')
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





#Queue(30000)
humans1 = 60      #random.randint(17400,18600)
autofill1 = 20     #random.randint(5400,6600)
bots1 = 20         #random.randint(5400, 6600)




def test1_simulation(): 
    test_results_served_bots = []
    test_results_served_ha = []
    test_results_notServed_bots = []
    test_results_notServed_ha = []
    humans = 600      #random.randint(17400,18600)
    autofill = 200     #random.randint(5400,6600)
    bots = 200        #random.randint(5400, 6600)

    for i in range(10):
        #print (i)
        test = Queue(1000, "None")
        test_results = test.simulateQueue(humans,autofill, bots)
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
    
    pie_ND = np.array([avg_S_bots,avg_S_ha,avg_NS_bots,avg_NS_ha])
    myLabels = ["Bots ", "Human and Autofill", "Bots Not Served", "Humans and Autofill Not Served"]
    myColors = ["#D0E1D4", "#457B9D","#EF6F6C", "#87C38F"]
    fracs = [avg_S_bots,avg_S_ha,avg_NS_bots,avg_NS_ha]
    total = sum(fracs)
    plt.pie(pie_ND, labels = myLabels, colors = myColors,
    autopct=lambda p: '{:.0f}%'.format(p * 100/ 100))
    plt.title("Bots served Vs Humans and Autofill users served")
    plt.show()


    bar_graph_x_ND = np.array(["Humans and \nAutofill Served", "Bots \nServed", "Humans and \nAutofill Not Served", "Bots Not \nServed"])
    bar_graph_y_ND = np.array([(sum(test_results_served_ha)),(sum(test_results_served_bots)),(sum(test_results_notServed_ha)),sum(test_results_notServed_bots)])
    plt.bar(bar_graph_x_ND,bar_graph_y_ND,color = "#8DB580")
    plt.title("Resources distributed in ten 100 capacity queue simulations")
    plt.show()


def test2_simulation():
    test2_results_served_bots = []
    test2_results_served_ha = []
    test2_results_notServed_bots = []
    test2_results_notServed_ha = []
    humans = 600      #random.randint(17400,18600)
    autofill = 200     #random.randint(5400,6600)
    bots = 200         #random.randint(5400, 6600)

    for i in range(10):
        #print (i)
        test2 = Queue(1000, "Captcha")
        test2_results = test2.simulateQueue_CA(humans,autofill, bots)
        t2_bots = splitServed(test2_results[0])[0]
        t2_ha = splitServed(test2_results[0])[1]
        t2_noBots = noServeSplit(test2_results[1])[0]
        t2_noHa = noServeSplit(test2_results[1])[1]


        test2_results_served_bots.append(t2_bots)
        test2_results_served_ha.append(t2_ha)
        test2_results_notServed_bots.append(t2_noBots)
        test2_results_notServed_ha.append(t2_noHa)



    avg_S_bots2 = sum(test2_results_served_bots) / (len(test2_results_served_bots))
    avg_S_ha2 = sum(test2_results_served_ha) / (len(test2_results_served_ha))
    avg_NS_bots2 = sum(test2_results_notServed_bots) / (len(test2_results_notServed_bots))
    avg_NS_ha2 = sum(test2_results_notServed_ha) / (len(test2_results_notServed_ha))

    print(avg_S_bots2)
    print(avg_S_ha2)
    print(avg_NS_bots2)
    print(avg_NS_ha2)
    print(test2_results_served_bots)
    print(test2_results_served_ha)
    print(test2_results_notServed_bots)
    print(test2_results_notServed_ha)


    #Graphs for CAPTCHA Defenses 
    plt.clf()
    pie_CA = np.array([avg_S_bots2,avg_S_ha2,avg_NS_bots2,avg_NS_ha2])
    myLabels_CA = ["Bots ", "Human and Autofill", "Bots Not Served", "Humans and Autofill Not Served"]
    myColors_CA = ["#317B22", "#E09F3E","#96C5F7", "#976391"]
    fracs = [avg_S_bots2,avg_S_ha2,avg_NS_bots2,avg_NS_ha2]
    total = sum(fracs)
    plt.pie(pie_CA, labels = myLabels_CA, colors = myColors_CA,
    autopct=lambda p: '{:.0f}%'.format(p * 100/ 100))
    plt.title("Bots served Vs Humans and Autofill users served with Captcha Defense")
    plt.show()

    bar_graph_x_CA = np.array(["Humans and \nAutofill Served", "Bots \nServed", "Humans and \nAutofill Not Served", "Bots Not \nServed"])
    bar_graph_y_CA = np.array([(sum(test2_results_served_ha)),(sum(test2_results_served_bots)),(sum(test2_results_notServed_ha)),sum(test2_results_notServed_bots)])
    plt.bar(bar_graph_x_CA,bar_graph_y_CA,color = "#F4D35E")
    plt.title("Resources distributed in ten 100 capacity queue simulations with Captcha Defense")
    plt.show()

def test3_simulation():
    test3_results_served_bots = []
    test3_results_served_ha = []
    test3_results_notServed_bots = []
    test3_results_notServed_ha = []
    humans = 600      #random.randint(17400,18600)
    autofill = 200     #random.randint(5400,6600)
    bots = 200         #random.randint(5400, 6600)


    for i in range(10):
        #print (i)
        test3 = Queue(1000, "Proxy")
        test3_results = test3.simulateQueue_PR(humans,autofill, bots)
        t3_bots = splitServed(test3_results[0])[0]
        t3_ha = splitServed(test3_results[0])[1]
        t3_noBots = noServeSplit(test3_results[1])[0]
        t3_noHa = noServeSplit(test3_results[1])[1]

        test3_results_served_bots.append(t3_bots)
        test3_results_served_ha.append(t3_ha)
        test3_results_notServed_bots.append(t3_noBots)
        test3_results_notServed_ha.append(t3_noHa)



    avg_S_bots3 = sum(test3_results_served_bots) / (len(test3_results_served_bots))
    avg_S_ha3 = sum(test3_results_served_ha) / (len(test3_results_served_ha))
    avg_NS_bots3 = sum(test3_results_notServed_bots) / (len(test3_results_notServed_bots))
    avg_NS_ha3 = sum(test3_results_notServed_ha) / (len(test3_results_notServed_ha))

    print(avg_S_bots3)
    print(avg_S_ha3)
    print(avg_NS_bots3)
    print(avg_NS_ha3)
    print(test3_results_served_bots)
    print(test3_results_served_ha)
    print(test3_results_notServed_bots)
    print(test3_results_notServed_ha)


    #Graphs for Proxy Defense 
    plt.clf()
    pie_PR = np.array([avg_S_bots3,avg_S_ha3,avg_NS_bots3,avg_NS_ha3])
    myLabels_PR = ["Bots ", "Human and Autofill", "Bots Not Served", "Humans and Autofill Not Served"]
    myColors_PR = ["#48BEFF", "#9A031E","#53A548", "#E7DFC6"]
    fracs = [avg_S_bots3,avg_S_ha3,avg_NS_bots3,avg_NS_ha3]
    total = sum(fracs)
    plt.pie(pie_PR, labels = myLabels_PR, colors = myColors_PR,
    autopct=lambda p: '{:.0f}%'.format(p * 100/ 100))
    plt.title("Bots served Vs Humans and Autofill users served with Proxy defense")
    plt.show()


    bar_graph_x_PR = np.array(["Humans and \nAutofill Served", "Bots \nServed", "Humans and \nAutofill Not Served", "Bots Not \nServed"])
    bar_graph_y_PR = np.array([(sum(test3_results_served_ha)),(sum(test3_results_served_bots)),(sum(test3_results_notServed_ha)),sum(test3_results_notServed_bots)])
    plt.bar(bar_graph_x_PR,bar_graph_y_PR,color = "#B20D30")
    plt.title("Resources distributed in ten 100 capacity queue simulations with Proxy Defense")
    plt.show()
