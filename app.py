from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    vendas = [
        {'produto': 'Teclado', 'quantidade': 2, 'valor': 150.0},
        {'produto': 'Mouse', 'quantidade': 3, 'valor': 80.0},
        {'produto': 'Monitor', 'quantidade': 1, 'valor': 1200.0}
    ]

    total = sum(item['quantidade'] * item['valor'] for item in vendas)

    return render_template(
        'index.html',
        vendas = vendas,
        total = total
    )

if __name__ == '__main__':
    app.run()
