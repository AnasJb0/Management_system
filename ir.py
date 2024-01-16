from abc import (ABC, abstractmethod)

class IR(ABC):
    _tranches = [0,400, 5001, 1000]
    _tauxIR = [0, 10, 26, 30, 64, 70]

    @classmethod
    @abstractmethod
    def getIR(cls, salaire):
        pass