#-----ficheroCalculoRutaMetroKiev-----#

#-------------------------------------#
"""             IMPORTS             """
#-------------------------------------#

from tkinter import Menu, Canvas, Label, StringVar, Tk, PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
#import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import time
import datetime
import math as mt
import sys, os


def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

#-------------------------------------#
"""  DECLARACION DE PUNTOS REALES   """
#-------------------------------------#


class Punto:
    def __init__(self, x, y, xx, yy):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCoord(self):
        return (self.xx, self.yy)


# Linea 1
p110 = Punto(50.46494012642525, 30.355093416884497, 23, 253)
p111 = Punto(50.456247626897266, 30.365447716885082, 23, 286)
p112 = Punto(50.457766184988856, 30.390651834628162, 23, 318)
p113 = Punto(50.45864903879728, 30.40437299905491, 23, 362)
p114 = Punto(50.45931819257611, 30.41863764016107, 65, 362)
p115 = Punto(50.45422742536485, 30.44862354015915, 104, 362)
p116 = Punto(50.45112945229003, 30.46429282850334, 148, 362)
p117 = Punto(50.44133462518602, 30.48996366960698, 188, 361)
p118 = Punto(50.44326719817879, 30.50463264015914, 229, 361)
p119 = Punto(50.44479360629467, 30.51552534016359, 265, 327)
p120 = Punto(50.44734465226959, 30.52275835795556, 327, 312)
p121 = Punto(50.44306386039469, 30.54715874016503, 378, 312)
p122 = Punto(50.441227639163415, 30.559338500883747, 434, 312)
p123 = Punto(50.445977325247455, 30.576883999054036, 482, 298)
p124 = Punto(50.45186375229452, 30.598156428504502, 520, 268)
p125 = Punto(50.45595732538683, 30.61296942850532, 557, 239)
p126 = Punto(50.459892606100276, 30.630291328508495, 588, 214)
p127 = Punto(50.46465869866755, 30.645565028501128, 617, 192)
# Linea 2
p210 = Punto(50.522730723600276, 30.498868071137395, 327, 49)
p211 = Punto(50.512239420741096, 30.498539045184664, 327, 84)
p212 = Punto(50.50155207222863, 30.498221812086765, 327, 118)
p213 = Punto(50.48610123209044, 30.497850773921535, 327, 152)
p214 = Punto(50.474005048111074, 30.503812969969697, 327, 187)
p215 = Punto(50.46592065758958, 30.515035299940298, 327, 222)
p216 = Punto(50.45926826298118, 30.52441301155909, 327, 256)
p217 = Punto(50.44811860516675, 30.525004351811184, 327, 287)
p218 = Punto(50.44018980321681, 30.518380948884836, 327, 375)
p219 = Punto(50.431287984256116, 30.516868699046643, 327, 424)
p220 = Punto(50.421412208373646, 30.520761017143574, 327, 474)
p221 = Punto(50.41397905914938, 30.52488896654911, 327, 520)
p222 = Punto(50.40478945648299, 30.51687132805836, 327, 569)
p223 = Punto(50.397387739824964, 30.508256063532823, 289, 604)
p224 = Punto(50.393826892524935, 30.489814657976208, 220, 604)
p225 = Punto(50.382434238091456, 30.477578657948037, 165, 604)
p226 = Punto(50.37657465912842, 30.46883377069136, 117, 604)
p227 = Punto(50.3671086990247, 30.454137016823314, 66, 604)
# Linea 3
p310 = Punto(50.47676197914337, 30.432779769613134, 155, 153)
p311 = Punto(50.47342141713646, 30.44911559011381, 187, 204)
p312 = Punto(50.461145571706496, 30.483634410707804, 216, 249)
p314 = Punto(50.445808752256475, 30.515154999053287, 253, 306)
p315 = Punto(50.43972032516655, 30.51948465794992, 352, 375)
p316 = Punto(50.43696930640579, 30.531805657953512, 376, 389)
p317 = Punto(50.427273024996545, 30.539400010713162, 396, 417)
p318 = Punto(50.41703403394279, 30.54731766961379, 418, 444)
p319 = Punto(50.40182175204946, 30.56048665794956, 439, 475)
p321 = Punto(50.39425906958125, 30.60486439904998, 461, 506)
p322 = Punto(50.3952481794903, 30.61623234016095, 483, 536)
p323 = Punto(50.39786352459437, 30.6347450990561, 501, 561)
p324 = Punto(50.400675638256914, 30.65208815794845, 519, 585)
p325 = Punto(50.402949851013496, 30.66690638640424, 549, 604)
p326 = Punto(50.40339502974507, 30.68435741688402, 578, 604)
p327 = Punto(50.40947275208938, 30.696202999057906, 607, 604)


#-------------------------------------#
"""       TRADUCCION DE PUNTOS      """
#-------------------------------------#

