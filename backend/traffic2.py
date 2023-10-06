import numpy as np
import random
from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from mesa.visualization.ModularVisualization import ModularServer

from SimpleContinuousModule import SimpleCanvas


class Car(Agent):
    
    #No importa la direcccion a la que empiecen, cuando se encuentra en un punto critico cambia
    posc = [6,10]
    posc1 = [6,5]
    def __init__(self, model: Model, pos, speed):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.speed = speed
    


    def step(self):   
        x, y = self.pos  
        direccionAbajo = [0,0.5] 
        direccionArriba = [ 0,-1]
        
        direccionDerecha = [0.5, 0] 
        direccionIzquierda = [-1, 0]

#ESTOS SON DECISIONES PARA CONTROLAR LA NUEVA DIRECCION DEL CARRO
        
        #RUTA B 
        randomB = random.choice([direccionAbajo, direccionDerecha])
        if (x == 7) and (y == 14):
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
        elif (x == 10) and (y == 18):
            self.speed = np.array(randomB)
        #RUTA D
        randomD = random.choice([direccionArriba, direccionIzquierda])
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
        #Ruta A  
        randomA = random.choice([direccionAbajo, direccionIzquierda])  
        if (x == 10) and (y == 6):
            self.speed = np.array(direccionAbajo)
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
        elif (x == 18) and (y == 14):
            self.speed = np.array(randomC)
            
    #----------------------------------------------------------------------------    
    #ESTA ES LA VERSION ANTERIOR EN LA QUE LA POSICION SE ACTUALIZABA
    
    #NUEVAS POSICIONES 
    #     new_pos = self.pos + np.array([1,1]) * self.speed
    #     if not self.agent_position(new_pos[0], new_pos[1]): 
    #         self.model.space.move_agent(self, new_pos)  
    
            
    # def agent_position(self, x, y):
    #         agents = self.model.space.get_neighbors((x, y), radius =0, include_center = True)
    #         return any(isinstance(agent, Car) for agent in agents)

#-----------------------------------------------------------------------------------------
#ESTA ES LA NUEVA VERSION QUE QUIERO IMPLEMENTAR, SIGUIENDO SUS SUGERENCIAS CON CAR_AHEAD        
    # #Nueva Implementacion 
        car_ahead = self.car_ahead()
        new_speed = self.accelerate() if car_ahead == None else self.decelerate(car_ahead)

        self.speed = np.array(new_speed)
        new_pos = self.pos +  self.speed
        self.model.space.move_agent(self, new_pos)


    def car_ahead(self):
        for neighbor in self.model.space.get_neighbors(self.pos, 1):
            if neighbor.pos[0] > self.pos[0]:
                return neighbor
        return None

    def accelerate(self):
        return self.speed[0] * 0.5, self.speed[1] * 0.5

    def decelerate(self, car_ahead):
        return car_ahead.speed[0] * -0.1, car_ahead.speed[1] * -0.1
            



class Street(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(25, 25, True)
        self.schedule = RandomActivation(self)

#CANTIDAD DE CARROS
        ncarros = 1
#Generación de carros lado A YAAA ESTA 
        a = 10
        
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([a, px]), np.array([0.0, 1.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
# # #Generación de carros lado B
        b = 14
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([px, b]), np.array([1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
# # #Generación de carros lado C YAA ESTA 
#         c = 9
#         for px in np.random.choice(1, ncarros, replace=True):
#             car = Car(self, np.array([14, px]), np.array([0.0, -1.0]))
#             self.space.place_agent(car, car.pos)
#             self.schedule.add(car)
# #Generacion de carros lado D
#         d = 10
#         for px in np.random.choice(1, ncarros, replace=True):
#             car = Car(self, np.array([px, d]), np.array([-1.0, 0.0]))
#             self.space.place_agent(car, car.pos)
#             self.schedule.add(car)

    def step(self):
        self.schedule.step()

def car_draw(agent):
    color = "Blue" if agent.unique_id == 1 else "Blue" if agent.unique_id == 2 else "green" if agent.unique_id == 3 else "green" if agent.unique_id == 4 else "Brown" if agent.unique_id == 5 else "brown" if agent.unique_id == 6 else "yellow" if agent.unique_id == 7 else "yellow"
    return {"Shape": "rect", "w": 0.034, "h": 0.02, "Filled": "true", "Color": color}

canvas = SimpleCanvas(car_draw, 500, 500)

model_params = {}

# server = ModularServer(Street, [canvas], "Traffic2", model_params)
# server.port = 8522
# server.launch()
modelo = Street()
modelo.step()
modelo.step()

#try