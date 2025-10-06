from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"mensagem": "Olá, mundo!"})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    resultado = dados['a'] + dados['b']
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)

"------------------------------------------------"

import sqlite3

# Criando/conectando ao banco
con = sqlite3.connect("exemplo.db")
cur = con.cursor()

# Criando uma tabela
cur.execute("""
    CREATE TABLE IF NOT EXISTS pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    );
""")

# Inserindo dados
cur.execute("INSERT INTO pessoa (nome, idade) VALUES (?, ?)", ("João", 30))
con.commit()

# Consultando dados
cur.execute("SELECT * FROM pessoa")
pessoas = cur.fetchall()
for pessoa in pessoas:
    print(pessoa)

# Fechando conexão
con.close()