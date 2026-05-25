import requests

API_KEY = "tmdb123456789abc"

def buscar_filme(nome_filme):

    url = (
        f"https://api.themoviedb.org/3/search/movie"
        f"?api_key={API_KEY}"
        f"&query={nome_filme}"
        f"&language=pt-BR"
    )

    try:

        resposta = requests.get(url, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        if dados["results"]:

            filme = dados["results"][0]

            return {
                "titulo": filme["title"],
                "lancamento": filme["release_date"],
                "sinopse": filme["overview"]
            }

        else:
            print("Filme não encontrado.")
            return None

    except requests.exceptions.RequestException as erro:
        print(f"Erro: {erro}")

        return None