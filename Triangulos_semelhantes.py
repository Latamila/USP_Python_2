class Triangle(object):
    def __init__(self,a,b, c):
        self.lados = sorted([a,b,c])
    
    def semelhantes(self, outro):
        x = outro.lados        
        if self.lados[0] >= x[0] and self.lados[1] >= x[1] and self.lados[2] >= x[2]:
            if self.lados[0] % x[0] == 0 and self.lados[1] % x[1] == 0 and self.lados[2] % x[2] == 0:
                return True
            else:
                return False
            
        if x[0] >= self.lados[0] and x[1] >= self.lados[1] and x[2] >= self.lados[2]:
            if x[0] % self.lados[0] == 0 and x[1] % self.lados[1] == 0 and x[2] % self.lados[2] == 0:
                return True
            else: 
                return False
            
        if self.lados[0] == self.lados[1] and self.lados[2] and x[0] == x[1] == x[2]:
            return True
        else:
            return False


print('Triangles')
t1 = Triangle(3,3,3)
t2 = Triangle(6,6,6)

print(t1.semelhantes(t2))
# deve devolver True
t1 = Triangle(3,4,5)
t2 = Triangle(6,8,10)

print('Triangles')
t1 = Triangle(6,8,10)
t2 = Triangle(3,4,5)

print(t1.semelhantes(t2))
# deve devolver True

print('Triangles')
t1 = Triangle(6,8,10)
t2 = Triangle(3,4,6)

print(t1.semelhantes(t2))
# deve devolver True
