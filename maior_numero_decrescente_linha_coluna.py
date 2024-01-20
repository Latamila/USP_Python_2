#-----------------------------------------------
'''
Parte A
Foi criar a função acha_max()

Parte B

Escreva um programa que, dado dois inteiros nl e nc e uma matriz quadrada 
de dimensão nl x nc, cujos elementos são todos inteiros, imprime uma tabela 
onde os elementos são listados em ordem decrescente, acompanhados da indicação 
de linha e coluna a que pertencem. Havendo repetições de elementos na matriz, 
a ordem é irrelevante. Utilize obrigatoriamente o procedimento da parte A, 
mesmo que você não o tenha feito.
'''

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

def main():
    A = le_matriz()
    inicio = acha_max(A)
    iniciado = inicio[0]
    passo = inicio[0]
    while passo > -1 :
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == iniciado:
                    print(iniciado,'\t', i,'\t', j)
        iniciado -= 1
        passo -= 1

#-----------------------------------------------
main()
