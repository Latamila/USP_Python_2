class BuscaBinaria:
    def busca_sequencial(self,lista,x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1
    def busca_binaria(self,lista,x):
        primeiro = 0 
        ultimo = len(lista) - 1
        
        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio + 1
                    
        return -1
    
lista = [-100,0,20,30,50,100,3000,5000]

b= BuscaBinaria()

print(b.busca_binaria(lista, 100))
print(len(lista))

print(b.busca_binaria(lista, 70))


def busca(lista,x):
        primeiro = 0 
        ultimo = len(lista) - 1
        
        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            print(meio)
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio + 1
                    
        return False
    
print(busca([1,2,3,4,5],6))
print(busca(['a','e','i'],'e'))
print('x'*15)
print(busca([1,2,3,4,5,6],4))
print('*'*15)

def bolha_curta(lista):
    fim = len(lista)

    for i in range(fim-1,0,-1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if not trocou:
            return  lista
    return lista
print(bolha_curta([1,5,3,4,2,0]))
print('-'*20)

def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j]. 
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
            
        array[j+1] = key
    return array

data = [9,5,1,4,3]
insertion_sort(data)
print('sorted data')
print(data)        

print('%'*20)
def x(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))

print('%'*20)


def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio
    
    

a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
print(busca_binaria(a, 99))
print('---------' * 10)
def x(n):
    if n == 0:
        print(n)
    else:
        x(n-1)
        print(n)
    

x(10)




'''
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
'''
def soma_lista(lista):
    if not lista:
        return 0 
    else:
        return lista[0] + soma_lista(lista[1:])



'''
Implemente a função encontra_impares(lista), que recebe como parâmetro uma 
lista de números inteiros e devolve uma outra lista apenas com os números
ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''




def encontra_impares(lista):
    # Lista para armazenar os números ímpares
    impares = []
    
    # Caso base: se a lista estiver vazia, retornar a lista de números ímpares
    if not lista:
        return impares
    
    # Verificar se o primeiro elemento da lista é ímpar
    if lista[0] % 2 != 0:
        impares.append(lista[0])

    # Chamar recursivamente a função para o restante da lista e estender a lista de números ímpares
    impares.extend(encontra_impares(lista[1:]))
    
    return impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(encontra_impares(lista)) 




'''
User
Este exercício tem duas partes:

Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. Essa função deve ser implementada utilizando recursão.

Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também que é possível transformar números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de 
�
=
=
1
n==1?

No exemplo de execução abaixo, note que há uma diferença entre como a string é e como ela é interpretada. Na função print o símbolo "\n" é interpretado como quebra de linha
'''

def incomodam(n):
    if not isinstance(n, int) or n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n <= 1:
        return ""
    elif n == 2:
        return "Um elefante incomoda muita gente\n2 elefantes " + incomodam(2) + "muito mais\n"
    else:
        frase_anterior = elefantes(n-1)
        nova_frase = str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
        return frase_anterior + nova_frase

# Testando a função elefantes para n = 4
print(elefantes(4))

'''
FIBONACCI RECURSIVO
'''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

'''
FATORIAL RECURSIVO 
'''

def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)
