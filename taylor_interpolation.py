import numpy as np
from scipy.interpolate import approximate_taylor_polynomial
import sympy as sym
class TaylorInter:
    def __init__(self, func, point, degree):
        self.func = func
        self.point = point
        self.degree = degree

    def taylor_inter(self):
        # Calcula la aproximación de Taylor 

        taylor_approximation = approximate_taylor_polynomial(self.func, self.point, self.degree, 1)
        return str(taylor_approximation)
