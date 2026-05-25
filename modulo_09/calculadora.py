def divisao(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"
    else:
        return f"Resultado: {resultado}"

# Teste
print(divisao(10, 2))
print(divisao(10, 0))