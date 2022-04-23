#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:19:14 2021

@author: lucia
"""

import sympy as sy

u, v = sy.symbols('u, v', real = True)
x, y, z, t = sy.symbols('x, y, z, t', real = True)

u0 = -1
v0 = 1


##modificar
sup = [u+sy.ln(u+1), v**2-sy.sin(v), u**2+v]

#derivadas:
sdu = [sy.diff(sup[i], u) for i in range(3)] 
sdv = [sy.diff(sup[i], v) for i in range(3)]

"""
#definición de la curva
curva = [t**2+t+2, 2-t]

#derivada 1 y 2
vel = [sy.diff(curva[0], t), sy.diff(curva[1], t), 0]
ac = [sy.diff(curva[0], t, 2), sy.diff(curva[1], t, 2), 0]


dudv = sy.Matrix(sdu).cross(sy.Matrix(sdv))

n = sy.Matrix(dudv).normalized()

gamma = sy.Matrix(sup).subs(u, curva[0])
gamma = sy.Matrix(sup).subs(v, curva[1])

m = sy.Matrix(n).subs(u, curva[0])
m = sy.Matrix(n).subs(v, curva[1])

num = sy.Matrix(vel).dot(sy.Matrix(ac).cross(sy.Matrix(m)))
dem = (sy.Matrix(vel).norm()**3)

#ver t
t0 = 0
kg = num/dem
kg = kg.subs(t, t0).evalf()

"""

alfa = [-1+2*t*t, 2-t*t]
gamma=sy.Matrix(sup).subs(u,alfa[0])
gamma=sy.Matrix(gamma).subs(v,alfa[1])
gammadt = [sy.diff(gamma[i],t) for i in range(3)]
gammadt2=[sy.diff(gammadt[i],t) for i in range(3)]
n=sy.Matrix(sdu).cross(sy.Matrix(sdv)).normalized()
m=sy.Matrix(n).subs(u,alfa[0])
m=sy.Matrix(m).subs(v,alfa[1])
t0=1
kg=sy.Matrix(gammadt).dot(sy.Matrix(gammadt2).cross(sy.Matrix(m)))/((sy.Matrix(gammadt).norm())**3)
kg=kg.subs(t,t0).evalf()

