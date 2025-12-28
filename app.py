from flask import Flask, render_template, request, redirect, url_for
from db import get_vendas, inserir_venda


app = Flask(__name__)


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


@app.route('/processar_venda', methods=['POST'])
def processar_venda():
    produto = request.form['produto']
    quantidade = int(request.form['quantidade'])
    valor = float(request.form['valor'])

    inserir_venda(produto, quantidade, valor)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
