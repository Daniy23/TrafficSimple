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

class Ship:

    def __init__(self, dim, x, y, angulo):
        self.angulo = angulo
        self.Position = [x, 5, y]
        self.angulo = 0
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("imp_fly_tiefighter.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        #global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(7,7,7)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        glRotate(50,0,0,1)
        #self.rotar()
        self.obj.render()
        glPopMatrix()

    def rotate(self, anguloNave):
        self.angulo = self.angulo + anguloNave
        glPushMatrix()
        glRotatef(self.angulo,0,1,0)
        glTranslatef(14.5,0.0,0.0)
        self.generate()
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
        glScaled(1,1,1)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        #self.rotar()
        self.obj.render()

        #glLightfv(GL_LIGHT0, GL_POSITION,  (self.Position[0], self.Position[1]+150, self.Position[2], 1))
        #glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0.2, 0.2, 1.0))
        #glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0,-1.0,0))
        #glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 20)
        #glLightfv(GL_LIGHT0, GL_SPOT_EXPONENT, 0)
        #glEnable(GL_LIGHT0)
        #glEnable(GL_LIGHTING)
        #glEnable(GL_COLOR_MATERIAL)
        #glEnable(GL_DEPTH_TEST)
        #glShadeModel(GL_SMOOTH) 

        glPopMatrix()



class Benches:

    def __init__(self, dim, x , y, angle):
        
        self.angulo = angle
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
        glRotate(self.angulo,0,0,1)
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

