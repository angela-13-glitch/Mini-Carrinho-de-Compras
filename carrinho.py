class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        if not isinstance(preco, (int, float)) or not isinstance(quantidade, int):
            raise TypeError("Preço deve ser numérico e quantidade deve ser inteira.")
        if preco <= 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser maiores que zero.")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        