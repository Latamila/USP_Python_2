#-----------------------------------------------


def pegando_linha(matriz, linha):
  return [i for i in matriz[linha]]

def pegando_coluna(matriz, coluna):
  return [i[coluna] for i in matriz]


def produto_lincol(lin, a_mat, col, b_mat):
  matRes = []
  for i in range(len(a_mat)):
    if i == lin:
      matRes.append([])
      for j in range(len(b_mat[0])):
        if j == col:
          listMult = [x*y for x,y in zip(pegando_linha(a_mat, i),
                                         pegando_coluna(b_mat,0))]
  return listMult

A = [ [1, 2, 1],
      [2, 2, 2],
      [1, 3, 2]]
B = [ [1, 1],
      [2, 0],
      [0, 1] ]

produto_lincol(1,A,0,B)
