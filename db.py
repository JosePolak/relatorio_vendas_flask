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
            'quantidade': int(quantidade),
            'valor': float(valor)
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


# Retorna total de registros e valor total para API JSON
def get_vendas_resumo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*), SUM(quantidade * valor) FROM vendas')
    resultado = cursor.fetchone()
    conn.close()
    
    return {
        "total_registros": resultado[0],
        "valor_total": resultado[1]
    }
