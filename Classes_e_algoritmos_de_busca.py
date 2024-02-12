class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista) #chega ao fim quando percorrer
        #toda a lista
    
        for i in range(fim - 1):
        #inicialmente, o menor elemento já visto 
            #é o i-esimo. 
            posicao_do_minimo = i

            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

        #coloca o menor elemento encontrado no inicio da sublista
        #para isso troca de lugar os elementos nas posições
        #j e posição do minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

import random 

lista1 = random.sample(range(800), 100)
print(lista1)
lista = [10,3,8,-10,200,17,32]

o = Ordenador()

o.selecao_direta(lista)

print(lista)
print('*'*15)
o.selecao_direta(lista1)
print(lista1)

def busca_sequencial(seq, x):
    for i in range(len(seq)):
        print(f'Numero: {seq[i]} na posição {i}')
        if seq[i] == x:
            return f'Achei o {seq[i]} na posição {i}'
    return False

lista2= [10,3,8,-10,200,17,32]
print(busca_sequencial(lista2, 17))


def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

numeros = [55,33,0,900,-432,10,77,123,11]

print(busca_sequencial(numeros, 33))
print(busca_sequencial(numeros, -432))


'''
Quantas vezes o valor 2 será trocado 
de lugar, dentro da lista, até ser 
,
colocado na posição certa da lista ordenada?
'''

def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim - 1):
        pos_menor = i
        for j in range(i + 1, fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
        print(lista)#mostra a lista a cada interação
        #e se conseguir perceber as mudanças dos numeros 
    return lista

numeros = [55,33,0,900,-432,10,77,2,11]

print(selecao_direta(numeros))


def busca(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return False

print(busca(['a','b','c','d','e','f'],'e'))
print(busca([12,13,14],15))

def ordenada(list):
    comparacao = sorted(list)
    for i in range(len(comparacao)-1):
        if comparacao[i] != list[i]:
            return False
    return True

print(ordenada(['a','b','c','d','e','f']))
print(ordenada(['a','b','c','e','d','g','f']))

