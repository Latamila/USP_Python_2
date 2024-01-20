'''
  Escreva um programa que leia duas matrizes, a matriz A de dimensão m x n e B 
  de dimensão n x p e imprime a matriz C de dimensão m x p que é
   o produto de A por B.'''

def imprima_matriz(m):
  #itera sob as linhas da matriz
  for i in range(len(m)):
    linha = []#cria uma linha nova a cada iteração
    #preenche com valores na coluna correspondente
    #ao pegar o valor de len do primeiro elemento 'm[0]'
    #de m, saberei quantas colunas tem na matriz.
    for j in range(len(m[0])):
      linha.append(str(m[i][j]))#mudo tipo para string para usar a função join
    print(' '.join(linha))

def cria_matriz(num_linhas, num_colunas):
  matriz = [] #lista vazia
  for i in range(num_linhas):
    #cria a lista i
    linha = [] #lista vazia
    for j in range(num_colunas):
      valor = int(input(f'Digite o elemento [{str(i)}][{str(j)}]: '))
      linha.append(valor)
    matriz.append(linha)
    #adciona a linha à matriz
  return matriz

def le_matriz():
  linha = int(input('Digite o numero de linhas da matriz: '))
  coluna = int(input('Digite o numero de colunas da matriz: '))
  matriz = cria_matriz(linha,coluna)
  return matriz

def pega_linha(matriz, n):
  return  [i for i in matriz[n]]# ou simplesmente return matriz[n]
  #pra pegar todos os numeros da linha n(p.ex, linha 1)

def pega_coluna(matriz, n):
  return [i[n] for i in matriz]#pegando o numero da coluna 'n'(p.ex coluna 1)


def multiplica_matriz(m1,m2):
  matriz_resultado = []
  matriz1_linha = len(m1)
  matriz1_coluna = len(m1[0])

  matriz2_linha = len(m2)
  matriz2_coluna = len(m2[0])
  for i in range(matriz1_linha): #valor de linhas da primeira
    matriz_resultado.append([])
    for j in range(matriz2_coluna):#valor de colunas da segunda
      #multiplica cada linha de mat1 por cada coluna de mat2
      lista_mult = [x*y for x,y in zip(pega_linha(m1, i), pega_coluna(m2, j))]
      # e em seguida adiciona a matriz_resultado a soma
      #das multiplicações

      matriz_resultado[i].append(sum(lista_mult))
  return matriz_resultado

def imprima_matriz(m):
  #itera sob as linhas da matriz
  for i in range(len(m)):
    linha = []#cria uma linha nova a cada iteração
    #preenche com valores na coluna correspondente
    #ao pegar o valor de len do primeiro elemento 'm[0]'
    #de m, saberei quantas colunas tem na matriz.
    for j in range(len(m[0])):
      linha.append(str(m[i][j]))#mudo tipo para string para usar a função join
    print(' '.join(linha))

def main():
  m1 = le_matriz()
  m2 = le_matriz()
  c =multiplica_matriz(m1,m2)
  imprima_matriz(c)

main()
