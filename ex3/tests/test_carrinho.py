import pytest
from carrinho import Carrinho


def test_vazio():
    assert Carrinho().total == 0


def test_um_item():
    c = Carrinho()
    c.adicionar(2500)
    assert c.total == 2500


def test_quantidade_dois():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000


def test_preco_zero_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)


def test_cupom_dez_no_minimo():
    c = Carrinho()
    c.adicionar(5000, quantidade=2)
    c.aplicar_cupom("DEZ")
    assert c.total == 9000


def test_cupom_desconhecido():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


def test_item_depois_do_cupom():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(10000)
    assert c.total == 9000


def test_dez_abaixo_do_minimo():
    c = Carrinho()
    c.adicionar(9999)
    c.aplicar_cupom("DEZ")
    assert c.total == 9999

def test_minimo_alcancado_depois_do_cupom():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    c.adicionar(5000)
    assert c.total == 9000

def test_vinte_no_minimo():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    assert c.total == 24000

def test_vinte_abaixo_do_minimo():
    c = Carrinho()
    c.adicionar(29999)
    c.aplicar_cupom("VINTE")
    assert c.total == 29999

def test_segundo_cupom_substitui():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    c.aplicar_cupom("DEZ")
    assert c.total == 27000

def test_quantidade_um_aceita():
    c = Carrinho()
    c.adicionar(100, quantidade=1)
    assert c.total == 100

@pytest.mark.parametrize("quantidade", [0, -1])
def test_quantidade_menor_que_um(quantidade):
    with pytest.raises(ValueError):
        Carrinho().adicionar(100, quantidade=quantidade)

@pytest.mark.parametrize("quantidade", [1.5, 2.0, "2", True])
def test_quantidade_nao_inteira(quantidade):
    with pytest.raises(ValueError):
        Carrinho().adicionar(100, quantidade=quantidade)
