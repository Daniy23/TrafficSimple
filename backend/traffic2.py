import numpy as np
import random
from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from mesa.visualization.ModularVisualization import ModularServer

from SimpleContinuousModule import SimpleCanvas
import math


class Car(Agent):
    
    #No importa la direcccion a la que empiecen, cuando se encuentra en un punto critico cambia 
    #-----------------------------------------------------------------
    def __init__(self, model: Model, pos, speed):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.speed = speed
        self.diagonalPos = 90
        self.vel = 1
    


    def step(self):
        x, y = self.pos  
        direccionAbajo = [0,0.5] 
        direccionArriba = [ 0,-1]
        
        direccionDerecha = [0.5, 0] 
        direccionIzquierda = [-1, 0]
        # print("Hi", self.speed)
        d,v = self.speed 
        d= d * self.vel
        v= v * self.vel
        e = [d,v]
        # print("He", e) 
        # print(e)
        

#ESTOS SON DECISIONES PARA CONTROLAR LA NUEVA DIRECCION DEL CARRO
        
        #RUTA B 
        randomB = random.choice([direccionAbajo, direccionDerecha])
        if (x == 5) and (y == 10):
            self.diagonalPos = 180 # 270 Grados hasta 6, 14
            # self.diagonalPos = np.array(self.diagonalvector(270))
        elif (x == 7) and (y == 10):
            self.diagonalPos = 270
        elif (x == 6) and (y == 14):
            self.diagonalPos = 315 # 315 Grados hasta 10, 18
            # self.diagonalPos = np.array(self.diagonalvector(315))
        elif (x == 7) and (y == 14):
            self.diagonalPos = 315
            self.speed = np.array(direccionAbajo)
        elif (x == 7) and (y == 16):
            self.speed = np.array(direccionDerecha)
        elif (x == 8) and (y == 16):
            self.speed = np.array(direccionAbajo)
        elif (x == 8) and (y == 17):
            self.speed = np.array(direccionDerecha)
        elif (x == 10) and (y == 17):
            self.speed = np.array(direccionAbajo)
        elif (x == 14) and (y == 18):
            self.speed = np.array(direccionArriba)
            self.diagonalPos = 45 #45 Grados hasta 18,14 (1)
            # self.diagonalPos = np.array(self.diagonalvector(45))
        elif (x == 10) and (y == 18):
            self.speed = np.array(randomB)
        elif (x == 11) and (y == 18):
            self.diagonalPos = 180
        elif (x == 10) and (y == 19):
            self.diagonalPos = 270 #0 Grados hasta 14, 18
            # self.diagonalPos = np.array(self.diagonalvector(0))  
        #RUTA D
        randomD = random.choice([direccionArriba, direccionIzquierda])
        # if math.isclose(x, 17) and math.isclose(y, 10):
        #     self.speed = np.array(direccionArriba)
        if (x == 17) and (y == 10):
            self.speed = np.array(direccionArriba)
        elif (x == 17) and (y == 8):
            self.speed = np.array(direccionIzquierda)
        elif (x == 16) and (y == 8):
            self.speed = np.array(direccionArriba)
        elif (x == 16) and (y == 7):
            self.speed = np.array(direccionIzquierda)
        elif (x == 14) and (y == 7):
            self.speed = np.array(direccionArriba)
        elif (x == 14) and (y == 6):
            self.speed = np.array(randomD)
            self.diagonalPos = 180
        elif (x == 14) and (y == 5):
            self.diagonalPos = 90 #180 Grados hasta 10, 6
            # print("GRADOS",self.diagonalPos)
            # self.diagonalPos = np.array(self.diagonalvector(180))
            # print("VECTOR",self.diagonalPos)
        #Ruta A  
        randomA = random.choice([direccionAbajo, direccionIzquierda])  
        if (x == 10) and (y == 6):
            self.speed = np.array(direccionAbajo)
            self.diagonalPos = 225 # 225 grados hasta 6,10
            # self.diagonalPos = np.array(self.diagonalvector(225))
        elif (x == 10) and (y == 7):
            self.speed = np.array(direccionIzquierda)
        elif (x == 8) and (y == 7):
            self.speed = np.array(direccionAbajo)
        elif (x == 8) and (y == 8):
            self.speed = np.array(direccionIzquierda)
        elif (x == 7) and (y == 8):
            self.speed = np.array(direccionAbajo)
        elif (x == 7) and (y == 10):
            self.speed = np.array(randomA)
        #Ruta C
        randomC = random.choice([direccionArriba, direccionDerecha])  
        if (x == 14) and (y == 17):
            self.speed = np.array(direccionDerecha)
        elif (x == 16) and (y == 17):
            self.speed = np.array(direccionArriba)
        elif (x == 16) and (y == 16):
            self.speed = np.array(direccionDerecha)
        elif (x == 17) and (y == 16):
            self.speed = np.array(direccionArriba)
        elif (x == 17) and (y == 14):
            self.speed = np.array(direccionDerecha)
        elif (x == 18) and (y == 10):
            self.speed = np.array(direccionIzquierda)
            self.diagonalPos = 135 #135 Grados grados hasta 14,6
            # self.diagonalPos = np.array(self.diagonalvector(135))
        elif (x == 18) and (y == 14):
            self.speed = np.array(randomC)
        elif (x == 18) and (y == 13):
            self.diagonalPos = 90
        elif (x == 19) and (y == 14):
            self.diagonalPos = 0 #90 grados hasta 18,10 
            # self.diagonalPos = np.array(self.diagonalvector(90))
            
    #--------------------------------------------------------------------------
    #NUEVAS POSICIONES 
        new_pos = self.pos + np.array([1,1]) * self.speed
       # print("New_pos", new_pos)
    #--------------------------------------------------
        if not self.agent_position(new_pos[0], new_pos[1]): 
            self.model.space.move_agent(self, new_pos)
    #...............................................................
    #ACELERACION Y FRENO DE LOS COCHES CONSIDERANDO SUS VECINOS
        # self.speed = self.speed * self.vel
        if self.agent_aceleracion(new_pos[0], new_pos[1]) == True:
            # print("desacelera porque hay coches")
            self.vel = self.vel - 0.4
            # print(self.speed)
        else:
            # print("acelera porque no hay coches")
            self.vel = self.vel + 0.4
            # print(self.speed)

    def agent_aceleracion(self, x, y):
            agents = self.model.space.get_neighbors((x, y), include_center =False, radius=4)
            agentbool =any(isinstance(agent, Car) for agent in agents)
            # print("ACELERACION", agentbool)
            return agentbool
    def agent_position(self, x, y):
            agents = self.model.space.get_neighbors((x, y), include_center =True, radius=0)
            agentbool =any(isinstance(agent, Car) for agent in agents)
            # print("ENFRENTE", agentbool)
            return agentbool
