from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,valor):
        nodo = No(valor)
        if self.inicio is None:
                self.inicio = nodo
                self.fim = nodo
        elif nodo.dado < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio.ant = nodo
            self.inicio = nodo
        elif nodo.dado > self.fim.dado:
            nodo.ant = self.fim
            self.fim.prox = nodo
            self.fim = nodo
        else:
            antTestado = self.inicio 
            aux = self.inicio.prox
            while aux:
                if nodo.dado < aux.dado:
                    nodo.prox = aux 
                    nodo.ant = antTestado  
                    antTestado.prox = nodo
                    aux.ant = nodo
                    break
                else:
                    antTestado = aux
                    aux = aux.prox
        self.imprimir()

    def imprimir(self):
        print("---------------------------------")
        if self.inicio is None:
            print( "Lista Encadeada está vazia!" )
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.prox

    def remover(self, valor):
        if self.inicio is not None:
            removeu = False 
            if self.inicio.dado == valor:
                self.inicio = self.inicio.prox
                if self.inicio == None:
                    self.fim = None
                else:
                    self.inicio.ant = None
                removeu = True
            else:
                antTestado = self.inicio
                aux = self.inicio.prox
                while aux is not None:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        antTestado = aux
                        aux = aux.prox
                if removeu:
                    print("Elemento ", valor, "removido")
                else:
                    print("Elemento não encontrado")
        self.imprimir()