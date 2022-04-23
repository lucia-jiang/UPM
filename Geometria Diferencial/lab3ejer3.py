#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:12:36 2021

@author: lucia
"""

import sympy as sy
u, v = sy.symbols('u, v', real = True)
x, y, z, t = sy.symbols('x, y, z, t', real = True)

sup = [u-v+u*v, u**3+u*v**2, u*v+v]

#modificar
u0 = 1
v0 = 1

#derivadas:
sdu = [sy.diff(sup[i], u) for i in range(3)] 
sdv = [sy.diff(sup[i], v) for i in range(3)]

sduu = [sy.diff(sup[i], u, u) for i in range(3)]
sduv = [sy.diff(sup[i], u, v) for i in range(3)]
sdvv = [sy.diff(sup[i], v, v) for i in range(3)]

n = sy.Matrix(sdu).cross(sy.Matrix(sdv)).normalized()

#calcular segunda forma e,f,g
e = sy.Matrix(n).dot(sy.Matrix(sduu)).subs(u,u0)
e = e.subs(v,v0).evalf()
f = sy.Matrix(n).dot(sy.Matrix(sduv)).subs(u,u0)
f = f.subs(v,v0).evalf()
g = sy.Matrix(n).dot(sy.Matrix(sdvv)).subs(u,u0)
g = g.subs(v,v0).evalf()


#calcular primera forma E,F,G
E = sy.Matrix(sdu).dot(sy.Matrix(sdu))
F = sy.Matrix(sdu).dot(sy.Matrix(sdv))
G = sy.Matrix(sdv).dot(sy.Matrix(sdv))

E = E.subs(u,u0)
E = E.subs(v,v0).evalf()
F = F.subs(u,u0)
F = F.subs(v,v0).evalf()
G = G.subs(u,u0)
G = G.subs(v,v0).evalf()

#Curvatura media:
H = (e*G+g*E-2*f*F)/(2*(E*G-F**2))
