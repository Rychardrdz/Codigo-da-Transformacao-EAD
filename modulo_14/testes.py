from django.test import TestCase

from .models import Produto


class ProdutoTest(TestCase):

    def test_criar_produto(self):

        produto = Produto.objects.create(
            nome="Teclado",
            descricao="Teclado Gamer",
            preco=200,
            quantidade=5
        )

        self.assertEqual(produto.nome, "Teclado")