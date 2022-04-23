#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:11:00 2021

@author: lucia
"""

import sympy as sy

u, v = sy.symbols('u, v', real = True)
x, y, z, t = sy.symbols('x, y, z, t', real = True)

u0 = 0
v0 = 0

##modificar
sup = [-v+sy.sinh(u), u+sy.cosh(v), u-v**2]

#derivadas:
sdu = [sy.diff(sup[i], u) for i in range(3)] 
sdv = [sy.diff(sup[i], v) for i in range(3)]

n = sy.Matrix(sdu).cross(sy.Matrix(sdv)).normalized()
n = n.subs(u,u0)
n = n.subs(v,v0).evalf()

pto = sy.Matrix(sup).subs(u,u0)
pto = pto.subs(v,v0).evalf() 


term = sy.Matrix(n).dot(sy.Matrix(pto))


#punto_evaluado = sup.subs(u,u0)
#punto_evaluado = sup.subs(v,v0)

#tang = sy.Matrix(n).dot(sy.Matrix(phi))

#tang = tang.subs(u, u0)
#tang = tang.subs(v, v0).evalf()

