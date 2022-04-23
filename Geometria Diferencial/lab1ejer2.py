#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:18:20 2021

@author: lucia
"""
import sympy as sy
import math
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


sy.init_printing()
x,y,z,t=sy.symbols('x y z t')

t0 = -2

#modificar:-------
curva = [sy.exp(t) * sy.cos(t), sy.exp(t)]
#-----------------

vel = [sy.diff(curva[0], t), sy.diff(curva[1], t), 0]
ac = [sy.diff(curva[0], t, 2), sy.diff(curva[1], t, 2), 0]

prod_vect = sy.Matrix(vel).cross(sy.Matrix(ac))

num = prod_vect.subs(t, t0).evalf()
den = sy.Matrix(vel).subs(t, t0).evalf().norm()
ks = num/(den**3)
ks = ks[2]



