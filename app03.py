import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    texto.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Entrada de Nome")
janela.geometry("500x600")
janela.configure(bg="gray")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Enviar", command=mostrar_nome)
botao.pack(pady=10)

texto = tk.Label(janela, text="")
texto.pack(pady=10)

janela.mainloop()
