from functools import reduce
from unicodedata import normalize
#
#
# teste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(reduce(lambda x, y: x+ '\n' + y , teste))
# exit()
# print('\n'.join(teste))
#
#
# Testa compressão de lista para percorrer lista de palavras
# No java é o equivalente à: lista.forEach(v -> func(v))
#
# def func(x):
#     if x == 'c':
#         return False
#     return True
#
#
# lista = ['a','b','c','d','e','f','g']
#
# lista = [palavra for palavra in lista if func(palavra)]
# print(lista)
#
#
# saida1 = open('../src/testes/saida_teste1', 'r').read().split('\n')
# saida2 = open('../src/testes/saida_teste2', 'r').read().split('\n')
#
# saida1.sort()
# saida2.sort()
#
# if saida1 == saida2:
#     print('Eh verdade esse bilete')
# else:
#     print('ERROOOOWW')
#
# open('arquivos/palavras', 'r').read()
#
# aux = open("../../arquivos/palavras", 'r', encoding='utf-8').read()
#
#
# def normatiza_palavra(palavra):
#     return normalize('NFKD', palavra).encode('ascii', 'ignore').decode('ascii')
#
#
# palavras = [normatiza_palavra(palavra.lower())
#             for palavra in set(open("../../arquivos/muitas_palavras", encoding='utf-8').read().split('\n'))
#                 if palavra.isalpha() and len(palavra) > 3]
#
#
# for p in palavras:
#     if str(p).__contains__('cipe'):
#         print(p)


aux = open('../../src/testes/possivel_repetido', 'r', encoding='utf-8').read().split('\n')

for p in aux:
    for j in range(aux.index(p)+1, len(aux)):
        if p == j:
            print('eh igual')
            exit()