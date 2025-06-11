import os
from Fila import Fila

fila = Fila()

op = -1

while op != 0:
    os.system('cls')
    print("---------------------------")
    print("1 - Adicionar na fila")
    print("2 - Remover da fila")
    print("3 - Imprimir fila")
    print("0 - Sair")
    op = int(input("Digite sua opção: "))
    if op == 1:
        dado = input("Digite o valor a ser inserido na Fila: ")
        fila.add(dado)
    elif op == 2:
        fila.remover()
    elif op == 3:
        fila.imprimir()
    elif op != 0:
        print("Opção Invalida!")
    input("")
