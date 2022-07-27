
from cmu_112_graphics import *
from tkinter import *
import random
from class_maze import *
from class_movement import *
from class_minions import *
# from TP_Main_Jei_Park import *

class Player(object):
    def __init__(self):
        # self.playerFront = self.loadImage('graphics/player/playerFront.png')
        # self.playerFront = self.scaleImage(self.playerFront, 0.07)

        # self.playerBack = self.loadImage('graphics/player/playerBack.png')
        # self.playerBack = self.scaleImage(self.playerBack, 0.07)

        # self.playerLeft = self.loadImage('graphics/player/playerLeft.png')
        # self.playerLeft = self.scaleImage(self.playerLeft, 0.07)

        # self.playerRight = self.loadImage('graphics/player/playerRight.png')
        # self.playerRight = self.scaleImage(self.playerRight, 0.07)

        # self.playerImage = self.playerFront

        self.isTrapped = False
        self.isDead = False
        # self.cx = 50 + self.cellWidth / 2 # top left cell
        # self.cy = 50 + self.cellHeight / 2
        self.row = 0
        self.col = 0
        # self.playerLocation = (self.cx, self.cy)
        self.wallThick = 10
        self.maze = maze()
        self.dfs = self.maze.dfs()
        self.dfsGraph = self.maze.graph














    # def screen(self):
    #     self.rows = 9
    #     self.cols = 9
    #     self.width = 1000
    #     self.height = 800
    #     self.margin = 50
    #     self.gridWidth  = self.width - 2*self.margin
    #     self.gridHeight = self.height - 2*self.margin
    #     self.cellWidth = self.gridWidth / self.cols
    #     self.cellHeight = self.gridHeight / self.rows
    
    # These are my own drawings!
    # def playerPics(self):
    #     self.playerFront = self.loadImage('graphics/player/playerFront.png')
    #     self.playerFront = self.scaleImage(self.playerFront, 0.07)

    #     self.playerBack = self.loadImage('graphics/player/playerBack.png')
    #     self.playerBack = self.scaleImage(self.playerBack, 0.07)

    #     self.playerLeft = self.loadImage('graphics/player/playerLeft.png')
    #     self.playerLeft = self.scaleImage(self.playerLeft, 0.07)

    #     self.playerRight = self.loadImage('graphics/player/playerRight.png')
    #     self.playerRight = self.scaleImage(self.playerRight, 0.07)

    # def isValidRowCol(self, rows, cols, drow, dcol): 
    #     if self.row + drow < 0 or self.row + drow > rows - 1:
    #         return False
    #     if self.col + dcol < 0 or self.col + dcol> cols - 1:
    #         return False
    #     if (self.row + drow, self.col + dcol) not in self.dfsGraph[(self.row, self.col)]:
    #         return False
    #     else:
    #         return True

    # def getValidCellBounds(self, row, col):
    #     x0 = self.margin + col * self.cellWidth
    #     x1 = self.margin + (col + 1) * self.cellWidth
    #     y0 = self.margin + row * self.cellHeight
    #     y1 = self.margin + (row + 1) * self.cellHeight
    #     cx = (x1- x0)/2 + self.margin + self.wallThick
    #     cy = (y1 - y0)/2 + self.margin + self.wallThick

    # def keyPressed(self, event): # playerPositionUpdate
    #     if self.gameOver == False: 
    #         if event.key == 'Left':
    #             if self.isValidRowCol(rows = 9, cols = 9, -1, 0):
    #                 self.playerLocation(-1,0)
    #                 self.playerImage = self.playerLeft
    #         elif event.key == 'Right':
    #             self.playerLocation(+1,0)
    #             self.playerImage = self.playerRight
    #         elif event.key == 'Up':
    #             self.playerLocation(0, -1)
    #             self.playerImage = self.playerBack
    #         elif event.key == 'Down':
    #             self.playerLocation(0, +1)
    #             self.playerImage = self.playerFront

    # def isValidMovement(self):
    #     # stays on board
    #     if self.cx <= self.margin + self.wallThick \
    #         or self.cx > self.Width - self.margin - self.wallThick:
    #         return False
    #     if self.cy < self.margin + self.wallThick \
    #         or self.cy > self.Width - self.margin - self.wallThick:
    #         return False
    #     # doesn't collide with the walls. ## The DFS maze walls
    #     # wall color
    #     if (self.cx, self.cy) 


    # def playerMovement(self, row, col):


    #     # if self.cx or self.cy in 


    #     # doesn't collide with the soft blocks

    # def consumeItems(self):
    #     return 42