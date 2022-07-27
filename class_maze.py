from cmu_112_graphics import *
from tkinter import *
import random

# maze - dfs
# pathfinding - Dijkstra's

class maze:
    def __init__(self, rows = 9, cols = 9, cellSize = 30):
        self.rows = rows
        self.cols = cols
        self.cellSize = cellSize
        self.maze = [ ([None]* cols) for row in range(rows)]
        self.graph = self.generateGraph(self.rows, self.cols)

    def generateGraph(self, rows, cols):
        graph = dict()
        for row in range(rows):
            for col in range(cols):
                graph[(row, col)] = set([])
        return graph

    def dfs(self):
        start = (0, 0)
        visited = [start]
        dfsHelper = self.dfsHelper(visited, start[0], start[1])
        if dfsHelper != None:
            return dfsHelper

    def dfsHelper(self, visited, currentRow, currentCol):
        up = (-1, 0) 
        down = (+1, 0)
        right = (0, +1)
        left = (0, -1)
        possibleDirections = [ up, down, right, left]
        random.shuffle(possibleDirections)
        currentCell = (currentRow, currentCol)
        visited.append(currentCell)
        if len(visited) == self.rows * self.cols:
            return self.graph
        for (dx, dy) in possibleDirections:
            newRow = currentRow + dx
            newCol = currentCol + dy
            newCell = (newRow, newCol)
            if newCell in visited:
                continue
            elif newCell not in visited:
            # check if newRow and newCol is in position
                if ((newRow >= 0 and newRow < self.rows) and 
                    (newCol >= 0 and newCol < self.cols)):
                    if (dx, dy) == up:
                        newCell = (currentCell[0] - 1, currentCell[1])
                    elif (dx, dy) == down:
                        newCell = (currentCell[0] +1 , currentCell[1])
                    elif (dx, dy) == left:
                        newCell = (currentCell[0], currentCell[1]-1)
                    elif (dx, dy) == right:
                        newCell = (currentCell[0], currentCell[1] +1)
                    self.graph[currentCell].add(newCell)
                    self.graph[newCell].add(currentCell)
                    self.dfsHelper(visited, newCell[0], newCell[1])