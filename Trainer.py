from employe import Employee 
from ir import IR

class Trainer(Employee, IR):
    def __init__(self, mtle=0, nom="namms", dateNaissance="31/05/2005", dateEmbauche="10/05/2024", salaireBase=4000):
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.__heureSup = 0
        self.__tarifHsup = 30
    
    @property
    def getheureSup(self):
        return self.__heureSup
    
    @property
    def gettarifHsup(self):
        return self.__tarifHsup
    
    def setheureSup(self, new_hs):
        self.__heureSup = new_hs
    
    def settarifHsup(self, new_ths):
        self.__tarifHsup = new_ths
    
    def __str__(self):
        return super().__str__() + f"Number of overtime hours per month: {self.getheureSup} - Remuneration per overtime hour: {self.gettarifHsup}"

    def getIR(self, salaire):
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        return (self.getsalaireBase + self.getheureSup * self.gettarifHsup) * (1 - self.getIR(self.getsalaireBase))