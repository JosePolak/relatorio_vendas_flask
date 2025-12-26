from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_vendas():
    conn = sqlite3.connect('database/vendas.db')
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

@app.route('/')
def home():
    vendas = get_vendas()

    total = sum(item['quantidade'] * item['valor'] for item in vendas)

    return render_template(
        'index.html',
        vendas = vendas,
        total = total
    )

if __name__ == '__main__':
    app.run()
