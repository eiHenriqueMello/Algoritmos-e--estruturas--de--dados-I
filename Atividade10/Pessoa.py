from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, cpf: str, nome: str, matricula: str):
        self.__cpf = cpf  
        self._nome = nome  
        self.__matricula = matricula 

   
    @abstractmethod
    def macroinventora(self):
        pass

    
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula


    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

