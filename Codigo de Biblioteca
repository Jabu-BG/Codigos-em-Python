class Livro():
    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def lista_livros(self):
        print(f"Livro: {self.titulo} / Autor: {self.autor} / Ano: {self.ano} / Status: {self.disponivel}")

    def emprestar_livro(self):
        if self.disponivel == True:
            print(f"Livo Emprestado!")
        else:
             print(f"Livro Indisponível")

    def devolver_livro(self):
        if self.disponivel == False:
            print(f"Livro devolvido!")
        else:
            print(f"Livro já está na Biblioteca")


livro1 = Livro("Harry Potter","J.K Rowling","1997", True)
livro2 = Livro("Jujutsu Kaisen", "Gege Akutami", "2018", False)
livro3 = Livro("Dom Casmurgo", "Machado de Assis", "1899", False)

lista_livros = [livro1, livro2, livro3]

livro2.devolver_livro()



