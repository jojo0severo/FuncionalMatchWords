import re

fragmentos = re.sub('[^a-zA-Z \n]+', '', open("fragmentos").read()).split('\n')
palavras = re.sub('[^a-zA-Z \n]+', '', open("palavras").read()).split('\n')

fragmentos = [frag.lower() for frag in fragmentos]
palavras = [palavra.lower() for palavra in palavras]

palavrasLocal = None
fragmentosLocal = []

verificadas = []


def percorre_palavras(palavras):
    global verificadas

    # verifica se a lista está vazia (funciona, acredite)
    if palavras:
        palavra = palavras.pop(0)
        if percorre_fragmentos(palavra):
            verificadas.append(palavra)

        percorre_palavras(palavras)


def percorre_fragmentos(palavra, idx=0):
    if idx >= len(fragmentos):
        return False

    fragmento = fragmentos[idx]

    if palavra:
        return True

    elif len(palavra) >= len(fragmento):
        if palavra[:len(fragmento)] == fragmento:
            return percorre_fragmentos(palavra[len(fragmento):], 0)

    percorre_fragmentos(palavra, idx+1)


if __name__ == "__main__":
    percorre_palavras(palavras)
    for i in verificadas:
        print(i)