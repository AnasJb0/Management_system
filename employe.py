from IEmployee import IEmployee
from abc import ABC, abstractmethod

class Employee(IEmployee, metaclass=ABC):
    _counter = 0
    def __init__(self, mtle=0, nom="El Kelkha", dateNaissance="31/03/2005", dateEmbauche="12/01/2024", salaireBase=7000):
        Employee._counter += 1
        self.__mtle = Employee._counter
        self.__nom = nom
        self.__dateNaissance = dateNaissance
        self.__dateEmbauche = dateEmbauche
        self.__salaireBase = salaireBase
    
    @property
    def getmtle(self): 
        return self.__mtle
    
    @property
    def getnom(self):
        return self.__nom
    
    @property
    def getdateNaissance(self):
        return self.__dateNaissance
    
    @property
    def getdateEmbauche(self):
        return self.__dateEmbauche
    
    @property
    def getsalaireBase(self):
        return self.__salaireBase
    
    def setmtle(self, new_mtle):
        self.__mtle = new_mtle
    
    def setnom(self, new_nom):
        self.__nom = new_nom
    
    def setdateNaissance(self, new_dateNaissance):
        self.__dateNaissance = new_dateNaissance
    
    def setsalaireBase(self, new_salaireBase):
        self.__salaireBase = new_salaireBase
    
    
    @abstractmethod
    def salaireAPayer(self):
        pass

    
    def __str__(self):
        return f"Employee ID: {self.getmtle} - Name: {self.getnom} - Date of Birth: {self.getdateNaissance} - Employment Date: {self.getdateEmbauche} - Base Salary: {self.getsalaireBase} - "
    
    def __eq__(self, other):
        return self.getmtle == other.getmtle