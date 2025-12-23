import sqlite3
import csv

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT,
        valor REAL
    )
''')

with open('vendas.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        cursor.execute('''
            INSERT INTO vendas (produto, valor)
            VALUES (?, ?)
        ''', (linha['produto'], float(linha['valor']))
        )

conexao.commit()
conexao.close()

print('Banco de dados criado e dados inseridos com sucesso.')
