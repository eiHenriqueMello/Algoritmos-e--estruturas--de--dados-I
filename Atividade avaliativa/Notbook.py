from Produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempo_de_bateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempo_de_bateria 
    
    
    def getTempoDeBateria(self):
        return self.__tempoDeBateria
    
    def setTempoDeBateria(self, value):
        self.__tempoDeBateria = value
    
    def getInformacoes(self):
        info = super().getInformacoes()
        info["tempo_de_bateria"] = self.getTempoDeBateria()
        return info
    
    def cadastrar(self):
        print(f"Notebook {self.modelo} cadastrado com sucesso!")
        return True