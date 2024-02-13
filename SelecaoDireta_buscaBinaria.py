import random

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


    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return  lista

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

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100))
    return lista

print(lista_grande(10))

def ordena(list):
    n = len(list)
    for i in range(n-1):
        menorindice = i

        for j in range(i + 1, n):
            if list[j] < list[menorindice]:
                menorindice = j

        if menorindice != i:
            temp = list[i]
            list[i] = list[menorindice]
            list[menorindice] = temp
    
    return list

print(ordena([1,10,80,2,4,6,8,13,3]))


lista = [5,1,7,3,2]
o = Ordenador()
o.bolha(lista)

print(lista)

import time

antes = time.time()
o.bolha(lista)

depois = time.time()

print(f'A execução do algoritmo demorou {depois-antes} segundos.')

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = Ordenador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print(f'A execução do Bolha demorou {depois-antes} segundos.')

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print(f'A execução do Seleção Direta demorou {depois-antes} segundos.')

c = ContaTempos()
c.compara(1000)
