#tkinter
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import messagebox

from tkinter import ttk
import tkinter as tk
from tkinter import Text
#datetime
import datetime

#importando tkcalender

from tkcalendar import Calendar, DateEntry

#import whatkit

import pywhatkit as kt
import pyautogui as pg
import time
import keyboard
import pyautogui

#importando main

from main import *



#variaveis

ano = datetime.date.today().year
mes = datetime.date.today().month
dia = datetime.date.today().day

planos = ["Todos os dias", "3 dias"]

# cores

cor_azul = '#a9f8f9'  # azul mais escurinho
cnovo  = '#dcdcdc' #branco mais escurinho
co0 = "#f0f3f5"  # Preta
c1 = "#feffff"  # branca
c2 = "#4fa882"  # verde
c3 = "#38576b"  # valor
c4 = "#403d3d"   # letra
c5 = "#e06636"   # - profit
c6 = "#ef5350"   # vermelha
c7 = "#263238"   # + verde
c8 = "#e9edf5"   # branco
v1 = "#278e79"
jabuticaba= "#1d153f"
azul_novo = "#038cfc"
roxo = "#b671d0"




#mascaras

#CPF
def apply_mask(event):
    cpf = event.widget.get()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf = cpf.replace(" ", "")
    new_cpf = ""
    for char in cpf:
        if char.isdigit():
            new_cpf += char
    cpf = new_cpf
    parte1 = cpf[:3]
    parte2 = cpf[3:6]
    parte3 = cpf[6:9]
    parte4 = cpf[9:11]
    cpf = ''
    if parte1 != '':
        cpf += parte1
    if parte2 != '':
        cpf += '.'+ parte2
    if parte3 != '':
        cpf += '.' + parte3
    if parte4 != '':
        cpf += '-' + parte4
    event.widget.delete(0, tk.END)
    event.widget.insert(0, cpf)
    
#TELEFONE



def update_mask(event):
    new_current = ''
    for char in event.widget.get():
        if char.isdigit() or char=='+':
            new_current += char
    if len(new_current) < 4:
        new_current = '+55'
    if len(new_current) > 14:
        new_current = new_current[:14]
    event.widget.delete(0, tk.END)
    event.widget.insert(0, new_current)

#funçao para devedor
def busca_devedores():
    deves = devedores()
    for devedor in deves:
        try:
            kt.sendwhatmsg_instantly(devedor.telefone,f'''Prezado(a) {devedor.nome},

Gostaríamos de lembrá-lo(a) de que sua mensalidade está atrasada. Por favor, entre em contato conosco o quanto antes para regularizar sua situação financeira. Caso já tenha efetuado o pagamento, por favor desconsidere esta mensagem.
Atenciosamente,
Thanos Academia''')
            mensagem_enviada_para_devedor(devedor.id)
        except:
            print("Erro ao enviar msg")

#create window (janela)


janela = Tk()
janela.title('ThanoSystem')
janela.geometry('1043x453')
janela.configure(background=c8)
janela.resizable(width=False, height=False)
busca_devedores()
icone = PhotoImage (file='C:\\Users\\cypri\\Desktop\\ThanoSystem\\icons8-thanos-48.png'  )
icone1 = PhotoImage (file='C:\\Users\\cypri\\Desktop\\ThanoSystem\\thanoscalvo.png' )
janela.iconphoto(False,icone)
#separando em partes





        



frame_cima = Frame(janela, width=310, height= 50, bg ="#8fbfff", relief='flat')
frame_cima.grid(row = 0, column= 0)



frame_baixo = Frame(janela, width=310, height= 403, bg=cnovo, relief='flat')
frame_baixo.grid(row = 1, column= 0, sticky=NSEW, padx=0,pady=1)

frame_direita = Frame(janela, width=588, height= 403,bg=cnovo, relief='flat')
frame_direita.grid(row = 0, column= 1, rowspan=2, padx=1, pady= 0, sticky=NSEW)

#adicionando textos em labels xD

app_nome = Label(frame_cima,text = 'Cadastro dos Clientes', anchor = NW, font =('Ivy 11 bold'), bg= "#8fbfff", fg= "black", relief='ridge',)
app_nome.place(x = 65 , y = 14)

#variavel tree modo global
global tree

#Função Inserir

