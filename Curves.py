import vector
import typing
from typing import List
import sympy as sym

class curve:

    def __init__(self, gamma_eq_vec: List
                 ):
        self.gamma_equations = gamma_eq_vec
        #define
        self.gamma_equations_symbols = self.find_symbols()
        # might need to make a function for it
        self.domain_symbols = self.find_dim_domain()
        self.dim_domain = len(self.domain_symbols)
        self.dim_codomain = len(gamma_eq_vec)
        self.d_one_gamma_equations = self.compute_derivative()
        self.d_two_gamma_equations = self.compute_second_derivative()


    def find_symbols(self) -> int:
        free_sym = []
        for eq in self.gamma_equations:
            eq_sym = eq.free_symbols
            free_sym.append(eq_sym)
        return free_sym

    def find_dim_domain(self)->int:
        free_sym = []
        for eq in self.gamma_equations:
            eq_sym = eq.free_symbols
            for element in eq_sym:
                if element not in free_sym:
                    free_sym.append(element)
        return free_sym

    #kind of correct but not completely. Only for one variable atm.
    def compute_derivative(self):
        dg_eq = []
        for index,eq in enumerate(self.gamma_equations):
            dg_eq.append(sym.diff(eq,self.domain_symbols[0]))
        return dg_eq

    def compute_second_derivative(self):
        second_dg_eq = []
        for index, eq in enumerate(self.d_one_gamma_equations):
            second_dg_eq.append(sym.diff(eq, self.domain_symbols[0]))
        return second_dg_eq

    '''
    work on 
    def is_regular(self):
        t_vals = []
        for eq in self.d_one_gamma_equations:
            t_vals.append(sym.solve(eq,self.domain_symbols[0]))
        return t_vals
    '''
    def eq_eval(self,eq,eq_val):
        eq1 = eq.subs(eq_val)
        return eq1

    def compute_curvature_kappa(self,t_val):
        mod_1 = self.eq_eval()
        numerator = vector.vector(self.d_one_gamma_equations).cross(vector.vector(self.d_two_gamma_equations))
        denominator = vector.vector(self.d_one_gamma_equations).magnitude()
        return numerator/denominator
"""
COMPUTING ARC-LENGTH
COMPUTING GRADIENT 
COMPUTING TORSION
COMPUTING DERIVATIVE MATRIX 

"""

"""
BOOL :
        (1) Regular 
        (2) unit speed 
        
"""
t = sym.symbols("t")

f = [sym.exp(t),t,sym.exp(-t)]
a = curve(f)
print(a.gamma_equations)
print(a.d_one_gamma_equations)
print(a.d_two_gamma_equations)
#a = vector.vector(a.gamma_equations).magnitude()

print(a.compute_curvature_kappa())