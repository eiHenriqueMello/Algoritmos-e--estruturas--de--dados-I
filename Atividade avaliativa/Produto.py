from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria
    
   
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, value):
        self._modelo = value
        
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, value):
        self._cor = value
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, value):
        self._preco = value
        
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, value):
        self._categoria = value
    
    def getInformacoes(self):
        return {
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria": self.categoria.nome
        }
    
    @abstractmethod
    def cadastrar(self):
        pass