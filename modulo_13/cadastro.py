from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]

    return jsonify({
        "mensagem": "Usuário cadastrado!",
        "nome": nome,
        "email": email
    })


if __name__ == "__main__":
    app.run(debug=True)