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
            senha = "P" + str(self._contador[tipo])
            self._prioritarias.append(senha)
        else:
            senha = "N" + str(self._contador[tipo])
            self._normais.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def chamar(self):
        if not self._normais and not self._prioritarias:
            raise IndexError("fila vazia")
        if self._prioritarias and (self._seguidas < 2 or not self._normais):
            self._seguidas += 1
            return self._prioritarias.popleft()
        self._seguidas = 0
        return self._normais.popleft()
