from flask import Flask, render_template
import csv
import sqlite3

app = Flask(__name__)


def get_vendas():
    conexao = sqlite3.connect('vendas.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT produto, valor FROM vendas')
    vendas = cursor.fetchall()

    conexao.close()

    return vendas


@app.route('/')
def home():
    vendas = get_vendas()
    total = sum(v[1] for v in vendas)

    return render_template(
        'index.html',
        vendas = vendas,
        total = total
    )

if __name__ == '__main__':
    app.run()
