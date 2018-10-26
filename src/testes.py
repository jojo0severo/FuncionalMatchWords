from functools import reduce


# teste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(reduce(lambda x, y: x+ '\n' + y , teste))
# exit()
# print('\n'.join(teste))


# Testa compressão de lista para percorrer lista de palavras
# No java é o equivalente à: lista.forEach(v -> func(v))

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


saida1 = open('../arquivos/saida_teste1', 'r').read().split('\n')
saida2 = open('../arquivos/saida_teste2', 'r').read().split('\n')

saida1.sort()
saida2.sort()

if saida1 == saida2:
    print('Eh verdade esse bilete')
else:
    print('ERROOOOWW')
