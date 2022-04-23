#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 23:19:55 2021

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
t0 = 1

#curva--------------
#curva = [sy.sin(t)/(1+t**2), t, sy.cos(t)]
curva = [t**2-sy.sin(t), t, t+sy.cos(t)+1]
#-------------------

d1 = [sy.diff(curva[0], t), sy.diff(curva[1], t), sy.diff(curva[2],t)]
d2 = [sy.diff(curva[0], t, 2), sy.diff(curva[1], t, 2), sy.diff(curva[2],t,2)]
d3 = [sy.diff(curva[0], t, 3), sy.diff(curva[1], t, 3), sy.diff(curva[2],t,3)]


T = sy.Matrix(d1).subs(t,t0)/sy.Matrix(d1).subs(t,t0).norm()

aux = sy.Matrix(d1).cross(sy.Matrix(d2)).subs(t,t0)
B = aux/aux.norm()

N = B.cross(T)

