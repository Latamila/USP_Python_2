'''
Vamos criar um módulo como exemplo que recebe duas funções. 
'''


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end = ' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0,1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result



'''
* Salve o arquivo como fibo.py
* Vamos ao prompt de comando
* Abre o diretorio que está armazenado seu arquivo (use o comando cd, se houver qualquer dificuldade de saber o caminho, va ate o seu arquivo, clique com botao esquerdo do mouse, e entre em propriedades. é possivel copiar e colar o caminho por la. 

*digite python para abrir um terminal python no seu diretorio e depois vamos importar o nosso modulo criado. 

import fibo

Dentro do fibo ha duas funções, entaõ para chama-las devemos declarar fibo.fib ou fibo.fib2. 

'''
'''
Para rodar a instrução sem precisar importar como módulo e sim como script
'''
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))

'''  
Neste script acima, vemos que se no nosso terminal o arquivo fibo está rodando como script é possivel fazer outras coisas como importar uma biblioteca que roda os modulos dentro dele sem precisar importar, que é a biblioteca sys. 

Nela usamos a função argv, convertendo seu retorno para inteiro. A função argv pega o primeiro argumento passado pelo usuario e por isso o numero 1 passado como parametro.
'''
