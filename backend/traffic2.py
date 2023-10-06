import numpy as np

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
        if (x == self.posc[0]) and (y == self.posc[1]):
            self.speed = np.array(direccionAbajo)
        elif (x == self.posc1[0]) and (y == self.posc1[1]):
            self.speed = np.array(direccionAbajo)
        new_pos = self.pos + np.array([1,1]) * self.speed

        
        if not self.agent_position(new_pos[0], new_pos[1]): 
            self.model.space.move_agent(self, new_pos)  
    
            
    def agent_position(self, x, y):
            agents = self.model.space.get_neighbors((x, y), radius =0, include_center = True)
            return any(isinstance(agent, Car) for agent in agents)
            



class Street(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(25, 25, True)
        self.schedule = RandomActivation(self)

#CANTIDAD DE CARROS
        ncarros = 4
#Generación de carros lado A YAAA ESTA 
        # a = 5
        
        # for px in np.random.choice(1, ncarros, replace=True):
        #     car = Car(self, np.array([a, px]), np.array([0.0, 1.0]))
        #     self.space.place_agent(car, car.pos)
        #     self.schedule.add(car)
# #Generación de carros lado B
        b = 5
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([px, b]), np.array([1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
#Generación de carros lado C YAA ESTA 
        # c = 10
        # for px in np.random.choice(1, ncarros, replace=True):
        #     car = Car(self, np.array([c, px]), np.array([0.0, -1.0]))
        #     self.space.place_agent(car, car.pos)
        #     self.schedule.add(car)

        d = 10
        for px in np.random.choice(1, ncarros, replace=True):
            car = Car(self, np.array([px, d]), np.array([-1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)

    def step(self):
        self.schedule.step()

def car_draw(agent):
    color = "Blue" if agent.unique_id == 1 else "Brown"
    return {"Shape": "rect", "w": 0.034, "h": 0.02, "Filled": "true", "Color": color}

canvas = SimpleCanvas(car_draw, 500, 500)

model_params = {}

# server = ModularServer(Street, [canvas], "Traffic2", model_params)
# server.port = 8522
# server.launch()
