from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

# Configuração da janela principal

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf", pagesize=A4)

        self.codigoRel = self.en_codigo.get()
        self.nomeRel = self.en_nome.get()
        self.telefoneRel = self.en_telefone.get()
        self.cepRel = self.en_cep.get()
        self.enderecoRel = self.en_endereco.get()
        self.numeroRel = self.en_numero.get()
        self.bairroRel = self.en_bairro.get()
        self.cidadeRel = self.en_cidade.get()
        self.c.setFont("Helvetica", 24)
        self.c.drawString(200, 800, "Ficha do Cliente")

        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(50, 750, f"Código: ")
        self.c.drawString(50, 730, f"Nome: ")
        self.c.drawString(50, 710, f"Telefone: ")
        self.c.drawString(50, 690, f"CEP: ")
        self.c.drawString(50, 670, f"Endereço: ")
        self.c.drawString(50, 650, f"Número: ")
        self.c.drawString(50, 630, f"Bairro: ")
        self.c.drawString(50, 610, f"Cidade: ")

        self.c.setFont("Helvetica", 14)
        self.c.drawString(130, 750, self.codigoRel)
        self.c.drawString(130, 730, self.nomeRel)
        self.c.drawString(130, 710, self.telefoneRel)
        self.c.drawString(130, 690, self.cepRel)
        self.c.drawString(130, 670, self.enderecoRel)
        self.c.drawString(130, 650, self.numeroRel)
        self.c.drawString(130, 630, self.bairroRel)
        self.c.drawString(130, 610, self.cidadeRel)

        self.c.rect(20, 550, 550, 3, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCliente()


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
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectado ao banco de dados")
    def desconecta_db(self):
        self.conn.close(); print("Desconectado ao banco de dados")  
    def montaTabelas(self):
        self.conecta_db(); 

        ### Criando a tabela clientes
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                codigo INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                telefone TEXT NOT NULL,
                cep TEXT,
                endereco CHAR(80),
                numero TEXT,
                bairro CHAR(40),
                cidade CHAR(40)
            )
        """)
        self.conn.commit()
        print("Banco de dados criado com sucesso")
        self.desconecta_db()
    def variaveis(self):
        self.codigo = self.en_codigo.get()
        self.nome = self.en_nome.get()
        self.telefone = self.en_telefone.get()
        self.cep = self.en_cep.get()
        self.endereco = self.en_endereco.get()
        self.numero = self.en_numero.get()
        self.bairro = self.en_bairro.get()
        self.cidade = self.en_cidade.get()
    def add_cliente(self):      # Método para adicionar cliente
        self.variaveis()
        self.conecta_db()
    
        self.cursor.execute("""
            INSERT INTO clientes (nome, telefone, cep, endereco, numero, bairro, cidade)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (self.nome, self.telefone, self.cep, self.endereco, self.numero, self.bairro, self.cidade))
        self.conn.commit()      # Confirma a inserção no banco de dados
        print("Cliente adicionado com sucesso")
        self.desconecta_db()
        self.select_lista()      # Atualiza a lista após adicionar o cliente
        self.limpa_tela()        # Limpa os campos após adicionar o cliente
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaClientes.selection()
        for i in self.listaClientes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaClientes.item(i, "values")
            self.en_codigo.insert(0, col1)
            self.en_nome.insert(0, col2)
            self.en_telefone.insert(0, col3)
            self.en_cep.insert(0, col4)
            self.en_endereco.insert(0, col5)
            self.en_numero.insert(0, col6)
            self.en_bairro.insert(0, col7)
            self.en_cidade.insert(0, col8)
    def deleta_cliente(self):
        self.variaveis()
        if self.codigo.strip() == "":
            print("Informe o código para deletar.")
            return
        self.conecta_db()
        self.cursor.execute(""" DELETE FROM clientes WHERE codigo = ? """, (self.codigo,))
        self.conn.commit()
        self.desconecta_db()
        self.limpa_tela()
        self.select_lista()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""
            UPDATE clientes SET nome = ?, telefone = ?, cep = ?, endereco = ?, numero = ?, bairro = ?, cidade = ?
            WHERE codigo = ?
        """, (self.nome, self.telefone, self.cep, self.endereco, self.numero, self.bairro, self.cidade, self.codigo))
        self.conn.commit()
        print("Cliente alterado com sucesso")
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)
        menubar.add_cascade(label="Sair", command=Quit)

        filemenu.add_command(label="Limpar", command=self.limpa_tela)
        filemenu2.add_command(label="Gerar PDF", command=self.geraRelatCliente)
        filemenu.add_command(label="Buscar", command=self.select_lista)
        filemenu.add_command(label="Novo", command=self.add_cliente)
        filemenu.add_command(label="Alterar", command=self.altera_cliente)
        filemenu.add_command(label="Apagar", command=self.deleta_cliente)
        filemenu2.add_command(label="Sobre", command=lambda: print("Desenvolvido por Ari Júnior"))


    def select_lista(self):
        self.conecta_db()
        self.listaClientes.delete(*self.listaClientes.get_children())
        lista = self.cursor.execute("""SELECT codigo, nome, telefone, cep, endereco, numero, bairro, cidade FROM clientes ORDER BY codigo""")
        for i in lista:     # Percorre a lista de clientes
            self.listaClientes.insert("", "end", values=i)
             # Insere cada cliente na lista

        self.desconecta_db()    # Desconecta do banco de dados após a consulta
        

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()     # Carrega a lista de clientes ao iniciar
        self.Menus()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.geometry("900x700")
        self.root.configure(background="#046D8B")
        self.root.resizable(width=True, height=True)
        self.root.minsize(width=780, height=650)
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
        self.criar_botao(self.frame_1, "Novo", 0.51, 0.10, comando=self.add_cliente)
        self.criar_botao(self.frame_1, "Alterar", 0.67, 0.10, comando=self.altera_cliente)
        self.criar_botao(self.frame_1, "Apagar", 0.83, 0.10, comando=self.deleta_cliente)


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
        self.listaClientes = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"), show= "headings")
        
       
        self.listaClientes.heading("col1", text="Cód")
        self.listaClientes.heading("col2", text="Nome")
        self.listaClientes.heading("col3", text="Telefone")
        self.listaClientes.heading("col4", text="CEP")
        self.listaClientes.heading("col5", text="Endereço")
        self.listaClientes.heading("col6", text="Número")
        self.listaClientes.heading("col7", text="Bairro")
        self.listaClientes.heading("col8", text="Cidade")

    
        self.listaClientes.column("col1", width=8, anchor="center")
        self.listaClientes.column("col2", width=150, anchor="w")
        self.listaClientes.column("col3", width=40, anchor="center")
        self.listaClientes.column("col4", width=35, anchor="center")
        self.listaClientes.column("col5", width=100, anchor="center")
        self.listaClientes.column("col6", width=20, anchor="center")
        self.listaClientes.column("col7", width=80, anchor="center")
        self.listaClientes.column("col8", width=70, anchor="center")


        self.listaClientes.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.90)   
        
        self.scrooLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaClientes.configure(yscrollcommand=self.scrooLista.set)
        self.scrooLista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.90)

        self.listaClientes.bind("<Double-1>", self.OnDoubleClick)

Application()