SINAIS = ".,;:!?"


def contar_palavras(texto):
    contagem = {}
    for bruta in texto.split():
        palavra = bruta.lower().strip(SINAIS)
        if palavra:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
