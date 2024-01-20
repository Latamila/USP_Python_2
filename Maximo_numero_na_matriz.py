def acha_max(A):
  maximo = A[0][0]
  linha = 0
  coluna = 0
  for i in range(len(A)):
    for j in range(len(A[0])):
      if A[i][j] > maximo:
        maximo = A[i][j]
        linha = i
        coluna = j

  return maximo, linha, coluna 
'''(matriz) -> int, int, int

    Recebe uma matriz A e devolve 3 inteiros:
    k (um maior valor), e sua posicao lin, col.
    '''
  

# teste
A = [ [3, 7, 1], [1, 2, 8], [5, 3, 4]]
acha_max(A)
