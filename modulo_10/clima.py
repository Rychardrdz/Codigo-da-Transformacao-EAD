import requests

API_KEY = "4d8f0b2c1a9e7f6b123456789"

def buscar_clima(cidade):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}"
        f"&appid={API_KEY}"
        f"&units=metric"
        f"&lang=pt_br"
    )

    try:

        resposta = requests.get(url, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        return {
            "cidade": cidade,
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],
            "umidade": dados["main"]["humidity"],
            "descricao": dados["weather"][0]["description"]
        }

    except requests.exceptions.HTTPError:
        print("Erro HTTP na requisição.")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão com a internet.")

    except requests.exceptions.Timeout:
        print("Tempo de resposta excedido.")

    except requests.exceptions.RequestException as erro:
        print(f"Erro: {erro}")

    return None