def getP(punto):
    # -------linea 1---------
    if punto == '110':
        return p110
    elif punto == '111':
        return p111
    elif punto == '112':
        return p112
    elif punto == '113':
        return p113
    elif punto == '114':
        return p114
    elif punto == '115':
        return p115
    elif punto == '116':
        return p116
    elif punto == '117':
        return p117
    elif punto == '118':
        return p118
    elif punto == '119':
        return p119
    elif punto == '120':
        return p120
    elif punto == '121':
        return p121
    elif punto == '122':
        return p122
    elif punto == '123':
        return p123
    elif punto == '124':
        return p124
    elif punto == '125':
        return p125
    elif punto == '126':
        return p126
    elif punto == '127':
        return p127
    # --------linea 2--------
    elif punto == '210':
        return p210
    elif punto == '211':
        return p211
    elif punto == '212':
        return p212
    elif punto == '213':
        return p213
    elif punto == '214':
        return p214
    elif punto == '215':
        return p215
    elif punto == '216':
        return p216
    elif punto == '217':
        return p217
    elif punto == '218':
        return p218
    elif punto == '219':
        return p219
    elif punto == '220':
        return p220
    elif punto == '221':
        return p221
    elif punto == '222':
        return p222
    elif punto == '223':
        return p223
    elif punto == '224':
        return p224
    elif punto == '225':
        return p225
    elif punto == '226':
        return p226
    elif punto == '227':
        return p227
    # --------linea 3--------
    elif punto == '310':
        return p310
    elif punto == '311':
        return p311
    elif punto == '312':
        return p312
    elif punto == '314':
        return p314
    elif punto == '315':
        return p315
    elif punto == '316':
        return p316
    elif punto == '317':
        return p317
    elif punto == '318':
        return p318
    elif punto == '319':
        return p319
    elif punto == '321':
        return p321
    elif punto == '322':
        return p322
    elif punto == '323':
        return p323
    elif punto == '324':
        return p324
    elif punto == '325':
        return p325
    elif punto == '326':
        return p326
    elif punto == '327':
        return p327


#-------------------------------------#
""" FUNCIONES AUX PARA CALCULO G, H """
#-------------------------------------#

def distanciaH(lat1, lon1, lat2, lon2):
    rad = mt.pi/180
    dlat = lat2-lat1
    dlon = lon2-lon1
    R = 6372.795477598
    a = (mt.sin(rad*dlat/2))**2 + mt.cos(rad*lat1) * \
        mt.cos(rad*lat2)*(mt.sin(rad*dlon/2))**2
    distancia = 2*R*mt.asin(mt.sqrt(a))
    return (distancia/37.5)*60


def transbordos(hora, dia, parada):
    if(dia == 'SÁBADO' or dia == 'DOMINGO'):
        if(parada == '119'):
            res = 3.5
        elif(parada == '314'):
            res = 6
        elif(parada == '120'):
            res = 3.5
        elif(parada == '217'):
            res = 4.5
        elif(parada == '218'):
            res = 4.5
        else:
            res = 6
    else:
        if((hora >= 7 and hora < 10) or (hora >= 17 and hora < 20)):
            if(parada == '119'):
                res = 2
            elif(parada == '314'):
                res = 2.5
            elif(parada == '120'):
                res = 2
            elif(parada == '217'):
                res = 2.25
            elif(parada == '218'):
                res = 2.25
            else:
                res = 2.5
        else:
            if(parada == '119'):
                res = 3.5
            elif(parada == '314'):
                res = 5
            elif(parada == '120'):
                res = 3.5
            elif(parada == '217'):
                res = 5
            elif(parada == '218'):
                res = 5
            else:
                res = 5
    return res + 1


#-------------------------------------#
"""           ALGORITMO A*          """
#-------------------------------------#

