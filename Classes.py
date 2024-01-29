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
