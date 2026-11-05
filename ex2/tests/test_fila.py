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


def test_normais_por_chegada():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    assert f.chamar() == "N1"
    assert f.chamar() == "N2"
    assert f.aguardando == 0


def test_prioritaria_na_frente():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"
    assert f.chamar() == "N1"


def test_prioritarias_por_chegada():
    f = Fila()
    f.emitir("prioritaria")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"
    assert f.chamar() == "P2"


def test_normal_depois_de_duas_prioritarias():
    f = Fila()
    f.emitir("normal")
    for _ in range(3):
        f.emitir("prioritaria")
    assert [f.chamar() for _ in range(4)] == ["P1", "P2", "N1", "P3"]


def test_contagem_zera_apos_normal():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    for _ in range(4):
        f.emitir("prioritaria")
    assert [f.chamar() for _ in range(6)] == ["P1", "P2", "N1", "P3", "P4", "N2"]
