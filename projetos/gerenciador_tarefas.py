from dataclasses import dataclass
@dataclass

class Task:
    titulo: str
    tarefas: list

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar(self):
        print(f"\nLista: {self.titulo}")
        for tarefa in self.tarefas:
            print(f"- {tarefa}")

if __name__ == "__main__":

    lista = Task("Minhas tarefas", [])

    lista.adicionar("Estudar Python")
    lista.adicionar("Fazer exercício")
    lista.adicionar("Ler um livro")

    lista.listar()
