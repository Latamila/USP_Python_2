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


MINA  = -1
 
def contaMinas(campo, lin, col):
    Ldj = [-1,  0,  1, 1, 1, 0, -1, -1]
    Ldi = [-1, -1, -1, 0, 1, 1,  1,  0]
    m = len(campo)
    n = len(campo[0])
    minas = 0
    for k in range(len(Ldj)):
        i = lin + Ldi[k]
        j = col + Ldj[k]
        if i >= 0 and i < m and j >= 0 and j < n:
            if campo[i][j] == MINA:
                    minas += 1
    return minas 

bomba = -1
livre = 0
def main():
    matriz = le_matriz()
    lin = int(input('digite a linha que quer analisar: '))
    col = int(input('digite a coluna que quer analisar: '))
    risco = contaMinas(matriz,lin, col)

    return risco

#-----------------------------------------------
main()
