from abc import ABC 

class Cliente(ABC):
    def __init__(self, nome):
        self.nome = nome 
        self.__limite = 0.0 
        