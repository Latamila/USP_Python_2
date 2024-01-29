class Carro():
    pass

meu_carro = Carro()
carro_papai = Carro()

meu_carro.modelo = 'crv'
meu_carro.ano = 2018
meu_carro.cor = 'prata'

carro_papai.modelo = 'palio'
carro_papai.ano = 2006
carro_papai.cor ='prata'

print(meu_carro.modelo)
print(carro_papai.modelo)   

novo_crv = meu_carro
novo_crv.ano += 5

print(novo_crv.ano)
########################################33333
class Carro():
    pass

meu_carro = Carro()
carro_papai = Carro()

meu_carro.modelo = 'crv'
meu_carro.ano = 2018
meu_carro.cor = 'prata'

carro_papai.modelo = 'palio'
carro_papai.ano = 2006
carro_papai.cor ='prata'

print(meu_carro.modelo)
print(carro_papai.modelo)   

novo_crv = meu_carro
novo_crv.ano += 5

print(novo_crv.ano)

#######################################
class Pato():
    pass

pato = Pato()
patinho = Pato()
if pato == patinho:
    print('Estamos no mesmo endereço')
else:
    print('Estamos em endereços diferentes')
    
print(pato)
print(patinho)

#metodo __init__
'''
Conhecido como construtor da classe

Chamado automaticamento pelo interpretador 
quando sao criados
'''
########################################################
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


def main():
    carro1 = Carro('ranger', 2000, 'preto',80)
    carro2 = Carro('hilux', 2009, 'prata',95)
    
    carro1.acelera(40)
    carro2.acelera(50)
    carro1.acelera(80)
    carro1.pare()
    carro2.acelera(100)

#########################################################################

class Carro:
    def __init__(self,m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.velocidade = 0
        self.vmaxima = vm #velocidade maxima
        
    def imprima(self):
        if self.velocidade == 0: #parado dá pra ver o ano
            print('%s %s %d'%(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.vmaxima:
            print('%s %s indo a %d km/h'%(self.modelo, self.cor, self.velocidade))
        else:
            print('%s %s indo muito raaaaapiddoooo!'%(self.modelo, self.cor))
    
    def acelera(self, v):
        self.velocidade = v
        if self.velocidade > self.vmaxima:
            self.velocidade = self.vmaxima
        self.imprima()
        
    def pare(self):
        self.velocidade = 0
        self.imprima()
        
main()
carro_vovo = Carro('ranger', 2000, 'preto')
print(carro_vovo.cor)

#########################################################
#projeto 2 class Carro




######################################################
class Cafeteira:
    def __init__(self, marca, tipo, tamanho, cor):
        self.marca = marca
        self.tipo = tipo
        self.cor = cor
        self.tamano = tamanho
        
#o parametro self é o proprio objeto a ser criado

class Cachorro:
    def __init__(self, raça, idade, nome, cor):
        self.raça = raça
        self.idade = idade
        self.nome = nome
        self.cor = cor
        
rex = Cachorro('vira-lata',2,'Bob','marrom')
print(rex.raça)
print(rex.nome)
print(rex.cor)
print(rex.idade)
print(rex.idade>2)

#######################################
class Lista:
    def append(self, elemento):
        return 'OOps! Este objeto não é uma lista.'
    
lista = []

a = Lista()
b = a.append(7)
 
lista.append(b)

print('lista =',lista,'\n')
print('a = ',a,'\n')
print('b = ',b,'\n')
