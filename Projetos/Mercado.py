produtos = {
    "Arroz 5kg = ": 25.50,
    "Feijão 1kg = ": 8.90,
    "Macarrão 500g = ": 4.75,
    "Óleo de soja 900ml = ": 7.20,
    "Leite 1L = ": 4.50,
    "Pão francês 1kg = ": 15.00,
    "Manteiga 200g = ": 12.30,
    "Queijo muçarela 500g = ": 28.90,
    "Café 500g = ": 18.50,
    "Açúcar 1kg = ": 5.20,
    "Sal 1kg = ": 2.80,
    "Refrigerante 2L = ": 9.90,
    "Suco de laranja 1L = ": 6.50,
    "Frango kg = ": 14.90,
    "Carne bovina kg = ": 39.90,
    "Ovos 12 unidades = ": 10.50,
    "Tomate kg = ": 8.00,
    "Batata kg = ": 4.50,
    "Cebola kg = ": 3.90,
    "Alface unidade = ": 2.50
}

# Basicamente encurta os nomes dos produtos
produtosCurto = {resumo.split()[0]: resumo for resumo in produtos}

 # Armazena os itens adicionados no Carrinho.
carrinho = {}

# Mostra os produtos com preço e tudo mais
def mostrarProdutos():
    print("\nLista de Produtos:")
    for produto, preco in produtos.items():
        print(f"{produto} R${preco:.2f}")

# Basicamente o sistema de adicionar no carrinho, junto com o quanto de quantidade você deseja.
def adicionarCarrinho():
    mostrarProdutos()
    produtoSaida = input("\nDigite o nome do produto que deseja adicionar: ")
    if produtoSaida in produtosCurto:
        produtoCompleto = produtosCurto[produtoSaida]
        
        # Têm também um leve tratamento de erro, impedindo o cabra colocar menos que 0 na quantidade e de colocar numero invalido, como letras e tals. Ele deve colocar o nome do produto, se não, não funfa
        try:
            quantidade = int(input(f"Quantos {produtoCompleto} deseja adicionar? "))
            if quantidade > 0:
                carrinho[produtoCompleto] = carrinho.get(produtoCompleto, 0) + quantidade
                print(f"{quantidade} x {produtoCompleto} adicionado(s).")
            else:
                print("Quantidade inválida.")
        except ValueError:
            print("Digite um número válido.")
    else:
        print("Produto não encontrado.")

 # Sistema de remover as compras do carinho, se você tentar acessar o carrinho sem ter comprado nada, vai dá o Carrinho Vazio, fora isso, continua.
def removerCarrinho():
    if not carrinho:
        print("Carrinho vazio!")
        return
    print("\nProdutos no carrinho:")
    for produto, quantidade in carrinho.items():
        print(f"{produto}: {quantidade}")
    produtoSaida = input("Digite o produto que deseja remover: ")
    if produtoSaida in produtosCurto:
        produtoCompleto = produtosCurto[produtoSaida]
        if produtoCompleto in carrinho:
            del carrinho[produtoCompleto]
            print(f"{produtoCompleto} removido do carrinho.")
            
            # Leve tratamento de erro
        else:
            print("Produto não está no carrinho.")
    else:
        print("Produto não encontrado.")
        
 # Sistema para checar seu carrinho
def verCarrinho():
    if not carrinho:
        print("Carrinho vazio!")
    total = 0
    print("\nCarrinho:")
    for produto, qtd in carrinho.items():
        subtotal = produtos[produto] * qtd
        total += subtotal
        print(f"{produto}: {qtd} x R${produtos[produto]:.2f} = R${subtotal:.2f}")
    print(f"Total: R${total:.2f}")

# Após usarmos o def para definir todas as maracutaias antes do codigo, agora é só puxar as informações, eu pensei em fazer o menu de outra maneira mas assim ficou melhor.
def main():
    while True:
        print("\n1. Ver produtos\n2. Adicionar ao carrinho\n3. Remover do carrinho\n4. Ver carrinho\n5. Finalizar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            mostrarProdutos()
        elif opcao == "2":
            adicionarCarrinho()
        elif opcao == "3":
            removerCarrinho()
        elif opcao == "4":
            verCarrinho()
        elif opcao == "5":
            print("Compra finalizada. Obrigado!")
            break
        else:
            print("Opção inválida.")

# Bom, basicamente inicia a função def main, uffa! Foi tudo.
if __name__ == "__main__":
    main()
