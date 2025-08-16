import tkinter as tk

def dizer_ola():
    texto.config(text="Olá, mundo!")

janela = tk.Tk()
janela.title("Exemplo com Botão")
janela.geometry("500x600")
janela.configure(bg="green")

# Label (texto)
texto = tk.Label(janela, text="Clique no botão abaixo", font=("Arial", 12, "bold"), fg="white",  bg="gray")
texto.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Clique aqui", font=("Arial", 12, "bold"), command=dizer_ola)
botao.pack(pady=10)

janela.mainloop()
