import sqlite3
from pathlib import Path

# Garante que a pasta database existe
Path('database').mkdir(exist_ok=True)

conn = sqlite3.connect('database/vendas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL
    )
''')

dados = [
    ('Teclado', 2, 150.0),
    ('Mouse', 3, 80.0), 
    ('Monitor', 1, 1200.0),
]

cursor.executemany('''
    INSERT INTO vendas (produto, quantidade, valor)
    VALUES (?, ?, ?)
    ''', dados)

conn.commit()
conn.close()

print('Banco criado e dados inseridos com sucesso.')
