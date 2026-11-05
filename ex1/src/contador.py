def contar_palavras(texto):
    contagem = {}
    for palavra in texto.split():
        contagem[palavra] = 1
    return contagem
