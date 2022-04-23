#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:34:49 2021

@author: lucia
"""

import sympy as sy
from scipy.integrate import dblquad

u, v = sy.symbols('u, v', real = True)
x, y, z, t = sy.symbols('x, y, z, t', real = True)

u0 = -1
v0 = 1

##modificar
sup = [sy.exp(u-v), u+v, 2*u+v**2]

#derivadas:
sdu = [sy.diff(sup[i], u) for i in range(3)] 
sdv = [sy.diff(sup[i], v) for i in range(3)]


#calcular E,F,G
E = sy.Matrix(sdu).dot(sy.Matrix(sdu))
F = sy.Matrix(sdu).dot(sy.Matrix(sdv))
G = sy.Matrix(sdv).dot(sy.Matrix(sdv))

E = E.subs(u,u0)
E = E.subs(v,v0).evalf()
F = F.subs(u,u0)
F = F.subs(v,v0).evalf()
G = G.subs(u,u0)
G = G.subs(v,v0).evalf()

dudv = sy.Matrix(sdu).cross(sy.Matrix(sdv))

u1 = -2
u2 = 2
v1 = -2
v2 = 2
elemArea = sy.lambdify((u, v), dudv.norm(), "numpy") 
area = dblquad(elemArea, v1, v2, lambda u: u1, lambda u: u2)