class MapaKiev:

    tablaG = {}  # tabla con los valores reales entre cada parada y sus adyacentes
    tablaH = {}  # tabla con los valores aereos desde cada parada a la parada "destino"

    hayTrasbordo = False
    tiempoTotal = 0
    tiempoCaminar=0
    tiempoTransporte=0
    tiempoTransbordo=0

    abiertos = {}  # diccionario que almacena las paradas en estado "abierto" y el valor acutal de su f
    cerrados = set()  # set(conjunto de elementos) que almacena las paradas en estado "cerrado"
    # diccionario que almacena los caminos que sigue el arbol de nodos(paradas) durante el algoritmo
    arbolSol = {}

    def buildG(self, dia, hora):
        self.tablaG = {
            '110': [('111', 3)],
            '111': [('110', 3), ('112', 3)],
            '112': [('111', 3), ('113', 2)],
            '113': [('112', 2), ('114', 2)],
            '114': [('113', 2), ('115', 4)],
            '115': [('114', 4), ('116', 2)],
            '116': [('115', 2), ('117', 4)],
            '117': [('116', 4), ('118', 2)],
            '118': [('117', 2), ('119', 1)],
            '119': [('118', 1), ('120', 1), ('314', transbordos(hora, dia, '314'))],
            '120': [('119', 1), ('121', 3), ('217', transbordos(hora, dia, '217'))],
            '121': [('120', 3), ('122', 2)],
            '122': [('121', 2), ('123', 2)],
            '123': [('122', 2), ('124', 3)],
            '124': [('123', 3), ('125', 2)],
            '125': [('124', 2), ('126', 2)],
            '126': [('125', 2), ('127', 2)],
            '127': [('126', 2)],

            '210': [('211', 2)],
            '211': [('210', 2), ('212', 2)],
            '212': [('211', 2), ('213', 3)],
            '213': [('212', 3), ('214', 2)],
            '214': [('213', 2), ('215', 2)],
            '215': [('214', 2), ('216', 2)],
            '216': [('215', 2), ('217', 2)],
            '217': [('216', 2), ('218', 2), ('120', transbordos(hora, dia, '120'))],
            '218': [('217', 2), ('219', 2), ('315', transbordos(hora, dia, '315'))],
            '219': [('218', 2), ('220', 2)],
            '220': [('219', 2), ('221', 2)],
            '221': [('220', 2), ('222', 2)],
            '222': [('221', 2), ('223', 2)],
            '223': [('222', 2), ('224', 3)],
            '224': [('223', 3), ('225', 3)],
            '225': [('224', 3), ('226', 2)],
            '226': [('225', 2), ('227', 2)],
            '227': [('226', 2)],

            '310': [('311', 3)],
            '311': [('310', 3), ('312', 5)],
            '312': [('311', 5), ('314', 5)],
            '314': [('312', 5), ('315', 1), ('119', transbordos(hora, dia, '119'))],
            '315': [('314', 1), ('316', 2), ('218', transbordos(hora, dia, '218'))],
            '316': [('315', 2), ('317', 2)],
            '317': [('316', 2), ('318', 2)],
            '318': [('317', 2), ('319', 3)],
            '319': [('318', 3), ('321', 6)],
            '321': [('319', 6), ('322', 1)],
            '322': [('321', 1), ('323', 2)],
            '323': [('322', 2), ('324', 2)],
            '324': [('323', 2), ('325', 2)],
            '325': [('324', 2), ('326', 2)],
            '326': [('325', 2), ('327', 2)],
            '327': [('326', 2)],
        }

    def buildH(self, punto):
        parada = getP(punto)
        self.tablaH = {
            '110': distanciaH(parada.getX(), parada.getY(), p110.getX(), p110.getY()),
            '111': distanciaH(parada.getX(), parada.getY(), p111.getX(), p111.getY()),
            '112': distanciaH(parada.getX(), parada.getY(), p112.getX(), p112.getY()),
            '113': distanciaH(parada.getX(), parada.getY(), p113.getX(), p113.getY()),
            '114': distanciaH(parada.getX(), parada.getY(), p114.getX(), p114.getY()),
            '115': distanciaH(parada.getX(), parada.getY(), p115.getX(), p115.getY()),
            '116': distanciaH(parada.getX(), parada.getY(), p116.getX(), p116.getY()),
            '117': distanciaH(parada.getX(), parada.getY(), p117.getX(), p117.getY()),
            '118': distanciaH(parada.getX(), parada.getY(), p118.getX(), p118.getY()),
            '119': distanciaH(parada.getX(), parada.getY(), p119.getX(), p119.getY()),
            '120': distanciaH(parada.getX(), parada.getY(), p120.getX(), p120.getY()),
            '121': distanciaH(parada.getX(), parada.getY(), p121.getX(), p121.getY()),
            '122': distanciaH(parada.getX(), parada.getY(), p122.getX(), p122.getY()),
            '123': distanciaH(parada.getX(), parada.getY(), p123.getX(), p123.getY()),
            '124': distanciaH(parada.getX(), parada.getY(), p124.getX(), p124.getY()),
            '125': distanciaH(parada.getX(), parada.getY(), p125.getX(), p125.getY()),
            '126': distanciaH(parada.getX(), parada.getY(), p126.getX(), p126.getY()),
            '127': distanciaH(parada.getX(), parada.getY(), p127.getX(), p127.getY()),

            '210':  distanciaH(parada.getX(), parada.getY(), p210.getX(), p210.getY()),
            '211':  distanciaH(parada.getX(), parada.getY(), p211.getX(), p211.getY()),
            '212':  distanciaH(parada.getX(), parada.getY(), p212.getX(), p212.getY()),
            '213':  distanciaH(parada.getX(), parada.getY(), p213.getX(), p213.getY()),
            '214':  distanciaH(parada.getX(), parada.getY(), p214.getX(), p214.getY()),
            '215':  distanciaH(parada.getX(), parada.getY(), p215.getX(), p215.getY()),
            '216':  distanciaH(parada.getX(), parada.getY(), p216.getX(), p216.getY()),
            '217':  distanciaH(parada.getX(), parada.getY(), p217.getX(), p217.getY()),
            '218':  distanciaH(parada.getX(), parada.getY(), p218.getX(), p218.getY()),
            '219':  distanciaH(parada.getX(), parada.getY(), p219.getX(), p219.getY()),
            '220':  distanciaH(parada.getX(), parada.getY(), p220.getX(), p220.getY()),
            '221':  distanciaH(parada.getX(), parada.getY(), p221.getX(), p221.getY()),
            '222':  distanciaH(parada.getX(), parada.getY(), p222.getX(), p222.getY()),
            '223':  distanciaH(parada.getX(), parada.getY(), p223.getX(), p223.getY()),
            '224':  distanciaH(parada.getX(), parada.getY(), p224.getX(), p224.getY()),
            '225':  distanciaH(parada.getX(), parada.getY(), p225.getX(), p225.getY()),
            '226':  distanciaH(parada.getX(), parada.getY(), p226.getX(), p226.getY()),
            '227':  distanciaH(parada.getX(), parada.getY(), p227.getX(), p227.getY()),

            '310':  distanciaH(parada.getX(), parada.getY(), p310.getX(), p310.getY()),
            '311':  distanciaH(parada.getX(), parada.getY(), p311.getX(), p311.getY()),
            '312':  distanciaH(parada.getX(), parada.getY(), p312.getX(), p312.getY()),
            '314':  distanciaH(parada.getX(), parada.getY(), p314.getX(), p314.getY()),
            '315':  distanciaH(parada.getX(), parada.getY(), p315.getX(), p315.getY()),
            '316':  distanciaH(parada.getX(), parada.getY(), p316.getX(), p316.getY()),
            '317':  distanciaH(parada.getX(), parada.getY(), p317.getX(), p317.getY()),
            '318':  distanciaH(parada.getX(), parada.getY(), p318.getX(), p318.getY()),
            '319':  distanciaH(parada.getX(), parada.getY(), p319.getX(), p319.getY()),
            '321':  distanciaH(parada.getX(), parada.getY(), p321.getX(), p321.getY()),
            '322':  distanciaH(parada.getX(), parada.getY(), p322.getX(), p322.getY()),
            '323':  distanciaH(parada.getX(), parada.getY(), p323.getX(), p323.getY()),
            '324':  distanciaH(parada.getX(), parada.getY(), p324.getX(), p324.getY()),
            '325':  distanciaH(parada.getX(), parada.getY(), p325.getX(), p325.getY()),
            '326':  distanciaH(parada.getX(), parada.getY(), p326.getX(), p326.getY()),
            '327':  distanciaH(parada.getX(), parada.getY(), p327.getX(), p327.getY()),
        }

    def getHijos(self, n):  # funcion que devuelve todos los pares (parada,valor) adyacentes a la parada n
        return self.tablaG[n]

    def h(self, n):  # funcion que devuelve el valor h de la parada n
        return self.tablaH[n]

    def getTiempo(self):
        return self.tiempoTotal

    def getHayTrasbordo(self):
        return self.hayTrasbordo
    
    def getTiempoCaminar(self):
        return self.tiempoCaminar
    
    def getTiempoTransporte(self):
        return self.tiempoTransporte
    
    def getTiempoTrasbordo(self):
        return self.tiempoTransbordo

    def iniLists(self, origen):  # funcion que inicializa los set y el arbol en funcion de "origen"
        self.abiertos.clear()
        self.abiertos[origen] = self.h(origen)
        self.cerrados.clear()
        self.arbolSol.clear()
        self.tiempoTotal = 0
        self.tiempoCaminar=0
        self.tiempoTransporte=0
        self.tiempoTransbordo=0
        self.hayTrasbordo = False
        # condicion de parada para generar la lista a partir del arbol cuando termine el algoritmo
        self.arbolSol[origen] = '-1'

    def getMenorF(self):  # funcion que obtiene los elementos de la lista de abiertos y devuelve el que contenga un menor valor de f = g+h
        mi_Node = None
        for n in self.abiertos.keys():
            if mi_Node == None or self.abiertos.get(n) < self.abiertos.get(mi_Node):
                mi_Node = n
        return mi_Node

    def analisisHijos(self, mi_Node):  # funcion que analiza los hijos de un nodo
        for (n, valorGPrima) in self.getHijos(mi_Node):  # por cada hijo de "mi_Node"
            if n not in self.cerrados:  # si no esta en la lista de cerrados se analiza
                # obtenemos el nuevo valor g de ese nodo
                newG = self.abiertos.get(
                    mi_Node)-self.h(mi_Node) + valorGPrima + self.h(n)
                if n in self.abiertos.keys():  # si el nodo estaba ya en "abiertos" se comprueba su valor anterior y se actualiza en caso de ser necesario
                    if self.abiertos.get(n) > newG:
                        self.abiertos[n] = newG
                        # se añade la relacion padre hijo al arbol
                        self.arbolSol[n] = mi_Node
                else:  # el nodo no estaba en abiertos: se añade
                    self.abiertos[n] = newG
                    # se añade la relacion padre hijo al arbol
                    self.arbolSol[n] = mi_Node

    # funcion para crear la lista solucion: comienza mirando el valor del nodo=destino y lo añade a la lista, sustituye destino por el nuevo valor y repite hasta que el valor sea -1
    def analisisArbolSol(self, mi_Node, dia, hora):
        ruta = []
        i = 0
        self.tiempoTotal = self.abiertos.get(mi_Node) - self.h(mi_Node)
        self.tiempoTransporte = self.tiempoTotal
        while self.arbolSol.get(mi_Node) != '-1':
            n = self.arbolSol.get(mi_Node)
            if ((mi_Node == '119' or mi_Node == '314') and (n == '119' or n == '314')) or ((mi_Node == '217' or mi_Node == '120') and (n == '217' or n == '120')) or ((mi_Node == '218' or mi_Node == '315') and (n == '218' or n == '315')):
                self.hayTrasbordo = True
                self.tiempoCaminar+=1
                self.tiempoTransporte-=transbordos(hora,dia,mi_Node)
                self.tiempoTransbordo+=transbordos(hora,dia,mi_Node)-1
            ruta.insert(i, mi_Node)
            mi_Node = self.arbolSol.get(mi_Node)
            i += 1
        ruta.insert(i, mi_Node)
        if i>1:
            if ruta[0] == '119' and ruta[1] == '314':
                self.tiempoTotal -= transbordos(hora, dia, '119') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
            elif ruta[0] == '314' and ruta[1] == '119':
                self.tiempoTotal -= transbordos(hora, dia, '314') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
            elif ruta[0] == '120' and ruta[1] == '217':
                self.tiempoTotal -= transbordos(hora, dia, '120') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
            elif ruta[0] == '217' and ruta[1] == '120':
                self.tiempoTotal -= transbordos(hora, dia, '217') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
            elif ruta[0] == '218' and ruta[1] == '315':
                self.tiempoTotal -= transbordos(hora, dia, '218') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
            elif ruta[0] == '315' and ruta[1] == '218':
                self.tiempoTotal -= transbordos(hora, dia, '315') - 1
                self.tiempoTransbordo=0
                self.hayTrasbordo = False
        ruta.reverse()  # se invierte la lista para devolver el orden correcto
        return ruta

    # funcion principal que calcula la ruta optima entre "origen" y "destino"
    def getRuta(self, origen, destino, dia, hora):
        self.buildH(origen)
        self.buildG(dia, int(hora))
        self.iniLists(origen)  # se inicializan las listas
        while len(self.abiertos) > 0:  # se realiza un bucle mientras tenga paradas que analizar
            mi_Node = self.getMenorF()  # se obtiene la  nueva parada a analizar
            print("-----------------------------")
            print(self.abiertos)
            print(self.cerrados)
            if(mi_Node == destino):  # se comprueba si se ha encontrado la parada objetivo: en caso positivo se genera el camino solucion
                return self.analisisArbolSol(mi_Node, dia, int(hora))
            # si no se ha encontrado:
            self.analisisHijos(mi_Node)  # se analizan los hijos de la parada
            self.cerrados.add(mi_Node)  # se introduce la parada en cerrados
            self.abiertos.pop(mi_Node)  # se retira la parada de abiertos
        return None  # en nuestro caso todas las paradas estan conectadas, por lo que nunca se llegaría a esta solucion


