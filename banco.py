import sqlite3 as lite

# iniciar conexao com o banco de dados
conexao = lite.connect('dados.db')

#with abre e fecha o banco de dados automaticamente
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, telefone TEXT,email TEXT, dia DATE, plano TEXT, ultima_mensagem DATE)")
