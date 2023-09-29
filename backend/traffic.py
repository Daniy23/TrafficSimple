import numpy as np

from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from mesa.visualization.ModularVisualization import ModularServer

from SimpleContinuousModule import SimpleCanvas

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from mesa.space import SingleGrid
from mesa.visualization.modules import CanvasGrid

class Car(Agent):
    def __init__(self, model, pos):
        super().__init__(model.next_id(), model)
        self.pos = pos

    def step(self):
        matrix = [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                [0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
                [0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0],
                [0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0],
                [0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0],
                [0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
                [0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
                [0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0],
                [0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0],
                [0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0],
                [0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0],
                [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]

        grid = Grid(matrix=matrix)
        (x,y) =self.pos

        start = grid.node(x, y)
        end = grid.node(1, 1)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end)) 
        self.model.grid.move_agent(self, path[1])


class Street(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(25, 10, True)
        self.grid = SingleGrid(17, 14, torus=False)
        self.schedule = RandomActivation(self)

        for px in np.random.choice(25 + 1, 5, replace=False):
            car = Car(self, np.array([px, 5]), np.array([1.0, 0.0]))
            self.space.place_agent(car, car.pos)
            self.schedule.add(car)
        

    def step(self):
        self.schedule.step()

def car_draw(agent):
    color = "Blue" if agent.unique_id == 1 else "Brown"
    return {"Shape": "rect", "w": 0.034, "h": 0.02, "Filled": "true", "Color": color}

canvas = SimpleCanvas(car_draw, 500, 500)

model_params = {}

server = ModularServer(Street, [canvas], "Traffic", model_params)
server.port = 8522
server.launch()

