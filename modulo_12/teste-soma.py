import unittest

from calculadora import soma


class TestSoma(unittest.TestCase):

    def test_soma(self):

        resultado = soma(5, 5)

        self.assertEqual(resultado, 10)


if __name__ == "__main__":
    unittest.main()