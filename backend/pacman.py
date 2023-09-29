from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class Ghost(Agent):
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
             
            # ## next_moves = self.model.grid.get_neighborhood(self.pos, moore=False)
            #  (x,y) = self.random.choice(next_moves)
            #  if matrix[y][x] != 0:
            #       self.model.grid.move_agent(self, (x,y))##
                  



class Block(Agent):
  def __init__(self, model, pos):
    super().__init__(model.next_id(), model)
    self.pos = pos


class Maze(Model):
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(17, 14, torus=False)

        ghost = Ghost(self, (8, 6))
        self.grid.place_agent(ghost, ghost.pos)
        self.schedule.add(ghost)
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

        for _,(x,y) in self.grid.coord_iter():
            if matrix[y][x] == 0:
                print(f"block at ({x},{y})")
                block = Block(self, (x, y))
                self.grid.place_agent(block, block.pos)

        grid = Grid(matrix=matrix)    
        start = grid.node(0, 0)
        end = grid.node(2, 2)
        
    def step(self):
        self.schedule.step()

def agent_portrayal(agent):
  if type(agent) == Ghost:
     return {"Shape": "ghost.png", "Layer": 0}
  
  elif type(agent)==Block:
    return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Gray", "Layer": 0}
  

grid = CanvasGrid(agent_portrayal, 17, 14, 450, 450)

server = ModularServer(Maze, [grid], "PacMan", {})
server.port = 8522
server.launch()



