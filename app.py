from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Relatório de Vendas</h1><p>Página inicial</p>'


@app.route('/sobre')
def sobre():
    return '<h1>Sobre</h1><p>Projeto de estudo com Flask</p>'


@app.route('/contato')
def contato():
    return '<h1>Contato</h1><p>Contato fictício</p>'


if __name__ == '__main__':
    app.run(debug=True)
