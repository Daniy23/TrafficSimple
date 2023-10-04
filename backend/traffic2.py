import numpy as np

import random

from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from mesa.visualization.ModularVisualization import ModularServer

from SimpleContinuousModule import SimpleCanvas

from pathfinding.core.grid import Grid
from mesa.space import SingleGrid

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

class Car(Agent):
    def __init__(self, model: Model, pos, posfinal):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.posfinal = posfinal

    def step(self):
        matrix = [
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]]
        
        grid = Grid(matrix=matrix)
        (x,y) =self.pos
        (a,b) = self.posfinal
        
        start = grid.node(x, y)
        end = grid.node(a, b)
        
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end)) 
        self.model.grid.move_agent(self, (path[1].x, path[1].y))
    
class Street(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(15, 15, True)
        self.grid = SingleGrid(15, 15, torus=True)

        self.schedule = RandomActivation(self)
        matrix = [
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]]
        
    

        car = Car(self, (6, 0), (0, 6))
        self.grid.place_agent(car, car.pos)
        self.schedule.add(car)
        
        # car = Car(self, (0,6), (0, 8))
        # self.grid.place_agent(car, car.pos)
        # self.schedule.add(car)
        
        car2 = Car(self, (6, 14), (0, 8))
        self.grid.place_agent(car2, car2.pos)
        self.schedule.add(car2)

    def step(self):
        self.schedule.step()

def car_draw(agent):
    color = "Blue" if agent.unique_id == 1 else "Brown"
    if type(agent) == Car:
        return {"Shape": "rect", "w": 0.034, "h": 0.02, "Filled": "true", "Color": color}

canvas = SimpleCanvas(car_draw, 500, 500)

model_params = {}

# server = ModularServer(Street, [canvas], "Traffic2", model_params)
# server.port = 8522
# server.launch()

