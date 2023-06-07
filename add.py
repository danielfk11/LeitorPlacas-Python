import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def criar_tabela():
    # Criação da tabela "moradores" 
    cursor.execute("CREATE TABLE IF NOT EXISTS moradores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, placa TEXT, telefone TEXT)")

def adicionar_morador():
    nome = input("Digite o nome do morador: ")
    placa = input("Digite a placa do veículo: ")
    telefone = input("Digite o telefone do morador: ")

    cursor.execute("INSERT INTO moradores (nome, placa, telefone) VALUES (?, ?, ?)", (nome, placa, telefone))
    conn.commit()
    print("-----------------------")
    print("Morador adicionado ao banco de dados.")

    cursor.execute("SELECT * FROM moradores WHERE placa = ?", (placa,))
    moradores = cursor.fetchall()

    if moradores:
        for morador in moradores:
            print("ID:", morador[0])
            print("Nome:", morador[1])
            print("Placa:", morador[2])
            print("Telefone:", morador[3])
            print("-----------------------")
    else:
        print("Morador nao adicionado.")

criar_tabela()
adicionar_morador()

# Fechar conexão
conn.close()