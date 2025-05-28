from Aluno import Aluno


if __name__ == "__main__":
   
    aluno = Aluno(cpf="315.253.790-46", 
                 nome="Jóca Monteiro", 
                 matricula="3469752164", 
                 curso="Redes de telefone sem fio")
    
    
    print(f"Nome: {aluno.nome}")
    print(f"CPF: {aluno.cpf}")
    print(f"Matrícula: {aluno.matricula}")
    print(f"Curso: {aluno.curso}")
    
   
    aluno.matricula = "35495521546"
    print(f"Nova matrícula: {aluno.matricula}")
    
    
    aluno.nome