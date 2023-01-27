import sqlite3 as lite
import datetime
#criando conexao


#CRIAR = Inserir
#LER = Acessar
#ATUALIZAR = Update
#REMOVER = delete

con = lite.connect('dados.db')



#inserir dados
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, cpf, telefone, email, dia, plano) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

def devedores():
    lista = []
    with con:
        cur = con.cursor()
        query = """
        SELECT id, nome, cpf, telefone, email, dia, plano
        FROM formulario
        WHERE 
            dia <= date()
            AND
            (ultima_mensagem IS NULL
            OR ultima_mensagem < dia)

        """
        
        cur.execute(query)
        resultados = cur.fetchall()
        format = f = '%Y-%m-%d'
        
        for entrada in resultados:
            valor_retorno = lambda:None
            valor_retorno.id = entrada[0]
            valor_retorno.nome = entrada[1]
            valor_retorno.cpf = entrada[2]
            valor_retorno.telefone = entrada[3]
            valor_retorno.email = entrada[4]
            new_date = datetime.datetime.strptime(entrada[5], format)
            valor_retorno.dia = new_date
            valor_retorno.plano = entrada[6]
            lista.append(valor_retorno)
            
    return lista

#Acessar informações
def mostrar_info():
    lista = []
    
    with con:
        cur = con.cursor()
        query = "SELECT id, nome, cpf, telefone, email, dia, plano FROM formulario"
        cur.execute(query)
        valores = cur.fetchall()
        
        format = f = '%Y-%m-%d'
        for entrada in valores:
            print(entrada)
            valor_retorno = lambda:None
            valor_retorno.id = entrada[0]
            valor_retorno.nome = entrada[1]
            valor_retorno.cpf = entrada[2]
            valor_retorno.telefone = entrada[3]
            valor_retorno.email = entrada[4]
            new_date = datetime.datetime.strptime(entrada[5], format)
            valor_retorno.dia = new_date
            valor_retorno.plano = entrada[6]
            lista.append(valor_retorno)

    return lista

def mostrar_por_id_info(id):
    valor_retorno = lambda:None
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario WHERE id=?"
        cur.execute(query,(id,))
        resultados = cur.fetchall()
        format = f = '%Y-%m-%d'
        for entrada in resultados:
            valor_retorno.id = entrada[0]
            valor_retorno.nome = entrada[1]
            valor_retorno.cpf = entrada[2]
            valor_retorno.telefone = entrada[3]
            valor_retorno.email = entrada[4]
            new_date = datetime.datetime.strptime(entrada[5], format)
            valor_retorno.dia = new_date
            valor_retorno.plano = entrada[6]
            return valor_retorno


#mensagem enviada para devedor

def mensagem_enviada_para_devedor(id):
    
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET ultima_mensagem=date() WHERE id=?"
        cur.execute(query,(id,))
        con.commit()

#Atualizar Informações




def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, cpf=?, telefone=?, email=?, dia=?, plano=? WHERE id=?"
        cur.execute(query,i)
        con.commit()

#pagar

def pagar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET dia=? WHERE id=?"
        cur.execute(query,i)
        con.commit()


#Deletar Informações

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)

#Selecionar clientes para o aviso
def selecionar_clientes():
    clientes = []
    with con:
        cur = con.cursor()
        query = ("SELECT nome, telefone FROM formulario")
        cur.execute(query)
        resultado = cur.fetchall()
        for cliente in resultado:
            clientes.append(cliente)
    return clientes
