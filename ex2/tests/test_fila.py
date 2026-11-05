import pytest
from fila import Fila

def test_primeira_normal():
    f = Fila()
    assert f.emitir("normal") == "N1"


def test_primeira_prioritaria():
    f = Fila()
    assert f.emitir("prioritaria") == "P1"


def test_numeracao_por_tipo():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.emitir("normal") == "N2"
    assert f.emitir("prioritaria") == "P2"


def test_tipo_invalido():
    f = Fila()
    with pytest.raises(ValueError):
        f.emitir("vip")


def test_aguardando():
    f = Fila()
    assert f.aguardando == 0
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.aguardando == 2


def test_chamar_vazia():
    f = Fila()
    with pytest.raises(IndexError):
        f.chamar()
