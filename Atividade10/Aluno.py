from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, cpf: str, nome: str, matricula: str, curso: str):
        super().__init__(cpf, nome, matricula)
        self.__curso = curso

   
    def macroinventora(self):
        print("Método implementado para Aluno")

    
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: str):
        self.__curso = curso

