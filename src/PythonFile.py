
fragmentos = re.sub('[^a-zA-Z \n]+', '', open("fragmentos").read()).split('\n')
palavras = re.sub('[^a-zA-Z \n]+', '', open("palavras").read()).split('\n')

fragmentos = [frag.lower() for frag in fragmentos]
palavras = [palavra.lower() for palavra in palavras]

palavrasLocal = None
fragmentosLocal = []

verificadas = []


def percorre_palavras(palavras):
    global verificadas

    if len(palavras) == 0:
        return

    else:
        palavra = palavras.pop(0)
        if percorre_fragmentos(palavra):
            verificadas.append(palavra)

    percorre_palavras(palavras)


def alimenta_corrida(palavra, idx=0):
    pass


def percorre_fragmentos(palavra, idx=0):
    if idx >= len(fragmentos):
        return False

    fragmento = fragmentos[idx]

    if len(palavra) == 0:
        return True

    elif len(palavra) >= len(fragmento):
        if palavra[:len(fragmento)] == fragmento:
            return percorre_fragmentos(palavra[len(fragmento):], 0)

    percorre_fragmentos(palavra, idx+1)


'''
    Como percorrer a lista de novo a partir de onde a palavra não achou nos fragmentos
    Exemplo:
        comecou a percorer a palavra camiseta
        chegou no estado seta
        achou o s
        palavra se torna eta
        não acha fragmento que complete
        volta para seta
        procura proximo fragmento que completaria
        se completa
        termina de completar a palavra
'''


if __name__ == "__main__":
    percorre_palavras(palavras)
    for i in verificadas:
        print(i)