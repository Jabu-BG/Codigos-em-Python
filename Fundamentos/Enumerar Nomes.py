caminho_arquivo = 'Aula 01/Aula/dados.txt'

def escreve_linhas():
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("Raphael")
        arquivo.writelines(["\nBorges", "\nEduardo", "\nBruno", "\nMarcelão"])

def ler_linhas():
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:

        linha1 = arquivo.readline()
        print(f'Linha 1: {linha1}')

        linha2 = arquivo.readline()
        print(f'Linha 2: {linha2}')

        linha3 = arquivo.readline()
        print(f'Linha 3: {linha3}')

        linha4 = arquivo.readline()
        print(f'Linha 4: {linha4}')

def enumerar():
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        for i, linha in enumerate(linhas, start=1):
            print(f'Linha {i}: {linha}')


if __name__ == "__main__":
    escreve_linhas()
    enumerar()
