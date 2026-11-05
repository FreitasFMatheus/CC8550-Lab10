import pytest
from fila import Fila

def test_primeira_normal():
    f = Fila()
    assert f.emitir("normal") == "N1"
