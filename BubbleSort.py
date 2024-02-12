class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista) #chega ao fim quando percorrer
        #toda a lista
    
        for i in range(fim - 1):
        #inicialmente, o menor elemento já visto 
            #é o i-esimo. 
            posicao_do_minimo = i

            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

        #coloca o menor elemento encontrado no inicio da sublista
        #para isso troca de lugar os elementos nas posições
        #j e posição do minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return  lista
