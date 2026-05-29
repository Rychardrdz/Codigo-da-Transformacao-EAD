def soma(a, b):
    return a + b


class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):

        if b == 0:
            raise ValueError("Não pode dividir por zero")

        return a / b