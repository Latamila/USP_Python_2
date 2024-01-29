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

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
carro_vovo = Carro('ranger', 2000, 'preto')
print(carro_vovo.cor)

#projeto 2
