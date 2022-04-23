#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:25:22 2021

@author: lucia
"""

import sympy as sy
import math
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


sy.init_printing()
x,y,z,t=sy.symbols('x y z t')

#t0 = -math.pi/4
t0 = 2

#modificar:-------
#curva = [sy.sin(t)/(1+t**2), sy.cos(t)]
curva = [sy.ln(t**2+1), t+sy.sin(t)]
#-----------------

vel = [sy.diff(curva[0], t), sy.diff(curva[1], t), 0]
ac = [sy.diff(curva[0], t, 2), sy.diff(curva[1], t, 2), 0]

prod_vect = sy.Matrix(vel).cross(sy.Matrix(ac))

num = prod_vect.subs(t, t0).evalf()
den = sy.Matrix(vel).subs(t, t0).evalf().norm()
ks = num/(den**3)
ks = ks[2]



#ejer3:----------------------------------------------
curva_ev = sy.Matrix(curva).subs(t,t0).evalf()

T = sy.Matrix(vel).subs(t,t0)/sy.Matrix(vel).subs(t,t0).norm()
N = [1,2]
N[0] = -T[1]
N[1] = T[0]

centro = [1,2]
centro[0] = curva[0].subs(t,t0)+1/ks*N[0]
centro[0] = centro[0].evalf()
centro[1] = curva[1].subs(t,t0)+1/ks*N[1]
centro[1] = centro[1].evalf()