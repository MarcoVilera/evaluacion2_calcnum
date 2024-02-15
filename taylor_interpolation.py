import numpy as np
from scipy.interpolate import approximate_taylor_polynomial

class TaylorInter:
    def __init__(self, func, point, degree):
        self.func = func
        self.point = point
        self.degree = degree

    def taylor_inter(self, x):
        # Calcula la aproximación de Taylor 

        taylor_approximation = approximate_taylor_polynomial(self.func, self.point, self.degree, 1)
        return taylor_approximation(x)

a = TaylorInter(np.exp, 0, 5)

try:
    x_value = int(input("Ingrese el valor de x a evaluar en la funcion: \n"))
    resultado = a.taylor_inter(x_value)
    print(f"Aproximación de Taylor en x = {x_value}: {resultado}")

except:
    print("Verifique los datos e ingreselos nuevamente")
