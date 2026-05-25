def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("A idade não pode ser negativa.")
                continue
            return idade
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

# Teste
idade_usuario = obter_idade()
print(f"Idade registrada: {idade_usuario}")