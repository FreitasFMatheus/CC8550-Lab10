from collections import deque


class Fila:
    def __init__(self):
        self._contador = {"normal": 0, "prioritaria": 0}
        self._normais = deque()
        self._prioritarias = deque()
        self._seguidas = 0

    def emitir(self, tipo):
        if tipo not in self._contador:
            raise ValueError("tipo invalido")
        self._contador[tipo] += 1
        if tipo == "prioritaria":
            letra, fila = "P", self._prioritarias
        else:
            letra, fila = "N", self._normais
        senha = letra + str(self._contador[tipo])
        fila.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def chamar(self):
        if not self._normais and not self._prioritarias:
            raise IndexError("fila vazia")
        pode_prioritaria = self._seguidas < 2 or not self._normais
        if self._prioritarias and pode_prioritaria:
            self._seguidas += 1
            return self._prioritarias.popleft()
        self._seguidas = 0
        return self._normais.popleft()