def inserir():

    nome = e_nome.get() 
    cpf = e_CPF.get()
    telefone = e_tel.get() 
    email = e_email.get() 
    data = e_data_pagamento.get_date() 
    plano = e_plano.get() 

    lista = [nome, cpf, telefone, email, data, plano]
    if nome == '':
        messagebox.showerror('Erro','O nome não pode ser vazio.')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Os dados foram inseridos corretamente!')

    e_nome.delete(0,'end')
    e_CPF.delete(0,'end')
    e_tel.delete(0,'end') 
    e_email.delete(0,'end') 
    e_data_pagamento.delete(0,'end')  
    e_plano.delete(0,'end') 

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()

 #Pagar
def pagar():
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    tree_lista = treev_dicionario['values']
    valor_id = tree_lista[0]
    selecionado = mostrar_por_id_info(valor_id)
    data = selecionado.dia

    next_month = data.month % 12 + 1
    year = data.year + 1 if next_month == 1 else data.year
    data = datetime.date(year,next_month,data.day)



    lista = [data,valor_id]
    pagar_info(lista)
    messagebox.showinfo('Sucesso','Pagamento Realizado com Sucesso!')

    e_nome.delete(0,'end')
    e_CPF.delete(0,'end')
    e_tel.delete(0,'end')
    e_email.delete(0,'end') 
    e_data_pagamento.delete(0,'end')  
    e_plano.delete(0,'end') 

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()

#Função Atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]
        valor_atualizacao = mostrar_por_id_info(valor_id)
        e_nome.delete(0,'end')
        e_CPF.delete(0,'end')
        e_tel.delete(0,'end') 
        e_email.delete(0,'end') 
        e_data_pagamento.delete(0,'end')  
        e_plano.delete(0,'end') 

        e_nome.insert(0,valor_atualizacao.nome)
        e_CPF.insert(0,valor_atualizacao.cpf)
        e_tel.insert(0,valor_atualizacao.telefone) 
        e_email.insert(0,valor_atualizacao.email) 


    
        


        e_data_pagamento.set_date(valor_atualizacao.dia)  
        e_plano.insert(0,valor_atualizacao.plano) 

        #Função atualizar

        def update():

            nome = e_nome.get() 
            cpf = e_CPF.get()
            telefone = e_tel.get() 
            email = e_email.get() 
            data = e_data_pagamento.get_date() 
            plano = e_plano.get() 

            lista = [nome, cpf, telefone, email, data, plano, valor_id]
            if nome == '':
                messagebox.showerror('Erro','O nome não pode ser vazio.')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Os dados foram atualizados com sucesso!')

                e_nome.delete(0,'end')
                e_CPF.delete(0,'end')
                e_tel.delete(0,'end') 
                e_email.delete(0,'end') 
                e_data_pagamento.delete(0,'end')  
                e_plano.delete(0,'end') 

            for widget in frame_direita.winfo_children():
                widget.destroy()

        

            mostrar()



        #Botão Confirmar

        button_confirmar = Button(frame_baixo,command = update, text = 'Confirmar', width=10, font =('Ivy 8 bold'), bg= "#b8d3ff", fg= "black", relief='raise', overrelief='ridge')
        button_confirmar.place(x = 210 , y = 140)
        

        

    except IndexError:
        messagebox.showerror('Erro','Selecione um dos dados na tabela para atualizar.')

#Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]
        deletar_info(valor_id)
        messagebox.showinfo('Sucesso','Os dados foram removidos com sucesso.')
        for widget in frame_direita.winfo_children():
                widget.destroy()

        mostrar()

        

    except IndexError:
        messagebox.showerror('Erro','Selecione um dos dados na tabela para Remover.')



     




#Configurar frame debaixo

#Nome
label_nome = Label(frame_baixo,text = 'Nome *', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_nome.place(x = 5 , y = 30)

e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x = 9 , y = 50)

#CPF

