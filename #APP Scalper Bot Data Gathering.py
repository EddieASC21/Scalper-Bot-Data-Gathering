#APP Scalper Bot Data Gathering
import numpy as np
import seaborn as sns
import matplotlib as plt
import random

#Establish Customer Classes
class Customer():
    def __init__(self, ArrivalT, ServiceT):
        self.ArrivalT = None
        self.ServiceT = None
    
class Human(Customer):
    def __init__(self, ArrivalT, ServiceT):
        super().__init__(ArrivalT= ArrivalT, ServiceT= ServiceT)

class Bot(Customer):
    def __init__(self, ArrivalT, ServiceT):
        super().__init__(ArrivalT= ArrivalT, ServiceT= ServiceT)

class Autofill(Customer):
    def __init__(self, ArrivalT, ServiceT):
        super().__init__(ArrivalT= ArrivalT, ServiceT= ServiceT)
