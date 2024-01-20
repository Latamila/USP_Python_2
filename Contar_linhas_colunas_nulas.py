def cria_matriz(num_linhas, num_colunas,valor):
  matriz = [] #lista vazia
  for i in range(num_linhas):
    #cria a lista i
    linha = [] #lista vazia
    for j in range(num_colunas):
      linha.append(valor)
    matriz.append(linha)
    #adciona a linha à matriz

    
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

def nulos(m): 
  linhas_nulas = 0
  colunas_nulas = 0
  colunas = 0
  linhas = 0
  for i in range(len(m)):
    linhas = 0
    for j in range(len(a[0])):
      num = m[i][j]
      linhas += num
    if linhas == 0:
      linhas_nulas += 1
  print(f'Linhas nulas = {linhas_nulas}')
  for j in range(len(m[0])):
    colunas = 0 
    for i in range(len(m)):
      num = m[i][j]
      colunas += num
    if colunas == 0:
      colunas_nulas += 1
  print(f'Coluns nulas = {colunas_nulas}')

def main():
  m = int(input('digite o numero de linhas: '))
  n = int(input('digite o numero de colunas(diferente do numero de linhas): '))
  print(f'Matriz: {m} x {n}')
  matriz = cria_matriz(m,n)
  imprima_matriz(matriz)
  nulos(matriz)
    
main()
'''
    Escreva um programa que leia inteiros positivos m e n 
    e os elementos de uma matriz A de números inteiros de dimensão 
    m x n e conta o número de linhas e colunas que tem apenas zeros.
'''
