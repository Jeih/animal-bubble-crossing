from cmu_112_graphics import *
from tkinter import *
import random
from class_maze import *
from class_movement import *
from class_minions import *

class fruits:
    def __init__(self):
        self.numberOfApples = 4
        self.numberOfOranges = 4
        self.rows = 16
        self.appleLocations = []
        self.orangeLocations = []
        self.appleCxCys = []
        self.orangeCxCys = []
        self.width = 790
        self.height = 790
        self.rows = 9
        self.cols = 9
        self.margin = 50
        self.gridWidth  = self.width - 2*self.margin
        self.gridHeight = self.height - 2*self.margin
        self.cellWidth = self.gridWidth / self.cols
        self.cellHeight = self.gridHeight / self.rows

    def appleLocation(self):
        appleCount = 0
        while appleCount < 7:
            row = random.randint(0,8)
            col = random.randint(0,8)
            if (row, col) != (0, 0):
                if (row, col) not in self.appleLocations:
                    self.appleLocations.append((row, col))
                    appleCount += 1

    def orangeLocation(self):
        orangeCount = 0
        while orangeCount < 7:
            row = random.randint(0,8)
            col = random.randint(0,8)
            if ((row, col) not in self.appleLocations) and \
            ((row, col) not in self.orangeLocations):
                self.orangeLocations.append((row, col))
                orangeCount += 1

    def getApplePositions(self):
        for appleLoc in self.appleLocations:
            appleRow = appleLoc[0]
            appleCol = appleLoc[1]

            appleX0 = self.margin + appleCol * self.cellWidth
            appleX1 = self.margin + (appleCol+1) * self.cellWidth
            appleY0 = self.margin + appleRow * self.cellHeight
            appleY1 = self.margin + (appleRow+1) * self.cellHeight
            appleCx = (appleX1 + appleX0)/2 
            appleCy = (appleY1 + appleY0)/2 

            self.appleCxCys.append((appleCx, appleCy))

    def getOrangePositions(self):
        for orangeLoc in self.orangeLocations:
            orangeRow = orangeLoc[0]
            orangeCol = orangeLoc[1]

            orangeX0 = self.margin + orangeCol * self.cellWidth
            orangeX1 = self.margin + (orangeCol+1) * self.cellWidth
            orangeY0 = self.margin + orangeRow * self.cellHeight
            orangeY1 = self.margin + (orangeRow+1) * self.cellHeight
            orangeCx = (orangeX1 + orangeX0)/2
            orangeCy = (orangeY1 + orangeY0)/2

            self.orangeCxCys.append((orangeCx, orangeCy))

    # fruit images are 500 X 500 pixcels
    # gif image displaying inspired by
    # ### from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html

    # def redrawAll(app, canvas):
    #     appleImage = app.spriteAppleImages[app.spriteAppleCounter]
    #     canvas.create_image(200, 200, image=appleImage)
    
    #     orangeImage = app.spriteOrangeImages[app.spriteOrangeCounter]
    #     canvas.create_image(200, 200, image=orangeImage)






    # # https://giphy.com/stickers/animal-crossing-acnh-fruits-ls5BnrrJpDYZ1XurI3
    #     self.apple = self.loadImage('graphics/items/apple.gif')
    #     self.appleStrip = self.scaleImage(self.apple, 0.06)
    #     self.appleSprites = [ ]
    #     for i in range(36): # there are 36 total apple images in apple.gif
    #         apple = self.appleStrip.crop((500 * i, 500, 500 *i , 500)) 
    #         self.appleSprites.append(apple)
    #     self.appleCounter = 0

    # #https://giphy.com/stickers/happy-color-orange-H83ZXrgTKq2eCrFrTE
    #     self.orange = self.loadImage('graphics/items/orange.gif')
    #     self.orangeStrip = self.scaleImage(self.orange, 0.06)
    #     # should i modify the scale after i crop the images?
    #     self.orangeSprites = [ ]
    #     for i in range(2): # there are 2 total orange pics in orange.gif
    #         orange = self.orangeStrip.crop((500 * i, 500, 500 *i , 500)) 
    #         self.orangeSprites.append(orange)
    #     self.orangeCounter = 0

    # def timerFired(self):
    #     self.appleCounter = (1 + self.applecounter) % len(self.appleSprites)
    #     self.orangeCounter = (1 + self.orangecounter) % len(self.orangeSprites)
        