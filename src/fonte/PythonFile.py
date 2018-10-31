import re
import sys
from functools import reduce
from unicodedata import normalize

sys.setrecursionlimit(10000)


def normatiza_palavra(palavra):
    return normalize('NFKD', palavra).encode('ascii', 'ignore').decode('ascii')


fragmentos = [normatiza_palavra(palavra.lower())
              for palavra in set(open("../../arquivos/fragmentos", encoding='utf-8').read().split('\n'))
                if palavra.isalpha()]

palavras = [normatiza_palavra(palavra.lower())
            for palavra in set(open("../../arquivos/muitas_palavras", encoding='utf-8').read().split('\n'))
                if palavra.isalpha() and len(palavra) > 3]




def percorre_fragmentos(palavra, idx=0):
    if idx >= len(fragmentos):
        return False

    bla, fragmento = False, fragmentos[idx]

    if not palavra:
        return True

    elif palavra[:len(fragmento)] == fragmento:
        bla = percorre_fragmentos(palavra[len(fragmento):], 0)

    return bla or percorre_fragmentos(palavra, idx + 1)


if __name__ == "__main__":
    verificadas = [palavra for palavra in palavras if percorre_fragmentos(palavra)]

    palavras_finais = reduce(lambda x, y: x + '\n' + y, verificadas)

    open('../../arquivos/saida', 'w').write(palavras_finais)
