import numpy as np


class PotenciaSim:
    def __init__(self,m,i):
        self.m = m
        self.i= i
        
    def pot_sym(self):
        '''
        '''

        if not PotenciaSim.isSymetric(self): 
            return "test failed"
        n = self.m.shape[0]
        v = np.random.rand(n)
        v /= np.linalg.norm(v)
        
        for i in range (self.i):
            w = np.dot(self.m,v)
            norma = np.linalg.norm(w)

            v = w / norma
            eigenvalor = np.dot(v,np.dot(self.m,v))
        return eigenvalor,v


    def isSymetric(self):
        '''
        Evalua si la función es simetrica utilizando np.shape()
        Args m = Matriz a Evaluar
        '''
        size= np.shape(self.m)
        if size[0] == size[1]: return True
        else: return False
    

a= PotenciaSim(np.array([[4,-2,1],[-2,5,3],[1,3,6]]),100)
c,b=a.pot_sym()
print(c)
print(b)
print(np.sin)