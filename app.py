from flask import Flask, render_template, request, redirect, url_for
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


@app.route('/nova_venda')
def nova_venda():
    return render_template('nova_venda.html')


@app.route('/processar_venda', methods = ['POST'])
def processar_venda():
    produto = request.form['produto']
    quantidade = request.form['quantidade']
    valor = request.form['valor']
    
    conn = sqlite3.connect('database/vendas.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO vendas (produto, quantidade, valor)
        VALUES (?, ?, ?)
        ''',
        (produto, quantidade, valor)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
