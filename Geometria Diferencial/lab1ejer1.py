#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:22:45 2021

@author: lucia
"""

import sympy as sy
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


sy.init_printing()
x,y,z,t = sy.symbols('x y z t')

a11 = 1
a12 = 4
a22 = 1
b1 = 1
b2 = 1
c = -2

#1. Transformar la ec. implícita en matriz:
A = sy.Matrix([[a11, sy.Rational(a12, 2)],[sy.Rational(a12, 2), a22]])

P, D = A.diagonalize()
P = P/sy.sqrt(sy.Abs(P.det()))

#autovalores
aut1, aut2 = D[0,0], D[1,1]

#Giro cónica y sustituir en la ecuación
B = sy.Matrix([[ b1, b2]]) * P
V = sy.Matrix([[x, y]])

ec = sum(V*D*V.transpose() + B*V.transpose(),c)

