import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def exibir_moradores():
    cursor.execute("SELECT * FROM moradores")
    moradores = cursor.fetchall()

    if moradores:
        for morador in moradores:
            print("ID:", morador[0])
            print("Nome:", morador[1])
            print("Placa:", morador[2])
            print("Telefone:", morador[3])
            print("-----------------------")
    else:
        print("Não há moradores cadastrados.")

exibir_moradores()