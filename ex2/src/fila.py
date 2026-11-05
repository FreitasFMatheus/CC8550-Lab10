class Fila:
    def __init__(self):
        self._contador = {"normal": 0, "prioritaria": 0}
        self._senhas = []

    def emitir(self, tipo):
        if tipo not in self._contador:
            raise ValueError("tipo invalido")
        self._contador[tipo] += 1
        letra = "P" if tipo == "prioritaria" else "N"
        senha = letra + str(self._contador[tipo])
        self._senhas.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._senhas)
