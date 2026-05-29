from flask import Flask

app = Flask(__name__)


@app.route("/saudacao")
def saudacao():

    return "Olá, seja bem-vindo!"


if __name__ == "__main__":
    app.run(debug=True)