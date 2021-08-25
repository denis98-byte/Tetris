#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

class Forma(object):
    formaNinguna = 0
    formaI = 1
    formaL = 2
    formaJ = 3
    formaT = 4
    formaO = 5
    formaS = 6
    formaZ = 7

    #Tupla con las coordenadas de las formas del juego tetris
    coordenadas = (
        ((0, 0), (0, 0), (0, 0), (0, 0)), #Las coordenadas de la formaNinguna
        ((0, -1), (0, 0), (0, 1), (0, 2)), #Las coordenadas de la formaI
        ((0, -1), (0, 0), (0, 1), (1, 1)), #Las coordenadas de la formaL
        ((0, -1), (0, 0), (0, 1), (-1, 1)), #Las coordenas de la formaJ
        ((0, -1), (0, 0), (0, 1), (1, 0)), #Las coordenadas de la formaT
        ((0, 0), (0, -1), (1, 0), (1, -1)), #Las coordenadas de la forma O
        ((0, 0), (0, -1), (-1, 0), (1, -1)), #Las coordenadas de la forma S
        ((0, 0), (0, -1), (1, 0), (-1, -1)) #Las coordenadas de la forma Z
    )

    #Funcion principal
    def __init__(self, forma=0):
        self.forma = forma  #Se instancia la forma

    def desplazamientos(self, direccion):
        coordenadasTemporales = Forma.coordenadas[self.forma]
        if direccion == 0 or self.forma == Forma.formaO:
            return ((x, y) for x, y in coordenadasTemporales)

        if direccion == 1:
            return ((-y, x) for x, y in coordenadasTemporales)

        if direccion == 2:
            if self.forma in (Forma.formaI, Forma.formaZ, Forma.formaS):
                return ((x, y) for x, y in coordenadasTemporales)
            else:
                return ((-x, -y) for x, y in coordenadasTemporales)

        if direccion == 3:
            if self.forma in (Forma.formaI, Forma.formaZ, Forma.formaS):
                return ((-y, x) for x, y in coordenadasTemporales)
            else:
                return ((y, -x) for x, y in coordenadasTemporales)

    def obtenerCoordenadas(self, direcion, x, y):
        return ((x + xx, y + yy) for xx, yy in self.desplazamientos(direcion))

    def movimientos(self, direccion):
        coordenadasTemporales = self.desplazamientos(direccion)
        maxX, maxY, minX, minY = 0, 0, 0, 0

        for x, y in coordenadasTemporales:
            if minY > y:
                minY = y
            if maxY < y:
                maxY = y
            if minX > x:
                minX = x
            if maxX < x:
                maxX = x
        return (minX, maxX, minY, maxY)

class Tablero(object):
    ancho = 10
    altura = 22

    def __init__(self):
        #Definicion de variables
        self.fondo = [0] * Tablero.ancho * Tablero.altura
        self.actualX = -1
        self.actualY = -1
        self.actualDireccion = 0
        self.actualForma = Shape()
        self.siguienteForma = Shape(random.randint(1, 7))
        self.actualEstado = [0] * 8