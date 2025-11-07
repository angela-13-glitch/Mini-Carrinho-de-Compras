class Produto:
 

    def __init__(self, nome: str, preco: float, quantidade: int):
        if not isinstance(preco, (int, float)):
            raise TypeError
        if not isinstance(quantidade, int):
            raise TypeError
        if preco <= 0 or quantidade <= 0:
            raise ValueError
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = quantidade

    def subtotal(self) -> float:
       
        return self.preco * self.quantidade


class Carrinho:
 

    def __init__(self):
        self.itens: dict[str, Produto] = {}

    def adicionar_produto(self, produto: Produto) -> None:
      
        existente = self.itens.get(produto.nome)
        if existente:
            existente.quantidade += produto.quantidade
        else:
            self.itens[produto.nome] = produto

    def remover_produto(self, nome_produto: str) -> None:
    
        self.itens.pop(nome_produto, None)

    def calcular_total(self) -> float:
      
        return sum(produto.subtotal() for produto in self.itens.values())

