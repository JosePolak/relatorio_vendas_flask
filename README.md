# Relatório de Vendas — Flask + SQLite

Projeto simples de backend desenvolvido em Python com Flask e SQLite, com foco em **organização de código, separação de responsabilidades e apresentação de dados**.

Além da interface web, a aplicação expõe uma rota de API (`/api/vendas`) que retorna dados consolidados em formato JSON, demonstrando integração backend com consumo via API.

O objetivo é demonstrar boas práticas iniciais em aplicações web, indo além de scripts isolados.

---

## 🧩 Funcionalidades

- Cadastro de vendas via formulário
- Armazenamento dos dados em banco SQLite
- Listagem das vendas em tabela
- Cálculo do total geral
- Interface web simples e responsiva (desktop e mobile)

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- HTML + CSS
- Jinja2 (templates)

---

## 📁 Organização do projeto

```
├── app.py              # Aplicação Flask (rotas e lógica web)
├── criar_banco.py      # Script para criação do banco de dados
├── db.py               # Camada de acesso ao banco de dados
├── database/
│   └── vendas.db
├── templates/
│   ├── base.html
│   ├── index.html
│   └── nova_venda.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

O projeto segue uma separação clara entre:
- camada web (`app.py`)
- camada de dados (`db.py`)
- camada de apresentação (`templates` e `static`)

---

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie o banco de dados (executar apenas uma vez):
```bash
python criar_banco.py
```

5. Execute a aplicação:
```bash
python app.py
```

6. Acesse no navegador:
```
http://127.0.0.1:5000
```

---

## 🎯 Objetivo do projeto

Este projeto faz parte de um processo de estudo e transição para a área de desenvolvimento backend, com foco em:

- Python
- desenvolvimento web com Flask
- organização de projetos
- boas práticas iniciais

Ele também serve como base para evoluções futuras com aplicações web mais completas.

---

## 📌 Próximos passos (planejados)

- Melhorias na validação de dados
- Expansão dos relatórios
- Evolução visual do layout
