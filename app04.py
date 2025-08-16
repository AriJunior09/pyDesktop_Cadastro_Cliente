import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    label_resultado.config(text=f"Você digitou: {texto}")




janela = tk.Tk()
janela.title("Lendo Entrada")
janela.geometry("300x200")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Ler texto", font=("Arial", 12), fg="gray", command=mostrar_texto)
botao.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()
