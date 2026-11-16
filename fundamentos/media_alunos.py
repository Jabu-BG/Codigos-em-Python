from dataclasses import dataclass
@dataclass


class Aluno:
    nome: str
    idade: int
    notas: list
    def media(self):
        return sum(self.notas) / len(self.notas)
    
if __name__ == "__main__":
    aluno1 = Aluno("Raphael", 41, [9.5, 8.7, 7.2])
    aluno2 = Aluno("Caroline", 32, [10, 4.2, 6.7])
    lista_alunos = [aluno1, aluno2]
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome}, Media: {aluno.media():.2f}")
