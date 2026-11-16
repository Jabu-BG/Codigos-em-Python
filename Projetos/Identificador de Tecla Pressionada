import tkinter as tk
def tecla_pressionada(event):
    print(f"Tecla pressionada: {event.keysym}")

    if event.keysym == 'Escape':
        root.quit()

def tecla_solta(event):
    print(f"Tecla Solta: {event.keysym}")

root = tk.Tk()
root.title("Captura de Eventos de Teclado")

label = tk.Label(root,text="Pressione qualquer tecla")
label.pack(pady=20)

root.bind('<KeyPress>', tecla_pressionada)
root.bind('<KeyRelease>',tecla_solta)

root.focus_set()

root.mainloop()
