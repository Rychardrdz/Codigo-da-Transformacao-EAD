from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []


@app.route("/posts", methods=["POST"])
def criar_post():

    dados = request.get_json()

    posts.append(dados)

    return jsonify({
        "mensagem": "Post criado!"
    })


@app.route("/posts", methods=["GET"])
def listar_posts():

    return jsonify(posts)


@app.route("/comentario", methods=["POST"])
def comentario():

    dados = request.get_json()

    return jsonify({
        "mensagem": "Comentário adicionado!",
        "comentario": dados
    })


@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    return jsonify({
        "mensagem": "Login realizado!",
        "usuario": dados["usuario"]
    })


if __name__ == "__main__":
    app.run(debug=True)