from desafio_extra_api import app


def test_inicio():

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200