import unittest

from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):

        self.calc = Calculadora()

    def test_somar(self):

        resultado = self.calc.somar(10, 5)

        self.assertEqual(resultado, 15)

    def test_dividir(self):

        resultado = self.calc.dividir(10, 2)

        self.assertEqual(resultado, 5)

    def test_divisao_por_zero(self):

        with self.assertRaises(ValueError):

            self.calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()