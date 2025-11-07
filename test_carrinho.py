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
            

if __name__ == "__main__":
    unittest.main()