import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from objloader import *

import random
import math

class Agua:
    def __init__(self):
        self.position = [0, 50, 0]
        self.size = 2
        
        
        #self.direction = [
           # 0.5, 2.5,-0.5]
        
        self.direction = [
            random.uniform(-0.5, 0.5), 2.5, random.uniform(-0.5, 0.5)] #Direccion aleatoria
        
        self.gravity = -9.81 * 0.007 

    def update(self):
        self.direction[1] += self.gravity
        
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1] 
        self.position[2] += self.direction[2]

    def create(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glScalef(self.size, self.size, self.size)
        glColor3f(0.0, 0.5, 1.0) #Azul

    #Coordenadas de los vértices
        self.vertexCoords = [  
               1,1,1,   1,1,-1,   1,-1,-1,   1,-1,1,
              -1,1,1,  -1,1,-1,  -1,-1,-1,  -1,-1,1  ]
        

    #Indices para formar las caras del cubo
        self.elementArray = [ 
              0,1,2,3, 0,3,7,4, 0,4,5,1,
              6,2,1,5, 6,5,4,7, 6,7,3,2  ]
    
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vertexCoords)
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, self.elementArray)
        glDisableClientState(GL_VERTEX_ARRAY)
        glColor3f(1.0, 1.0, 1.0)

        glPopMatrix()
   
        



    


        
class Cubo:

    def __init__(self, dim):
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [50,5,-50]

        self.direction = [0,0,0]
        self.agua_disponible = []
        
    def display_list(self):
        for i in self.agua_disponible:
            i.create()
        
    def add_list(self):
        agua = Agua()
        self.agua_disponible.append(agua)

    def update_list(self):
        agua_eliminada = []
        for i in self.agua_disponible:
            i.update()
            if i.position[1] < -30:
                #Elimina cubos (agua) en cierto eje Y para no alentar el programa
                agua_eliminada.append(i)
                
        for i in agua_eliminada:
            self.agua_disponible.remove(i)
                
                

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
        nums = 3 #4-5 es ideal pero alenta la simulacion
        for i in range(nums):
            self.add_list()

        self.update_list()
        self.display_list()

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
        
        # Se inicializa una posición aleatoria en el tablero
        self.Position = [x, 5, y]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("fobj_lamp.obj", swapyz=True)
        self.obj.generate()
            
    def generate(self):
        # global obj
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(1,1,1)
        glRotate(90,0,0,1)
        glRotate(90,0,1,0)
        # self.rotar()
        self.obj.render()
        
        
        luz()
        

        glPopMatrix()

def luz():
        #glLightfv(GL_LIGHT1, GL_POSITION, (0, 100, 0, 1))
        #glLightfv(GL_LIGHT1, GL_POSITION, (self.Position[0], self.Position[1], self.Position[2], 1))
        glLightfv(GL_LIGHT1, GL_POSITION, (0, -155, -155, 1))
        
        glLightfv(GL_LIGHT2, GL_POSITION, (0, 100, 0, 1)) #Luz derecha
        
        glLightfv(GL_LIGHT3, GL_POSITION, (0, 100, 0, 1)) 
        
        glLightfv(GL_LIGHT4, GL_POSITION, (370, 155, 155, 1)) 
        
        glLightfv(GL_LIGHT5, GL_POSITION, (0,100,0, 1)) 

        
        #glLightfv(GL_LIGHT1, GL_POSITION, (0, 155, 155, 1))
        #glLightfv(GL_LIGHT1, GL_POSITION, (370, -155, 155, 1))
        #glLightfv(GL_LIGHT1, GL_POSITION, (370, 155, -155, 1))
        
        
        
        #Intensidad
        #glLightfv(GL_LIGHT1, GL_DIFFUSE, (1, 1, 0, 1.0))
        
        glLightfv(GL_LIGHT1, GL_DIFFUSE, (1.5, 1.5, 0, 1.0))
        glLightfv(GL_LIGHT2, GL_DIFFUSE, (2.5, 2.5, 0, 1.0))
        glLightfv(GL_LIGHT3, GL_DIFFUSE, (2.5, 2.5, 0, 1.0)) 
        glLightfv(GL_LIGHT4, GL_DIFFUSE, (30, 30, 0, 1.0)) #Mucha intensidad para testear 
        glLightfv(GL_LIGHT5, GL_DIFFUSE, (2.5, 2.5, 0, 1.0)) 
        #glLightfv(GL_LIGHT1, GL_SPECULAR, [2.5, 2.5, 0, 1.0])
        #glLightfv(GL_LIGHT2, GL_SPECULAR, [2.5, 2.5, 0, 1.0])
        


        
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, (0, 1, 0))
        
        glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, (0, -1, 0)) #Funciona perfectamente
        
        glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, (-1, 0, 0)) #Ilumina centro
        
        glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, (-1, -1, 0)) 
        
        glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, (0, -1, 0)) 

        glLightfv(GL_LIGHT1, GL_SPOT_CUTOFF, 35.0) #Angulo del foco
        glLightfv(GL_LIGHT2, GL_SPOT_CUTOFF, 45.0) #Angulo del foco
        glLightfv(GL_LIGHT3, GL_SPOT_CUTOFF, 45.0)
        glLightfv(GL_LIGHT4, GL_SPOT_CUTOFF, 45.0)
        glLightfv(GL_LIGHT5, GL_SPOT_CUTOFF, 45.0)
        #glLightfv(GL_LIGHT1, GL_SPOT_EXPONENT, 2)
        
        
        #Luz ambiente, aumentar si esta muy oscuro
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1])  # valores RGB para blanco, en el rango [0,1]
    

        glEnable(GL_LIGHTING)
        
        
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT2) #FUnciona bien
        #glEnable(GL_LIGHT3)
        #glEnable(GL_LIGHT4)
        #glEnable(GL_LIGHT5)
        


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

class Edificios:

    def __init__(self, dim, x , y, angle):
        
        self.angulo = angle
        self.objetivo_direction = (0, 0, 1)  
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [x, 5, y]

        self.direction = [0,0,0]

    def loadmodel(self):
        self.obj = OBJ("Edificio.obj", swapyz=True)
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