label_CPF = Label(frame_baixo,text = 'CPF *', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_CPF.place(x = 5 , y = 80)

e_CPF = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_CPF.bind("<KeyRelease>", apply_mask)
e_CPF.place(x = 9 , y = 109)

#Telefone

label_tel = Label(frame_baixo,text = 'Telefone *', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_tel.place(x = 5 , y = 135)

e_tel = tk.Entry(frame_baixo, width=25, justify='left', relief='solid')
e_tel.insert(0, "+55")
e_tel.place(x = 9 , y = 164)
e_tel.bind("<KeyRelease>", update_mask)

#Email

label_email = Label(frame_baixo,text = 'Email *', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_email.place(x = 5 , y = 190)

e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x = 9 , y = 217)

#DataAtual

label_data_atual = Label(frame_baixo,text = 'Data de Hoje', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_data_atual.place(x = 5 , y = 290)

e_data_atual = Label(frame_baixo, text=f'{dia}/{mes}/{ano}', width=10, justify='left', relief='solid')
e_data_atual.place(x = 9 , y = 315)

#ComboBox com opções de Plano
label_plano = Label(frame_baixo,text = 'Plano:', anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_plano.place(x = 5 , y = 250)
e_plano = ttk.Combobox(frame_baixo, value = planos, width=12, state='enabled')
opcao_combobox = e_plano.current(0)
e_plano.place(x = 55 , y = 250)

#DataPagamento

label_data_pagamento = Label(frame_baixo,text = 'Data de pagamento',anchor = NW, font =('Ivy 10 bold'), bg= cnovo, fg= c4, relief='flat')
label_data_pagamento.place(x = 100 , y = 290)

e_data_pagamento = DateEntry(frame_baixo, justify=CENTER,selectmode='day',date_pattern='dd-MM-yyyy', background = 'darkblue', foreground = 'white', borderwidth=2, width=12)
e_data_pagamento.place(x = 100 , y = 315)


#Botão Inserir

button_adicionar = Button(frame_baixo, command = inserir, text = 'Adicionar', width=10, font =('Ivy 8 bold'), bg= "#b8d3ff", fg= "black", relief='raise', overrelief='ridge')
button_adicionar.place(x = 9 , y = 360)

#Botão Atualizar


button_atualizar = Button(frame_baixo,command = atualizar, text = 'Salvar', width=10, font =('Ivy 8 bold'), bg= "gray", fg= c1, relief='raise', overrelief='ridge')
button_atualizar.place(x = 210 , y = 109)


#Botao pagar
button_pagar = Button(frame_baixo,command = pagar, text = 'Pagar', width=10, font =('Ivy 8 bold'), bg= "#b8d3ff", fg= "black", relief='raise', overrelief='ridge')
button_pagar.place(x = 100 , y = 360)

#Botão Atualizar

button_remover = Button(frame_baixo,command = deletar, text = 'Remover', width=10, font =('Ivy 8 bold'), bg= "#b8d3ff", fg= "black", relief='raise', overrelief='ridge')
button_remover.place(x = 193 , y = 360)

#Avisos da academia
#-------------------


def enviar_mensagem(mensagem):
    mensagem = mensagem.strip()
    if not mensagem:
        return
    clientes = selecionar_clientes()
    for nome, telefone in clientes:
        try:
            kt.sendwhatmsg_instantly (telefone, mensagem)
        except:
            print("Erro ao enviar mensagem para", nome)
    janela_aviso.withdraw()

# Função para abrir a janela "mini"
def abrir_janela_aviso():
    global janela_aviso
    janela_aviso = Toplevel()
    janela_aviso.protocol("WM_DELETE_WINDOW", janela_aviso.withdraw())
    janela_aviso.title("Aviso")
    janela_aviso.geometry("300x150")
    janela_aviso.configure(background=c8)
    janela_aviso.resizable(width=False, height=False)
    
    label_aviso = Label(janela_aviso, text="Enviar aviso para todos os clientes!", font=("Ivy 10 bold"), bg=c8)
    label_aviso.place(x=30, y=20)
    mensagem_entry = Text(janela_aviso, width=30, height=3, wrap="word")
    mensagem_entry.place(x=30, y=50)
    botao_enviar = Button(janela_aviso, text="Enviar", command=lambda: enviar_mensagem(mensagem_entry.get("1.0", END).strip()))
    botao_enviar.place(x=120, y=110)
    janela_aviso.deiconify()

# Adicionando o botão "Aviso"
botao_aviso = Button(frame_baixo, text="Aviso", command=abrir_janela_aviso)
botao_aviso.place(x=250, y=170)




#-------------------


#TABELA
def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabeçario
    tabela_head = ['ID','Nome', 'Cpf','Telefone', 'Email', 'Data', 'Plano']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,150,110,100,155,70,100,30]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Ajustar coluna com tamanho da palavra do cabeçario ( string )
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    format = f = '%Y-%m-%d'
    for item in lista:
        tag = 'paga'
        
        if datetime.datetime.today() > item.dia:
            tag = 'vencidas'
        new_item = (
            item.id,
            item.nome,
            item.cpf,
            item.telefone,
            item.email,
            item.dia.strftime('%d-%m-%Y'),
            item.plano
        )
        tree.insert('', 'end', values=new_item, tags=(tag,))
    tree.tag_configure('vencidas',background='#e37372')
#chamando a função mostrar

mostrar()







janela.mainloop()



