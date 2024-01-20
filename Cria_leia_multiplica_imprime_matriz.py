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
