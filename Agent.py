from employe import Employee
from ir import IR
class Agent(Employee, IR):
    def __init__(self, mtle=0, nom="hamms", dateNaissance="31/10/2005", dateEmbauche="10/05/2024", salaireBase=4000, primeResponsabilite=0):
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.primeResponsabilite = primeResponsabilite

    def getIR(self, salaire):
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        return (self.getsalaireBase + self.primeResponsabilite) * (1 - self.getIR(self.getsalaireBase))
