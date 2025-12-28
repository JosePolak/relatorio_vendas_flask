import sqlite3

DB_PATH = 'database/vendas.db'


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_vendas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT produto, quantidade, valor
        FROM vendas
    ''')

    rows = cursor.fetchall()
    conn.close()

    vendas = []
    for produto, quantidade, valor in rows:
        vendas.append({
            'produto': produto,
            'quantidade': quantidade,
            'valor': valor
        })
    
    return vendas


def inserir_venda(produto, quantidade, valor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO vendas (produto, quantidade, valor)
        VALUES (?, ?, ?)
        ''',
        (produto, quantidade, valor)
    )

    conn.commit()
    conn.close()