#-------------------------------------#
"""         INTERFAZ INICIAL        """
#-------------------------------------#

raiz = Tk()
raiz.title("Metro de Kiev")
raiz.resizable(True, True)
raiz.iconbitmap(resolver_ruta("logo.ico"))

#------------menú------------:
menubar = Menu(raiz)

raiz.config(menu=menubar)
menubar.config(cursor="hand2")
filemenu = Menu(menubar)
editmenu = Menu(menubar)
infomenu = Menu(menubar)

def nuevo():
    for n in range(0, len(lineas)):
        canvas.delete(lineas[n])
    cuadro1.set('')
    cuadro2.set('')

    A = time.ctime()
    A = A.split()
    A = A[3]

    cuadro3.delete(0, "end")
    cuadro3.insert(hora, A[0]+A[1])
    cuadro4.delete(0, "end")
    cuadro4.insert(minutos, A[3]+A[4])
    labelTop.configure(text="") 

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Cerrar", command = raiz.quit)
editmenu = Menu(menubar, tearoff=0)

s = ttk.Style()
#----windows------
def tema(n):
    if(n==0):
        style.set_theme('adapta')
    elif(n==1):
        style.set_theme('aquativo')
    elif(n==2):
        style.set_theme('arc')
    elif(n==3):
        style.set_theme('black')
    elif(n==4):
        style.set_theme('blue')
    elif(n==5):
        style.set_theme('breeze')
    elif(n==6):
        style.set_theme('clearlooks')
    elif(n==7):
        style.set_theme('elegance')
    elif(n==8):
        style.set_theme('equilux')
    elif(n==9):
        style.set_theme('itft1')
    elif(n==10):
        style.set_theme('keramik')
    elif(n==11):
        style.set_theme('kroc')
    elif(n==12):
        style.set_theme('plastik')
    elif(n==13):
        style.set_theme('radiance')
    elif(n==14):
        style.set_theme('scidsand')
    elif(n==15):
        style.set_theme('scidgrey')
    elif(n==16):
        style.set_theme('scidblue')
    elif(n==17):
        style.set_theme('scidgreen')
    elif(n==18):
        style.set_theme('scidmint')
    elif(n==19):
        style.set_theme('scidpink')
    elif(n==20):
        style.set_theme('scidpurple')
    elif(n==21):
        style.set_theme('smog')
    elif(n==22):
        style.set_theme('winxpblue')
    elif(n==23):
        style.set_theme('yaru')
    elif(n==24):
        style.set_theme('default')
        
