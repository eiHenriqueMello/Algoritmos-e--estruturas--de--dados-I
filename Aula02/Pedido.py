from Pessoa import Pessoa
from Produto import Produto
from datetime import date

class Pedido:
    def __init__(self, data = date.today(), cli = Pessoa("Balcao") ) :
        self.id = None
        self.data = data
        self.cliente = cli 
        self.produtos = []

    def addProd(self, prod):
        if prod != None and prod.preco >= 10:
            self.produto.append(prod)

        soma = 0.0
        for p in self.produtos:
            soma += p.preco
        return soma

    def  __str__(self):
        txt = "Pedido realizado em: " + str(self.data)
        txt += "\nCliente: " + self.cliente.nome
        txt += "\nCliente: " + str(self.cliente)
        txt += "\nProdutos: "
        for p in self.produtos:
            txt += str( p )