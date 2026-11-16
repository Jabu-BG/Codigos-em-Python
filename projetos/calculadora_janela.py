import tkinter as tk

def somar():
    """Soma os dois números inseridos e exibe o resultado"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())  # Corrigido: antes estava pegando entry1 duas vezes
        resultado = num1 + num2
        resultado_label.config(text=str(resultado))
    except ValueError:
        resultado_label.config(text="Erro: entrada inválida")

def limpar():
    """Limpa os campos de entrada e o resultado."""
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado_label.config(text="0")

root = tk.Tk()
root.title("Calculadora Simples")

tk.Label(root, text="Número 1:").grid(row=0, column=0, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)


tk.Label(root, text="Número 2:").grid(row=1, column=0, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Resultado:").grid(row=2, column=0, sticky="e")
resultado_label = tk.Label(root, text="0", bg="white", relief="sunken")
resultado_label.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

tk.Button(root, text="Somar", command=somar).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Limpar", command=limpar).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
