import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

class Cubo:
    
    def __init__(self, dim, vel):
        #Se inicializa las coordenadas de los vertices del cubo
        self.vertexCoords = [  
                   1,1,1,   1,1,-1,   1,-1,-1,   1,-1,1,
                  -1,1,1,  -1,1,-1,  -1,-1,-1,  -1,-1,1  ]

        self.DimBoard = dim
        #Se inicializa una posicion aleatoria en el tablero
        self.Position = []
        #Inicializar las coordenadas (x,y,z) del cubo en el tablero
        #almacenandolas en el vector Position
        #...
        #Se inicializa un vector de direccion aleatorio
        self.Direction = []
        #El vector aleatorio debe de estar sobre el plano XZ (la altura en Y debe ser fija)
        #Se normaliza el vector de direccion
        #...
        #Se cambia la maginitud del vector direccion con la variable vel
        #...
        

    def update(self):
        #Se debe de calcular la posible nueva posicion del cubo a partir de su
        #posicion acutual (Position) y el vector de direccion (Direction)
        #...
        
        #Se debe verificar que el objeto cubo, con su nueva posible direccion
        #no se salga del plano actual (DimBoard)
        #...

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5,5,5)
        #Se dibuja el cubo
        #...
        glPopMatrix()