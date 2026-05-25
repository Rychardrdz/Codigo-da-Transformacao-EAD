from clima import buscar_clima
from filmes import buscar_filme


def mostrar_menu():

    print("\n========== MENU ==========")
    print("1 - Consultar clima")
    print("2 - Buscar filme")
    print("0 - Sair")


while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        cidade = input("Digite a cidade: ")

        clima = buscar_clima(cidade)

        if clima:

            print("\n====== CLIMA ======")
            print(f"Cidade: {clima['cidade']}")
            print(f"Temperatura: {clima['temperatura']}°C")
            print(f"Sensação térmica: {clima['sensacao']}°C")
            print(f"Umidade: {clima['umidade']}%")
            print(f"Condição: {clima['descricao']}")

    elif opcao == "2":

        nome_filme = input("Digite o nome do filme: ")

        filme = buscar_filme(nome_filme)

        if filme:

            print("\n====== FILME ======")
            print(f"Título: {filme['titulo']}")
            print(f"Lançamento: {filme['lancamento']}")
            print(f"Sinopse: {filme['sinopse']}")

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")