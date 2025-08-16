from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.en_codigo.delete(0, END)
        self.en_nome.delete(0, END)
        self.en_telefone.delete(0, END)
        self.en_cep.delete(0, END)
        self.en_endereco.delete(0, END)
        self.en_numero.delete(0, END)
        self.en_bairro.delete(0, END)
        self.en_cidade.delete(0, END)        

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.geometry("700x500")
        self.root.configure(background="#046D8B")
        self.root.resizable(width=True, height=True)
        self.root.minsize(width=580, height=450)
        self.root.maxsize(width=1200, height=900)
    
    def frame_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#e6e6e6", highlightbackground="#1D6E6E", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg="#e6e6e6", highlightbackground="#1D6E6E", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def criar_botao(self, parent, texto, relx, rely, comando=None):
        return Button(
        parent,
        text=texto,
        font=("verdana", 10, "bold"),
        fg="#FFFFFF",
        bg="#1D6E6E",
        command=comando
    ).place(relx=relx, rely=rely, relwidth=0.14, relheight=0.14)

    def widgets_frame1(self):
        self.criar_botao(self.frame_1, "Limpar", 0.19, 0.10, comando=self.limpa_tela)
        self.criar_botao(self.frame_1, "Buscar", 0.35, 0.10)
        self.criar_botao(self.frame_1, "Novo", 0.51, 0.10)
        self.criar_botao(self.frame_1, "Alterar", 0.67, 0.10)
        self.criar_botao(self.frame_1, "Apagar", 0.83, 0.10)


        ## Criando Labels e Entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_codigo.place(relx=0.02, rely=0.02)
        self.en_codigo = Entry(self.frame_1, font=("bold", 10))
        self.en_codigo.place(relx=0.02, rely=0.12, relwidth=0.10, relheight=0.11)

        ## Criando Labels e Entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_nome.place(relx=0.02, rely=0.35)
        self.en_nome = Entry(self.frame_1, font=("bold", 10))
        self.en_nome.place(relx=0.02, rely=0.45, relwidth=0.56, relheight=0.11)

        ## Criando Labels e Entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_telefone.place(relx=0.60, rely=0.35)
        self.en_telefone = Entry(self.frame_1, font=("bold", 10))
        self.en_telefone.place(relx=0.60, rely=0.45, relwidth=0.2, relheight=0.11)

        ## Criando Labels e Entrada do CEP
        self.lb_cep = Label(self.frame_1, text="CEP", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_cep.place(relx=0.82, rely=0.35)
        self.en_cep = Entry(self.frame_1, font=("bold", 10))
        self.en_cep.place(relx=0.82, rely=0.45, relwidth=0.12, relheight=0.11)

        ## Criando Labels e Entrada do endereço
        self.lb_endereco = Label(self.frame_1, text="Endereço", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_endereco.place(relx=0.02, rely=0.6)
        self.en_endereco = Entry(self.frame_1, font=("bold", 10))
        self.en_endereco.place(relx=0.02, rely=0.7, relwidth=0.32, relheight=0.11)

        ## Criando Labels e Entrada do número
        self.lb_numero = Label(self.frame_1, text="Número", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_numero.place(relx=0.36, rely=0.6)
        self.en_numero = Entry(self.frame_1, font=("bold", 10))
        self.en_numero.place(relx=0.36, rely=0.7, relwidth=0.08, relheight=0.11)

        ## Criando Labels e Entrada da Bairro   
        self.lb_bairro = Label(self.frame_1, text="Bairro", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_bairro.place(relx=0.46, rely=0.6)
        self.en_bairro = Entry(self.frame_1, font=("bold", 10))
        self.en_bairro.place(relx=0.46, rely=0.7, relwidth=0.22, relheight=0.11)

        ## Criando Labels e Entrada da cidade   
        self.lb_cidade = Label(self.frame_1, text="Cidade", font=("Arial", 11, "bold"),fg="#1D6E6E", bg="#e6e6e6")
        self.lb_cidade.place(relx=0.70, rely=0.6)
        self.en_cidade = Entry(self.frame_1, font=("bold", 10))
        self.en_cidade.place(relx=0.70, rely=0.7, relwidth=0.24, relheight=0.11)

    def lista_frame2(self):
        self.listaClientes = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaClientes.heading("#0", text="")
        self.listaClientes.heading("col1", text="Código")
        self.listaClientes.heading("col2", text="Nome")
        self.listaClientes.heading("col3", text="Telefone")
        self.listaClientes.heading("col4", text="Cidade")

        self.listaClientes.column("#0", width=1, anchor="center")
        self.listaClientes.column("col1", width=50, anchor="center")
        self.listaClientes.column("col2", width=200, anchor="center")
        self.listaClientes.column("col3", width=100, anchor="center")
        self.listaClientes.column("col4", width=150, anchor="center")

        self.listaClientes.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.90)   
        
        self.scrooLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaClientes.configure(yscrollcommand=self.scrooLista.set)
        self.scrooLista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.90)

Application()