#---------FUNCION---------DIAGONAL-------------------------------
    def diagonalvector(self, grados):
        angulo_grados = grados
        # Convertir el ángulo de grados a radianes
        angulo_radianes = math.radians(angulo_grados)

        # Calcular las componentes del vector
        x = math.cos(angulo_radianes)
        y = math.sin(angulo_radianes)
        vectordiagonal = [x, y]
        return vectordiagonal
    #EJEMPLO DE IMPLEMENTACION, DESCOMENTA LA LINEA 72-24
                

class Street(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(25, 25, True)
        self.schedule = RandomActivation(self)

#CANTIDAD DE CARROS
        ncarros = 4
#Generación de carros lado A YAAA ESTA 
        a = 10
        
        for px in np.random.choice(1, ncarros, replace=True):
            #               Posicion Inicial    direccion inicial
            car = Car(self, np.array([a, px]), np.array([0.0, 1.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
# # #Generación de carros lado B
        b = 14
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([px, b]), np.array([1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
# #Generación de carros lado C YAA ESTA 
        c = 14
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([c, px]), np.array([0.0, -1.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
#Generacion de carros lado D
        d = 10
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([px, d]), np.array([-1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)

    def step(self):
        self.schedule.step()

def car_draw(agent):
    color = "Blue" if agent.unique_id == 1 else "Green" if agent.unique_id == 2 else "green" if agent.unique_id == 3 else "green" if agent.unique_id == 4 else "Brown" if agent.unique_id == 5 else "brown" if agent.unique_id == 6 else "yellow" if agent.unique_id == 7 else "yellow"
    return {"Shape": "rect", "w": 0.02, "h": 0.02, "Filled": "true", "Color": color}

canvas = SimpleCanvas(car_draw, 500, 500)

model_params = {}

# server = ModularServer(Street, [canvas], "Traffic2", model_params)
# server.port = 8522
# server.launch()


#try