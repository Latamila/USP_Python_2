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

