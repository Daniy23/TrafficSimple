import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from objloader import *

import random
import math


import sys
sys.path.append('..')

from city import Cubo, Lamps, Benches, Casas

done = False

screen_width = 500
screen_height = 500

nceldas = 20

textures = []
piso = "mapa.bmp"
celda = "slyth.bmp"


#vc para el obser.
FOVY=60.0
ZNEAR=0.01
ZFAR=900.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=1.0
EYE_Y=800.0
EYE_Z=1.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0
UP_X=0
UP_Y=1
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500
#Dimension del plano
DimBoard = 370
DimBoard2 = 100


pygame.init()

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image,"RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)
    
def Init():
    global cubos, lamps1, lamps2, lamps3, lamps4, bench1, bench2, bench3, bench4, casa1
    #plano  #variables

    
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) 

    Texturas(piso)
    Texturas(celda)
 
    #Crear cubos
    cubos = Cubo(DimBoard)   #cubos, segundo argumento velocida
    lamps1 = Lamps(DimBoard, -155, -155)
    lamps2 = Lamps(DimBoard, 155, 155)
    lamps3 = Lamps(DimBoard, -155, 155)
    lamps4 = Lamps(DimBoard, 155, -155)
    bench1 = Benches(DimBoard, -110, 0)
    bench2 = Benches(DimBoard, 0, -110)
    bench3 = Benches(DimBoard, 110, 0)
    bench4 = Benches(DimBoard, 0, 110)
    casa1 = Casas(DimBoard, random.randrange(0,200), random.randrange(0,200))

    cubos.loadmodel()
    lamps1.loadmodel()
    lamps2.loadmodel()
    lamps3.loadmodel()
    lamps4.loadmodel()
    bench1.loadmodel()
    bench2.loadmodel()
    bench3.loadmodel()
    bench4.loadmodel()
    casa1.loadmodel()
    #basuras en plano
        
        
def PlanoTexturizado():
    glColor3f(1.0,1.0,1.0)
    glEnable(GL_TEXTURE_2D)
    #Front face
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
def Plano2Texturizado():
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    # Front face
    glBindTexture(GL_TEXTURE_2D, 0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard2 / 2, 0, -DimBoard2 / 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-DimBoard2 / 2, 0, DimBoard2 / 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard2 / 2, 0, DimBoard2 / 2)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(DimBoard2 / 2, 0, -DimBoard2 / 2)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    PlanoTexturizado()
        
    lamps1.generate()
    lamps2.generate()
    lamps3.generate()
    lamps4.generate()
    cubos.generate()
    bench1.generate()
    bench2.generate()
    bench3.generate()
    bench4.generate()
    casa1.generate()
    

Init()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()