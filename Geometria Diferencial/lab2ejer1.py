#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:52:48 2021

@author: lucia
"""

import sympy as sy

u, v = sy.symbols('u, v', real = True)
x, y, z, t = sy.symbols('x, y, z, t', real = True)

u0 = 1
v0 = 0

##modificar
sup = [sy.cos(u+v), sy.sin(u+v), u+v**2]

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

