import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from objloader import *

import random
import math

class Cubo:

    def __init__(self, dim):
        
        self.angulo = 0
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [50,5,-50]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("fuente.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        #global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(100,100,100)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        #self.rotar()
        self.obj.render()
        glPopMatrix()

class Lamps:

    def __init__(self, dim, x , y):
        
        self.angulo = 0
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [x, 5, y]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("fobj_lamp.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        #global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(.5,.5,.5)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        #self.rotar()
        self.obj.render()
        glPopMatrix()

class Benches:

    def __init__(self, dim, x , y):
        
        self.angulo = 0
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [x, 5, y]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("obj_0402_park_bench.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        #global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5,5,5)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        #self.rotar()
        self.obj.render()
        glPopMatrix()

class Casas:

    def __init__(self, dim, x , y):
        
        self.angulo = 0
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [x, 5, y]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("cool.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        #global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5,5,5)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        #self.rotar()
        self.obj.render()
        glPopMatrix()

