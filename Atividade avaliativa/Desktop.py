from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencia_da_fonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potencia_da_fonte  
    
   
    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte
    
    def setPotenciaDaFonte(self, value):
        self._potenciaDaFonte = value
    
    def getInformacoes(self):
        info = super().getInformacoes()
        info["potencia_da_fonte"] = self.getPotenciaDaFonte()
        return info
    
    def cadastrar(self):
        
        print(f"Desktop {self.modelo} cadastrado com sucesso :) ")
        return True