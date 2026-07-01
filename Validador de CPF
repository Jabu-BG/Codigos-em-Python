def validar_CPF(cpf: str) -> tuple[bool, str]:
    # Permite que o CPF seja digitado com pontos e hífen
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False, "CPF deve possuir 11 números."

    # Verifica se todos os números são iguais
    if cpf == cpf[0] * 11:
        return False, "Números repetidos!"

    # Calcula os dois dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0

        if digito != int(cpf[i]):
            return False, "Dígitos verificadores errados!"

    return True, "CPF válido!"


cpf_input = input("Digite seu CPF: ")
valido, mensagem = validar_CPF(cpf_input)
print(mensagem)
