def exec_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = exec_merge_sort(lista[:meio])
        direita = exec_merge_sort(lista[meio:])
        return exec_merge(esquerda, direita)
        
        
def exec_merge(esquerda, direita):
    sub_lista_ordenada=[]
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita +=1
            
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada
    
lista = [ 10,8,7, 3,2,1]
print(exec_merge_sort(lista))



"usando recursividade"

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursivamente ordena as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Combina as duas metades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se há elementos restantes em left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica se há elementos restantes em right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Exemplo de uso
    arr = [12, 11, 13, 5, 6, 7]
    print("Array original:", arr)
    merge_sort(arr)
    print("Array ordenado:", arr)

if __name__ == "__main__":
    main()
