from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


conexao = sqlite3.connect("usuarios.db", check_same_thread=False)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conexao.commit()


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]

    cursor.execute("""
    INSERT INTO usuarios (nome, email)
    VALUES (?, ?)
    """, (nome, email))

    conexao.commit()

    return jsonify({
        "mensagem": "Usuário salvo no banco!"
    })


@app.route("/usuarios")
def usuarios():

    cursor.execute("SELECT * FROM usuarios")

    lista = cursor.fetchall()

    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True)