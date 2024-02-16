import numpy as np


# La clase PotenciaSim representa una simulación de potencia con atributos m que es una matriz e 
#i es el numero de iteraciones.
class PotenciaSim:
    def __init__(self,m,i):
        self.m = m
        self.i= i
        
    def pot_sym(self):
        """
        Calcula los valores propios y los vectores propios de una matriz simétrica.
        :devuelve: una lista de cadenas, donde el primer elemento es el valor propio y el segundo el
        el vector propio.
        """


        # El código `if not PotenciaSim.isSymetric(self): return "prueba fallida"` verifica si la
        # matriz `m` es simétrica o no. Si la matriz no es simétrica, devuelve la cadena "prueba
        # fallida".
        if not PotenciaSim.isSymetric(self): return "test failed"
            
        n = self.m.shape[0]
        v = np.random.rand(n)
        v /= np.linalg.norm(v)

        for i in range (self.i):
            w = np.dot(self.m,v)
            norma = np.linalg.norm(w)
            v = w / norma
            eigenvalor = np.dot(v,np.dot(self.m,v))
        values = [str(eigenvalor),str(v)]
        return values


    def isSymetric(self):
        """
        La función comprueba si una matriz es simétrica comparando sus dimensiones.
        :return: un valor booleano. Si el número de filas es igual al número de columnas de la matriz,
        devuelve Verdadero. De lo contrario, devuelve Falso.
        """
        size= np.shape(self.m)
        if size[0] == size[1]: return True
        else: return False
