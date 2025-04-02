# MÉTODO SEM PARÂMETRO E SEM RETORNO 

# def imprimirNomeProf():
#     print("Henrique")

# #MÉTODO QUE TEM RETORNO E NãO RECEBE PARÂMETRO 

# def getPI(): 
#     return 3.1415

# #MÉTODO QUE RECEBE PARÂMETRO E POSSUI RETORNO 

#     def calcAreCirculo(raio):
#         area = getPI() * raio * raio 
#         return area 

# #MÉTODO QUE RECEBE PARÂMETRO E NÃO TEM RETORNO 

#     def imprimirAreaCirculo(raio):
#         print("Área: ", calcAreaCirculo(raio))
    
##################################################################################################################################################################################
# Construa uma classe chamada Carro que possui os atributos modelo ano e quilometragem.
# Esta classe também deve conter um metodo para incrementar a quilometragem e um método para imprimir os dados de todos atributos do objeto carro 

# class Carros:
#     def __init__(self, modelo, ano, quilometragem):
#         self.modelo = modelo            #atributos
#         self.ano = ano 
#         self.quilometragem = quilometragem
          
#     def inc_quilometragem(self, distancia):
#         if distancia > 0:
#             self.quilometragem += distancia
#         else:
#             print("Distancia")
#     def imprimir_dados(self):
#         print (f"Modelo: {self.modelo}")
#         print (f"Ano: {self.ano}")
#         print (f"Quilometragem: {self.quilometragem} km")        


# # Exemplo 
# meu_car = Carros("M5", 2024, 24000)
# meu_car.imprimir_dados()

# # Incrementa a quilometragem
# meu_car.inc_quilometragem(20000)
# meu_car.imprimir_dados()

###########################################################################################################################


class Carro:

    def __init__(self, modelo = None, ano = 2025):
        self.modelo = modelo
        self.ano = ano
        self.__kilometragem = 0

    def incrementar(self, km):
        if km > 0:
            self.__kilometragem

    def setKM(self, km):
        # if km > self.__kilometragem:
            self.__kilometragem = km

    def __str__(self):
        txt = "Modelo: " + self.modelo
        txt += "\nAno: " + str(self.ano)
        txt += "\nKilometragem: " + str(self.__kilometragem)
        return txt
        
    def imprimir(self):
        print(self)
        
        

X = Carro("Doblo", 2025)
print(X)



