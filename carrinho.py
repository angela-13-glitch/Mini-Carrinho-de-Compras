class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        if not isinstance(preco, (int, float)) or not isinstance(quantidade, int):
            raise TypeError("Preço deve ser numérico e quantidade deve ser inteira.")
        if preco <= 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser maiores que zero.")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto: Produto):
        if produto.nome in self.itens:
            self.itens[produto.nome].quantidade += produto.quantidade
        else:
            self.itens[produto.nome] = produto

    def remover_produto(self, nome_produto: str):
        if nome_produto in self.itens:
            del self.itens[nome_produto]

    def calcular_total(self) -> float:
        return sum(p.preco * p.quantidade for p in self.itens.values())

