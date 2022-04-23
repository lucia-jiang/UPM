#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:17:49 2021

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

#curva--------------
#curva = [sy.sin(t)/(1+t**2), t, sy.cos(t)]
curva = [t, sy.log(t**2+1), t+sy.sin(t)]
#-------------------

d1 = [sy.diff(curva[0], t), sy.diff(curva[1], t), sy.diff(curva[2],t)]
d2 = [sy.diff(curva[0], t, 2), sy.diff(curva[1], t, 2), sy.diff(curva[2],t,2)]
d3 = [sy.diff(curva[0], t, 3), sy.diff(curva[1], t, 3), sy.diff(curva[2],t,3)]

M = [d1, d2, d3]

num = sy.Matrix(M).det().subs(t, t0).evalf()
den = sy.Matrix(d1).cross(sy.Matrix(d2)).subs(t,t0).evalf()
den = sy.Matrix(den).norm()

res = num/den**2