submenuTemas = tk.Menu(editmenu)
submenuTemas.add_radiobutton(label="Adapta", command=lambda: tema(0))
submenuTemas.add_radiobutton(label="Aquativo", command=lambda: tema(1))
submenuTemas.add_radiobutton(label="Arc", command=lambda: tema(2))
submenuTemas.add_radiobutton(label="Black", command=lambda: tema(3))
submenuTemas.add_radiobutton(label="Blue", command=lambda: tema(4))
submenuTemas.add_radiobutton(label="Breeze", command=lambda: tema(5))
submenuTemas.add_radiobutton(label="Clearlooks", command=lambda: tema(6))
submenuTemas.add_radiobutton(label="Elegance", command=lambda: tema(7))
submenuTemas.add_radiobutton(label="Equilux", command=lambda: tema(8))
submenuTemas.add_command(label="ITFT1", command=lambda: tema(9))
submenuTemas.add_radiobutton(label="Keramik", command=lambda: tema(10))
submenuTemas.add_radiobutton(label="Kroc", command=lambda: tema(11))
submenuTemas.add_radiobutton(label="Plastik", command=lambda: tema(12))
submenuTemas.add_radiobutton(label="Radiance", command=lambda: tema(13))
submenuScid = Menu(submenuTemas)
submenuTemas.add_cascade(label="Scid Themes",menu=submenuScid)
submenuScid.add_radiobutton(label="Sand", command=lambda: tema(14))
submenuScid.add_radiobutton(label="Grey", command=lambda: tema(15))
submenuScid.add_radiobutton(label="Blue", command=lambda: tema(16))
submenuScid.add_radiobutton(label="Green", command=lambda: tema(17))
submenuScid.add_radiobutton(label="Mint", command=lambda: tema(18))
submenuScid.add_radiobutton(label="Pink", command=lambda: tema(19))
submenuScid.add_radiobutton(label="Purple", command=lambda: tema(20))
submenuTemas.add_radiobutton(label="Smog", command=lambda: tema(21))
submenuTemas.add_radiobutton(label="WinXPblue", command=lambda: tema(22))
submenuTemas.add_radiobutton(label="Yaru", command=lambda: tema(23))
submenuTemas.add_radiobutton(label="Default", command=lambda: tema(24))

