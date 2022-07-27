from cmu_112_graphics import *
from tkinter import *
import random
from class_minions import *
from class_maze import *
# from TPMainJP import *

# maze - dfs
# pathfinding - Dijkstra's

class movement():
    def __init__(self):
        self.maze = maze()
        self.graph = self.maze.graph

    def bfs(self, graph, start, target):
        queue = [start]
        visited = set()
        visited.add(start)
        path = {}
        result = [target, target]
        while len(queue) > 0:
            node = queue.pop(0)
            # base case
            if node == target:
                # result.append(target)
                while result[0] != start:
                    currentPosition = result[0]
                    result.insert(0, path[currentPosition])
                return result
            else:
                # for neighbor in neighbors(self, row, col)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        # Update the mapping so that N points to the node
                        path[neighbor] = node
                        # path[neighbor] = node
        # return no path
        return None