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

from city import Cubo, Lamps, Benches, Casas, Ship, Edificios, Edificios2, Edificios3, Perrito, luz

done = False

import requests

URL_BASE = "http://localhost:5000"
r = requests.post(URL_BASE+ "/games", allow_redirects=False)
print(r)
#LOCATION = r.headers["location"]


elementos = r.json()
cars = elementos['cars']
LOCATION = elementos["location"]

screen_width = 500
screen_height = 500

nceldas = 20

textures = []
piso = "mapa.bmp"
celda = "slyth.bmp"


#vc para el obser.
FOVY=60.0
ZNEAR=0.01
ZFAR=10000.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=300.0
EYE_Y=400.0
EYE_Z=300.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0
UP_X=0
UP_Y=1
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-900
X_MAX=900
Y_MIN=-900
Y_MAX=900
Z_MIN=-900
Z_MAX=900
#Dimension del plano
DimBoard = 370
DimBoard2 = 100

pygame.init()

carros = {}
for agent in cars:
    car = Ship(DimBoard, agent["x"], agent["z"], 0)
    carros[agent["id"]] = car

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
    global perro, perro2, cubos, lamps1, lamps2, lamps3, lamps4, bench1, bench2, bench3, bench4, casa1, ship1, ship2, edificio1,edificio2, edificio3
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
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.8, 0.8, 0.8, 1.0))
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
    bench1 = Benches(DimBoard, -110, 0, 0)
    bench2 = Benches(DimBoard, 0, -110, -90)
    bench3 = Benches(DimBoard, 110, 0, 180)
    bench4 = Benches(DimBoard, 0, 110, 90)
    casa1 = Casas(DimBoard, random.randrange(0,200), random.randrange(0,200))
    #ship1 = Ship(DimBoard, 120, 120, 0)
    #ship2 = Ship(DimBoard, -120, -120, 0)
    edificio1 = Edificios(DimBoard, -300, 450, 90)
    edificio2 = Edificios2(DimBoard, -300, -200, 180)
    edificio3 = Edificios3(DimBoard, 270, -220, 180)
    #edificio4 = Edificios4(DimBoard, 7, 7, 180)
    #    edificio4 = Edificios4(DimBoard, 270, 220, 180)
    perro = Perrito(DimBoard, 250, 150, 0)
    perro2 = Perrito(DimBoard, 300, 200, 0)

    cubos.loadmodel()
    lamps1.loadmodel()
    lamps2.loadmodel()
    lamps3.loadmodel()
    lamps4.loadmodel()
    bench1.loadmodel()
    bench2.loadmodel()
    bench3.loadmodel()
    bench4.loadmodel()
    #ship1.loadmodel()
    #ship2.loadmodel()
    edificio1.loadmodel()
    edificio2.loadmodel()
    edificio3.loadmodel()
    perro.loadmodel()
    perro2.loadmodel()
    #casa1.loadmodel()
    #basuras en plano

    for ship in carros.values():
        ship.loadmodel()
        
       
def PlanoTexturizado():
    
    glColor3f(1.0,1.0,1.0)
    glEnable(GL_TEXTURE_2D)
    #glEnable(GL_LIGHT1)
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
    glDisable(GL_LIGHT0)
    
    
def Plano2Texturizado():

    glColor3f(1.0,1.0,1.0)
    glEnable(GL_TEXTURE_2D)
    #glEnable(GL_LIGHT1)
    glColor3f(1.0, 1.0, 1.0)
    #glEnable(GL_LIGHT1)
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
    glDisable(GL_LIGHT0)
   


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
    edificio1.generate()
    edificio2.generate()
    edificio3.generate()
    perro.generate()
    perro2.generate()
    
    perro.move()
    perro2.move()
    
    for ship in carros.values():
        ship.generate()


    response = requests.get(URL_BASE + LOCATION)
    elementos = response.json()
    cars = elementos["cars"]

    for agent in cars:
        carros[agent["id"]].update(agent["x"] * 28 - 340, agent["z"] *28 - 340)
        carros[agent["id"]].rotate(agent["degrees"])
    #ship1.generate()
    #casa1.generate()
    cmddown = False

    #ship1.rotate(0.5)
    #ship2.rotate(0.5)
    
#...
    keypress = pygame.key.get_pressed()#Move using WASD
    if keypress[pygame.K_w]:
        glTranslatef(0,0,2.0)
    if keypress[pygame.K_s]:
        glTranslatef(0,0,-2.0)
    if keypress[pygame.K_d]:
        glTranslatef(-2.0,0,0)
    if keypress[pygame.K_a]:
        glTranslatef(2.0,0,0)
    if keypress[pygame.K_LSHIFT]:
        glTranslatef(0,2.0,0)
    if keypress[pygame.K_SPACE]:
        glTranslatef(0,-2.0,0)
    if keypress[pygame.K_LEFT]:
        glRotatef(1, 0.0, 1.0, 0.0)
    if keypress[pygame.K_RIGHT]:
        glRotatef(1, 0.0, -1.0, 0.0)
    #gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)

Init()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()
    pygame.display.flip()
    pygame.time.wait(10)


    #glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    #glLightfv(GL_LIGHT1, GL_DIFFUSE, (5, 5, 0, 1.0))  # Intensidad alta
    #glLightfv(GL_LIGHT1, GL_AMBIENT, (0, 0, 0, 1.0))  # Intensidad alta
    




pygame.quit()