def ayuda():
    showinfo(title="Ayuda", message="Calculadora de la ruta más corta entre estaciones de Kiev, utilizando el algoritmo A*")
def acerca():
    showinfo(title="Acerca", message="Realizado por: \n Gonzalo Aguado Corbelle \n Lucía Jiang \n Jaime Jiménez Jiménez \n David Pantoja Mínguez \n Juan Paños Fernández \n Gonzalo Poza González \n")

infomenu = Menu(menubar, tearoff=0)

infomenu.add_command(label="Ayuda", command = ayuda)
infomenu.add_separator()
infomenu.add_command(label="Acerca de", command = acerca)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Apariencia", menu=submenuTemas)
menubar.add_cascade(label="Información", menu=infomenu)

# ---------------temática-----------
style = ThemedStyle(raiz)

# ---------------marco--------
miframe = ttk.Frame()
miframe.pack(fill="both", expand="True")
miimagen = PhotoImage(file=resolver_ruta("plano.png"))
miframe.config(width="950", height="650")
#miframe.config(cursor="hand2")

# ---------------var----------
opciones = ["", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
diaSemana = StringVar()
x = datetime.datetime.today().weekday()

if x == 0:
    diaSemana.set("LUNES")
elif x == 1:
    diaSemana.set("MARTES")
elif x == 2:
    diaSemana.set("MIÉRCOLES")
elif x == 3:
    diaSemana.set("JUEVES")
elif x == 4:
    diaSemana.set("VIERNES")
elif x == 5:
    diaSemana.set("SÁBADO")
elif x == 6:
    diaSemana.set("DOMINGO")
#if x < 0 or x > 6:
 #   print("ERROR")
origen = 2
destino = 1
A = time.ctime()
A = A.split()
A = A[3]
dia = 0
hora = 3
minutos = 0
errorOCreada = -1
errorDCreada = -2
errorHCreada = -3
errorO = Label(raiz, text="PARADA ORIGEN NO EXISTENTE",
               fg="red", font=("Arial", 15))
errorD = Label(raiz, text="PARADA DESTINO NO EXISTENTE",
               fg="red", font=("Arial", 15))
errorH = Label(raiz, text="ERROR EN LA HORA INTRODUCIDA",
               fg="red", font=("Arial", 15))
# ---------------tabla--------

#Lista de paradas
listaParadas = ('L1 -110- Akademmistechko', 
                'L1 -111- Zhytomyrska', 
                'L1 -112 -Sviatoshyn',
                'L1 -113- Nyvky', 
                'L1 -114- Beresteiska', 
                'L1 -115- Shuliavska', 
                'L1 -116- Politekhnichnyi Instytut',
                'L1 -117- Vokzalna', 
                'L1 -118- Universytet', 
                'L1 -119- Teatralna', 
                'L1 -120- Jreshchatyk',
                'L1 -121- Arsenalna', 
                'L1 -122- Dnipro', 
                'L1 -123- Hidropark', 
                'L1 -124- Livoberezhna', 
                'L1 -125- Darnytsia',
                'L1 -126 Chernihivska', 
                'L1 -127  Lisova',
                'L2 -210- Heroiv Dnipra',
                'L2 -211- Minska',
                'L2 -212- Obolon',
                'L2 -213- Pochaina',
                'L2 -214- Tarasa Shevchenka',
                'L2 -215- Kontraktova Ploshcha',
                'L2 -216- Poshtova Ploshcha',
                'L2 -217- Maidan Nezalezhnosti',
                'L2 -218- Ploshcha Lva Tolstoho',
                'L2 -219- Olimpiiska',
                'L2 -220- Palats "Ukrayina"',
                'L2 -221- Lybidska',
                'L2 -222- Demiivska',
                'L2 -223- Holosiivska',
                'L2 -224- Vasylkivska',
                'L2 -225- Vystavkovyi Tsentr',
                'L2 -226- Ipodrom',
                'L2 -227- Teremky',

                'L3 -310- Syrets',
                'L3 -311- Dorogozhychi',
                'L3 -312- Lukianivska',
                'L3 -314- Zoloti Vorota',
                'L3 -315- Palats Sportu',
                'L3 -316- Klovska',
                'L3 -317- Pecherska',
                'L3 -318- Druzhby Narodiv',
                'L3 -319- Vydubychi',
                'L3 -321- Slavutych',
                'L3 -322- Osokorky',
                'L3 -323- Pozniaky',
                'L3 -324- Jarkivska',
                'L3 -325- Vyrlytsia',
                'L3 -326- Boryspilska',
                'L3 -327- Chervony Jutir')

milabel1 = ttk.Label(miframe, text="Origen:", font=("Arial", 10)).grid(row=0, column=0, sticky="e")
cuadro1 = ttk.Combobox(miframe, textvariable=origen)
cuadro1['values'] = listaParadas
cuadro1.grid(row=0, column=1)
cuadro1.config(cursor="hand2")

milabel2 = ttk.Label(miframe, text="Destino:", font=("Arial", 10)).grid(row=0, column=2, sticky="e")
cuadro2 = ttk.Combobox(miframe, textvariable=destino)
cuadro2['values'] = listaParadas
cuadro2.grid(row=0, column=3)
cuadro2.config(cursor="hand2")

milabel3 = ttk.Label(miframe, text="Hora:", font=("Arial", 10))
cuadro3 = ttk.Spinbox(miframe, textvariable=hora, from_=0, to=23, wrap=True)
cuadro3.insert(hora, A[0]+A[1])
milabel3.grid(row=1, column=0, sticky="e")
cuadro3.grid(row=1, column=1)
cuadro3.config(cursor="hand2")

milabel4 = ttk.Label(miframe, text=":", font=("Arial", 10))
cuadro4 = ttk.Spinbox(miframe, textvariable=minutos, from_=0, to=59, wrap=True)
cuadro4.insert(minutos, A[3]+A[4])
milabel4.grid(row=1, column=2)
cuadro4.grid(row=1, column=3)
cuadro4.config(cursor="hand2")

milabel6 = ttk.Label(miframe, text="Dia:", font=("Arial", 10))
milabel6.grid(row=2, column=0, sticky="e")

canvas = Canvas(miframe,width=653, height=653)
canvas.grid(row=3,column=4)
canvas.create_image(0, 0, image=miimagen, anchor='nw')

opcion = ttk.OptionMenu(miframe, diaSemana, *opciones)
opcion.config(width=13)
opcion.grid(row=2, column=1)
opcion.config(cursor="hand2")

labelTop = ttk.Label(miframe, text="")
labelTop.grid(row=3, column=1, columnspan=2)

aviso = Label(miframe, text="", fg="red", font=("Arial", 15))
aviso.grid(row=4, column=1, columnspan=2)
    
#-------------------------------------#
"""  GESTION ERRORES DATOS INTERFAZ """
#-------------------------------------#

def getErrores(o, d, h, m):
    res = 0
    global origen
    global destino
    global errorO
    global errorD
    global errorH
    global errorOCreada
    global errorDCreada
    global errorHCreada
    if errorOCreada == 0:
        errorO.destroy()
    if errorDCreada == 0:
        errorD.destroy()
    if errorHCreada == 0:
        errorH.destroy()
    origen = int(o)
    destino = int(d)
    hora = int(h)
    minutos = int(m)
    if (origen < 110 or (origen > 127 and origen < 210) or origen == 313 or origen == 320 or (origen > 227 and origen < 310)):
        errorO = Label(raiz, text="PARADA ORIGEN NO EXISTENTE", fg="red", font=("Arial", 15))
        res = 1
        errorO.pack()
        errorOCreada = 0
    if (destino < 110 or (destino > 127 and destino < 210) or destino == 313 or destino == 320 or (destino > 227 and destino < 310)):
        errorD = Label(raiz, text="PARADA DESTINO NO EXISTENTE", fg="red", font=("Arial", 15))
        errorD.pack()
        errorDCreada = 0
        res = 1
    if (hora < 0 or hora > 23 or minutos < 0 or minutos > 59):
        errorH = Label(raiz, text="ERROR EN LA HORA INTRODUCIDA", fg="red", font=("Arial", 15))
        errorH.pack()
        errorHCreada = 0
        res = 1

    if ((origen == 314 and destino == 119) or (destino == 314 and origen == 119) or (origen == 217 and destino == 120) or (origen == 120 and destino == 217) or (origen == 218 and destino == 315) or (origen == 315 and destino == 218)):
        errorP = Label(raiz, text="Es la misma parada", fg = "red", font=("Arial", 15)).pack()
        res = 1
    return res

def errorHoraSalida(o, d, hora, minutos, mp):
    #0 si no hay error, 1 si empieza en la linea 1, 2 linea2 y 3 linea3
    global errorHS
  

    if(o<128 and ((hora==0 and minutos>18) or hora in range(1,5) or (hora==5 and minutos<27))):
        aviso.configure(text="Aviso: la línea 1 no abre hasta las 5:27")
        return 1
    if(o<228 and ((hora in range(1,5) or (hora==5 and minutos<22) or (hora==0 and minutos>16)))):
        aviso.configure(text="Aviso: la línea 2 no abre hasta las 5:22")
        return 2
    if(o<328 and ((hora in range (1,5) or (hora==5 and minutos<20) or (hora==0 and minutos>17)))):
        aviso.configure(text="Aviso: la línea 3 no abre hasta las 5:20")
        return 3
    return 0

def errorHoraLlegada(o,d,hora,minutos,mp):
    horaLlegada = hora
    minutoLlegada = minutos+mp.getTiempo()
    if(minutoLlegada>60):
        minutoLlegada-=60
        horaLlegada +=1

    if(d<128 and (horaLlegada in range(1,5) or (horaLlegada==0 and minutoLlegada>18) or (horaLlegada==5 and minutoLlegada<27))):
        aviso.configure(text="Aviso: la línea 1 cierra a las 00:18, antes de \nque llegue al destino", fg="red", font=("Arial", 15))
        
    elif(d<228 and (horaLlegada in range(1,5) or (horaLlegada==0 and minutoLlegada>16) or (horaLlegada==5 and minutoLlegada<22))):
        aviso.configure(text="Aviso: la línea 2 cierra a las 00:16, antes de \nque llegue al destino", fg="red", font=("Arial", 15))


    elif(d<328 and (horaLlegada in range(1,5) or (horaLlegada==0 and minutoLlegada>17) or (horaLlegada==5 and minutoLlegada<20))):
        aviso.configure(text="Aviso: la línea 3 cierra a las 00:17, antes de \nque llegue al destino", fg="red", font=("Arial", 15))



#-------------------------------------#
"""        INTERFAZ SOLUCION        """
#-------------------------------------#

lineas = []

def paradas2num(n): #obtener código de las paradas
    res = 0
    if(n>=0 and n<18): #Línea 1
        res = n+110 
    elif(n>=18 and n<36): #Línea 2
        res = n+192
    elif(n>=36 and n<39): #310-312
        res = n+274
    elif(n>=39 and n<45): #314-319
        res = n+275
    else: #Línea 3: 321-327
        res = n+276
    return str(res)

def num2paradas(n):
    n = int(n)
    res=""
    if(n>=110 and n<128):
        res = listaParadas[n-110]
    elif(n>=210 and n<228):
        res = listaParadas[n-192]
    elif(n>=310 and n<313):
        res = listaParadas[n-274]
    elif(n>=314 and n<320):
        res = listaParadas[n-275]
    else:
        res = listaParadas[n-276]
    return res

def codigoInicio(o, d, h, m):
    o = paradas2num(o)
    d = paradas2num(d)
    aviso.configure(text="")    
    
    if getErrores(o, d, h, m) == 1:
        return
    
    mp = MapaKiev()
    ruta = mp.getRuta(o, d, diaSemana, h)


    for n in range(0, len(lineas)):
        canvas.delete(lineas[n])
        
        
    for i in range(0, len(ruta)-1):
        if ((ruta[i] == '314' and ruta[i+1] == '315') or (ruta[i] == '315' and ruta[i+1] == '314')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (296, 375), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        elif((ruta[i] == '122' and ruta[i+1] == '123') or (ruta[i] == '123' and ruta[i+1] == '122')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (462, 312), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        elif((ruta[i] == '118' and ruta[i+1] == '119') or (ruta[i] == '119' and ruta[i+1] == '118')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (244, 360), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        elif((ruta[i] == '119' and ruta[i+1] == '120') or (ruta[i] == '120' and ruta[i+1] == '119')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (273, 312), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        elif((ruta[i] == '315' and ruta[i+1] == '316') or (ruta[i] == '316' and ruta[i+1] == '315')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (365, 377), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        elif((ruta[i] == '324' and ruta[i+1] == '325') or (ruta[i] == '325' and ruta[i+1] == '324')):
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), (532, 601), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

        else:
            lineas.insert(i, canvas.create_line(getP(ruta[i]).getCoord(), getP(
                ruta[i+1]).getCoord(), fill='black', arrow='last', width=3, arrowshape=(12, 16, 6)))

    
    
    horaComienzo = (5.27, 5.22, 5.20)
    horaCierre = (0.18, 0.16, 0.17) 
    
    salida = errorHoraSalida(int(o), int(d), int(h), int(m), mp) #llama a la función, que comprueba que esté abierto el metro a la hora de calcular el trayecto,
                                                                #y que no cierre antes de que lleguemos
    print(salida)
    if(salida==0):
        errorHoraLlegada(int(o), int(d), int(h), int(m), mp)
    
    
    rutaSol="La ruta óptima es: \n\n"
    for i in range(0, len(ruta)):
        rutaSol = rutaSol + num2paradas(ruta[i]) + "\n"

    transbordos = "Transbordos: no\n"
    if(mp.getHayTrasbordo()):
        transbordos = "Transbordos: sí\n"+"Tiempo estimado de "+str(mp.getTiempoTrasbordo())+" mins"
    
    
    tiempoTotal = "El tiempo total estimado es de " + str(round(mp.getTiempo())) + " mins\n"+ str(mp.getTiempoCaminar()) + " mins andando, "+str(round(mp.getTiempoTransporte(),2))+" mins en metro\n"
    
    if(salida!=0):
        tiempoTotal = "Cogiendo el primer metro, a las " + str(horaComienzo[salida-1]) + ":\n" + tiempoTotal
    
    if(salida==0):
        horaLlegada = int(h)
        minutoLlegada = round(int(m)+mp.getTiempo())
        if(minutoLlegada>60):
            minutoLlegada-=60
            horaLlegada +=1
            if(int(minutoLlegada)<10):
                minutoLlegada = "0"+str(minutoLlegada)
        tiempoTotal += "Llegará aproximadamente a las " + str(horaLlegada) + ":" + str(minutoLlegada)

    labelTop.configure(text="Precio = 8 UAH\n\n"+rutaSol+ "\n\n" + tiempoTotal + "\n\n" +transbordos, font=("Arial", 14))
    
    
#-------------------------------------#
""" BOTON INICIO Y BUCLE PRINCIPAL  """
#-------------------------------------#

botonfinal = ttk.Button(miframe, text="Buscar", command=lambda: codigoInicio(
    cuadro1.current(), cuadro2.current(), cuadro3.get(), cuadro4.get()))
botonfinal.grid(row=2,column=3)
botonfinal.config(cursor="hand2")
# ----------------bucle--------
raiz.mainloop()

