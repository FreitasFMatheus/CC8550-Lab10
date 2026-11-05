CUPONS = {  # codigo -> (porcentagem de desconto, subtotal minimo)
    "DEZ": (10, 10000),
    "VINTE": (20, 30000),
}


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._cupom = None

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        if type(quantidade) is not int or quantidade < 1:
            raise ValueError("quantidade invalida")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._cupom = codigo

    @property
    def total(self):
        if self._cupom is None:
            return self._subtotal
        porcentagem, minimo = CUPONS[self._cupom]
        if self._subtotal < minimo:
            return self._subtotal
        return self._subtotal * (100 - porcentagem) // 100
