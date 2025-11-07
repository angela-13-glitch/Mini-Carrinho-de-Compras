
import unittest
from carrinho import Carrinho, Produto

class TestCarrinho(unittest.TestCase):

    def test_adicionar_produto(self):
        carrinho = Carrinho()
        produto = Produto("Maçã", 2.5, 3)
        carrinho.adicionar_produto(produto)
        self.assertEqual(len(carrinho.itens), 1)
        self.assertEqual(carrinho.itens["Maçã"].quantidade, 3)

    def test_nao_permitir_preco_ou_qtd_invalidos(self):
        with self.assertRaises(ValueError):
            Produto("Banana", 0, 2)
        with self.assertRaises(ValueError):
            Produto("Banana", 2, 0)
        with self.assertRaises(TypeError):
            Produto("Banana", "2", 3)

    def test_somar_quantidades_mesmo_produto(self):
        carrinho = Carrinho()
        carrinho.adicionar_produto(Produto("Maçã", 2.5, 2))
        carrinho.adicionar_produto(Produto("Maçã", 2.5, 3))
        self.assertEqual(carrinho.itens["Maçã"].quantidade, 5)

    def test_remover_produto(self):
        carrinho = Carrinho()
        carrinho.adicionar_produto(Produto("Pera", 3.0, 2))
        carrinho.remover_produto("Pera")
        self.assertEqual(len(carrinho.itens), 0)

    def test_calcular_total(self):
        carrinho = Carrinho()
        carrinho.adicionar_produto(Produto("Maçã", 2.0, 2))
        carrinho.adicionar_produto(Produto("Banana", 3.0, 1))
        self.assertEqual(carrinho.calcular_total(), 7.0)

if __name__ == "__main__":
    unittest.main()