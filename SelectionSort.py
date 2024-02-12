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
