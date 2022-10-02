# Projeto 10
# CRUD com Python e MySQL

import mysql.connector

conexao = mysql.connector.connect(  # Criando a conexão com o banco de dados
    host='localhost',  # Pois o BD tá armazenado no computador, é local. Se fosse armazenado em um link ou IP específico, bastaria colocar o link ou o IP aqui
    user='root',
    password='Brito',
    database='bdyoutube',
)

# O cara que vai executar a conexão, executar os comandos da execução
cursor = conexao.cursor()


# CREATE
def create():
    nome_produto = input("Nome do produto: ")
    valor = int(input("Valor do produto: "))
    # Cria-se uma variável comando pra executar funções
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()  # Quando edita o banco de dados precisa commitar


# READ
def read():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # Quando se lê o BD
    print(resultado)


# UPDATE
def update():
    nome_produto = input("Nome do produto: ")
    valor = int(input("Valor do produto: "))
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()  # Quando edita o banco de dados precisa commitar


# DELETE
def delete():
    nome_produto = input("Nome do produto: ")
    comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()  # Quando edita o banco de dados precisa commitar


create()
# read()
# update()
# delete()


# Para encerrar o programa. Sempre rodar.
cursor.close()
conexao.close()
