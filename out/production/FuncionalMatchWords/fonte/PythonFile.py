import re
import sys
from functools import reduce

# Define o tamanho máximo da pilha de recursão
sys.setrecursionlimit(10000)

# Cria uma lista de fragmentos unicos sem acentos e caracteres especiais
fragmentos = list(set(re.sub('[^a-zA-Z \n]+', '', open("../../arquivos/fragmentos")
                             .read()).split('\n')))


# Cria uma lista de palavras unicas sem acentos e caracteres especiais
palavras = list(set(re.sub('[^a-zA-Z \n]+', '', open("../../arquivos/muitas_palavras", encoding='utf-8')
                           .read()).split('\n')))


# Cria uma lista de fragmentos com todos os fragmentos minusculos
fragmentos = [frag.lower() for frag in fragmentos]


# Cria uma lista de palavras com quantidade de caracteres maior que 3 e minusculas
palavras = [palavra.lower() for palavra in palavras if len(palavra) > 3]


def percorre_fragmentos(palavra, idx=0):
    # Verifica se o indice (idx) eh maior ou igual ao tamanho de fragmentos
    if idx >= len(fragmentos):
        return False

    # Inicializa duas variáveis -> um, dois = valor_um, valor_dois
    bla, fragmento = False, fragmentos[idx]

    # Se a palavra estiver vazia
    if not palavra:
        return True

    # Verifica se a palavra, do inicio ate o tamanho do fragmento, eh igual ao fragmento
    elif palavra[:len(fragmento)] == fragmento:

        # Guarda estado da recursao. Caso a primeira descida nao tenha sido sucesso, ela volta
        # pra onde deu certo e tenta de novo
        bla = percorre_fragmentos(palavra[len(fragmento):], 0)

    return bla or percorre_fragmentos(palavra, idx + 1)


if __name__ == "__main__":
    # Percorre todas as palavras e retorna as palavras que foram aceitas pelo metodo
    verificadas = [palavra for palavra in palavras if percorre_fragmentos(palavra)]

    # Concatena todas as palvras separando por \n
    palavras_finais = reduce(lambda x, y: x + '\n' + y, verificadas)

    # Salva no arquivo dentro da pasta arquivos
    open('../../arquivos/saida', 'w').write(palavras_finais)
