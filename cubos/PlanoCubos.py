#Autor: Ivan Olmos Pineda
#Curso: Multiagentes - Graficas Computacionales

import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Se carga el archivo de la clase Cubo
from Cubo import Cubo


import requests

URL_BASE = "http://localhost:5000"
r = requests.post(URL_BASE+ "/games", allow_redirects=False)
print(r.headers)
LOCATION = r.headers["Location"]

lista = r.json()


screen_width = 600
screen_height = 600

textures = []
piso = "mapa.bmp"

#vc para el obser.
FOVY=60.0
ZNEAR=1.0
ZFAR=1800.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=400.0
EYE_Y=200.0
EYE_Z=400.0
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
DimBoard = 200
contador = 0
pygame.init()

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

cubos = {}

print(lista)
for agent in lista:
    cubo = Cubo(agent["x"], agent["z"])
    cubos[agent["id"]] = cubo

def Init():
    pygame.display.set_mode(
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
    Texturas(piso)
    
    
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
        
def display():
    global contador
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    PlanoTexturizado()
    #Se dibuja el plano gris
    # glColor3f(0.3, 0.3, 0.3)
    # glBegin(GL_QUADS)
    # glVertex3d(-DimBoard, 0, -DimBoard)
    # glVertex3d(-DimBoard, 0, DimBoard)
    # glVertex3d(DimBoard, 0, DimBoard)
    # glVertex3d(DimBoard, 0, -DimBoard)
    # glEnd()
    #Se dibuja cubos
    for cubo in cubos.values():
        cubo.draw()
    
    if contador == 3:
       response = requests.get(URL_BASE + LOCATION)
       lista = response.json()
       for agent in lista:
           cubos[agent["id"]].update(agent["x"] * 20 - 160, agent["z"] * 20 - 160)
       contador = 0
    else: 
       contador += 1
        
        

    # response = requests.get(URL_BASE + LOCATION)
    # lista = response.json()
    # for agent in lista:
    #     cubos[agent["id"]].update(agent["x"] * 20 - 160, agent["z"] * 20 - 160)
    
done = False
Init()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()