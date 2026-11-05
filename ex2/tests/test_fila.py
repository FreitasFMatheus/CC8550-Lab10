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
