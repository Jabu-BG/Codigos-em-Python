import logging
def dividir():
    try:
        dividendo=float(input("Digite o dividendo: "))
        divisor=float(input("Digite o divisor: "))
        if divisor == 0:
            raise ZeroDivisionError("Divisão por zero não permitida")
        resultado = dividendo / divisor
        print(f"Resultado: {resultado:.2f}")
    except ValueError as e:
        logging.error(f"Entrada Inválida: {e}")
        print("Por favor, digite apenas números.")
    except ZeroDivisionError as e:
        logging.error(f"Erro Matemático: {e}")
        print("Não é possível dividir por zero.")

    except Exception as e:
        logging.error(f"Error Inesperado: {e}")

dividir()
