
from cmu_112_graphics import *
from tkinter import *
import random
from class_maze import *
from class_movement import *

""" This is a class for enemies. """
""" enemy uses bfs algorithm to follow the player"""
class enemies(object):
    def __init__(self):
        self.margin = 50
        self.cols = 9
        self.rows = 9
        self.minionLocations = []
        self.minionCxCys = []
        self.width = 790
        self.height = 790
        self.gridWidth  = self.width - 2*self.margin
        self.gridHeight = self.height - 2*self.margin
        self.cellWidth = self.gridWidth / self.cols
        self.cellHeight = self.gridHeight / self.rows

    def minionLocation(self):
        minionCount = 0
        while minionCount < 6:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if (row== 0 and col == 0) or (row== 0 and col == 1) or \
            (row == 1 and col == 0) or (row == 1 and col == 1):
                continue
            if (row , col) not in self.minionLocations:
                self.minionLocations.append((row, col))
                minionCount += 1

    def getMinionPositions(self):
        for minionLoc in self.minionLocations:
            minionRow = minionLoc[0]
            minionCol = minionLoc[1]
            # print(minionLoc)

            minionX0 = self.margin + minionCol * self.cellWidth
            minionX1 = self.margin + (minionCol+1) * self.cellWidth
            minionY0 = self.margin + minionRow * self.cellHeight
            minionY1 = self.margin + (minionRow+1) * self.cellHeight
            minionCx = (minionX1 + minionX0)/2
            minionCy = (minionY1 + minionY0)/2
            # print((minionX0, minionX1, minionY0, minionY1))
            # print((minionCx, minionCy))

            self.minionCxCys.append((minionCx, minionCy))
