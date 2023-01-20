#################################################
# Your name: Jei Park
# Your andrew id: Jehyop
#################################################

from cmu_112_graphics import *
from tkinter import *
import random
from class_maze import *
from class_movement import *
from class_player import *
from class_minions import *
from class_items import *
from class_minions import *

class Player(object):
    def __init__(self):
        self.isTrapped = False
        self.isDead = False

def appStarted(app):
    app.playerLoseGameOver = False
    app.playerWinGameOver = False
    app.timerDelay = 100
    (app.rows, app.cols, app.cellSize, app.margin) = gameDimensions()
    app.balloonTimePassed = 0 # keeps track of how much time has passed since last reset
    app.minionTimePassed = 0
    app.playerTimePassed = 0
    app.minion1Timer = 0
    app.maze = maze()
    app.mazeDFS = app.maze.dfs()
    app.mazeGraph = app.maze.graph
    app.gridWidth  = app.width - 2*app.margin
    app.gridHeight = app.height - 2*app.margin
    app.cellWidth = app.gridWidth // app.cols
    app.cellHeight = app.gridHeight // app.rows
    # player cx, cy location update
    app.cx = 88.0
    app.cy = 88.0
    (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)
    app.wallThick = 10

    ######## Balloon Image#########
    app.balloonCxCyList = []
    app.balloonImage = app.loadImage('graphics/balloons/bubble.png')
    app.balloonImage = app.scaleImage(app.balloonImage, 0.7)

    ############## Call Fruits ##############
    app.fruits = fruits()
    app.fruits.appleLocation()
    app.appleLocations = app.fruits.appleLocations

    app.fruits.orangeLocation()
    app.orangeLocations = app.fruits.orangeLocations

    ############ Apple Row Col #############
    app.apple1row = app.fruits.appleLocations[0][0]
    app.apple1col = app.fruits.appleLocations[0][1]

    app.apple2row = app.fruits.appleLocations[1][0]
    app.apple2col = app.fruits.appleLocations[1][1]

    app.apple3row = app.fruits.appleLocations[2][0]
    app.apple3col = app.fruits.appleLocations[2][1]

    app.apple4row = app.fruits.appleLocations[3][0]
    app.apple4col = app.fruits.appleLocations[3][1]

    app.apple5row = app.fruits.appleLocations[4][0]
    app.apple5col = app.fruits.appleLocations[4][1]

    app.apple6row = app.fruits.appleLocations[5][0]
    app.apple6col = app.fruits.appleLocations[5][1]

    app.apple7row = app.fruits.appleLocations[6][0]
    app.apple7col = app.fruits.appleLocations[6][1]

    ############ Orange Row Col #############
    app.orange1row = app.fruits.orangeLocations[0][0]
    app.orange1col = app.fruits.orangeLocations[0][1]

    app.orange2row = app.fruits.orangeLocations[1][0]
    app.orange2col = app.fruits.orangeLocations[1][1]

    app.orange3row = app.fruits.orangeLocations[2][0]
    app.orange3col = app.fruits.orangeLocations[2][1]

    app.orange4row = app.fruits.orangeLocations[3][0]
    app.orange4col = app.fruits.orangeLocations[3][1]

    app.orange5row = app.fruits.orangeLocations[4][0]
    app.orange5col = app.fruits.orangeLocations[4][1]

    app.orange6row = app.fruits.orangeLocations[5][0]
    app.orange6col = app.fruits.orangeLocations[5][1]

    app.orange7row = app.fruits.orangeLocations[6][0]
    app.orange7col = app.fruits.orangeLocations[6][1]

    ########## Call Fruit Cx Cy #############
    app.fruits.getApplePositions()
    app.appleCxCys = app.fruits.appleCxCys

    app.fruits.getOrangePositions()
    app.orangeCxCys = app.fruits.orangeCxCys

    if len(app.appleCxCys) == 0 and len(app.orangeCxCys) == 0:
        app.playerWinGameOver = True    

    ######### get Apple Cx Cy ###############
    app.apple1cx = app.fruits.appleCxCys[0][0]
    app.apple1cy = app.fruits.appleCxCys[0][1]

    app.apple2cx =  app.fruits.appleCxCys[1][0]
    app.apple2cy = app.fruits.appleCxCys[1][1]

    app.apple3cx =  app.fruits.appleCxCys[2][0]
    app.apple3cy = app.fruits.appleCxCys[2][1]

    app.apple4cx =  app.fruits.appleCxCys[3][0]
    app.apple4cy = app.fruits.appleCxCys[3][1]

    app.apple5cx =  app.fruits.appleCxCys[4][0]
    app.apple5cy = app.fruits.appleCxCys[4][1]

    app.apple6cx =  app.fruits.appleCxCys[5][0]
    app.apple6cy = app.fruits.appleCxCys[5][1]

    app.apple7cx =  app.fruits.appleCxCys[6][0]
    app.apple7cy = app.fruits.appleCxCys[6][1]

    ######### get Orange Cx Cy ###############

    app.orange1cx = app.fruits.orangeCxCys[0][0]
    app.orange1cy = app.fruits.orangeCxCys[0][1]

    app.orange2cx =  app.fruits.orangeCxCys[1][0]
    app.orange2cy = app.fruits.orangeCxCys[1][1]

    app.orange3cx =  app.fruits.orangeCxCys[2][0]
    app.orange3cy = app.fruits.orangeCxCys[2][1]

    app.orange4cx =  app.fruits.orangeCxCys[3][0]
    app.orange4cy = app.fruits.orangeCxCys[3][1]

    app.orange5cx =  app.fruits.orangeCxCys[4][0]
    app.orange5cy = app.fruits.orangeCxCys[4][1]

    app.orange6cx =  app.fruits.orangeCxCys[5][0]
    app.orange6cy = app.fruits.orangeCxCys[5][1]

    app.orange7cx =  app.fruits.orangeCxCys[6][0]
    app.orange7cy = app.fruits.orangeCxCys[6][1]

    ############## Call Minions##############
    app.minion1Dx = -5
    app.minion1Dy = -5
    app.minion2Dx = -5
    app.minion2Dy = -5
    app.minion3Dx = -5
    app.minion3Dy = -5
    app.minion4Dx = -5
    app.minion4Dy = -5

    app.minion = enemies()
    app.minion.minionLocation()
    app.minionLocations = app.minion.minionLocations
    app.minion.getMinionPositions()
    app.minionCxCys = app.minion.minionCxCys

    # """ minionCxCy getValidCellBounds listed below"""
    # app.minion1cx = app.minionCxCys[0][0]
    # app.minion1cy = app.minionCxCys[0][1]

    # app.minion2cx = app.minionCxCys[1][0]
    # app.minion2cy = app.minionCxCys[1][1]

    # app.minion3cx = app.minionCxCys[2][0]
    # app.minion3cy = app.minionCxCys[2][1]

    # app.minion4cx =  app.minionCxCys[3][0]
    # app.minion4cy =  app.minionCxCys[3][1]

    # app.minion5cx =  app.minionCxCys[4][0]
    # app.minion5cy =  app.minionCxCys[4][1]

    # app.minion6cx = app.minionCxCys[5][0]
    # app.minion6cy =  app.minionCxCys[5][1]

    # """ minionRowCol listed below"""
    # app.minion1row, app.minion1col = convertCxCyToRowCol(app,app.minion1cx, app.minion1cy)

    # app.minion2row, app.minion2col = convertCxCyToRowCol(app,app.minion2cx, app.minion2cy)

    # app.minion3row, app.minion3col = convertCxCyToRowCol(app,app.minion3cx, app.minion3cy)

    # app.minion4row, app.minion4col = convertCxCyToRowCol(app,app.minion4cx, app.minion4cy)

    # app.minion5row, app.minion5col = convertCxCyToRowCol(app,app.minion5cx, app.minion5cy)

    # app.minion6row,app.minion6col  =  convertCxCyToRowCol(app,app.minion6cx, app.minion6cy)

    """ """
    """ minionRowCol listed below"""
    app.minion1row = app.minionLocations[0][0]
    app.minion1col = app.minionLocations[0][1]

    app.minion2row = app.minionLocations[1][0]
    app.minion2col = app.minionLocations[1][1]

    app.minion3row = app.minionLocations[2][0]
    app.minion3col = app.minionLocations[2][1]

    app.minion4row = app.minionLocations[3][0]
    app.minion4col = app.minionLocations[3][1]

    app.minion5row = app.minionLocations[4][0]
    app.minion5col = app.minionLocations[4][1]

    app.minion6row = app.minionLocations[5][0]
    app.minion6col = app.minionLocations[5][1]

    """ minionCxCy getValidCellBounds listed below"""
    app.minion1cx = getValidCellBounds(app, app.minion1row, app.minion1col)[0]
    app.minion1cy = getValidCellBounds(app, app.minion1row, app.minion1col)[1]

    app.minion2cx = getValidCellBounds(app, app.minion2row, app.minion2col)[0]
    app.minion2cy =  getValidCellBounds(app, app.minion2row, app.minion2col)[1]

    app.minion3cx =  getValidCellBounds(app, app.minion3row, app.minion3col)[0]
    app.minion3cy =  getValidCellBounds(app, app.minion3row, app.minion3col)[1]

    app.minion4cx =  getValidCellBounds(app, app.minion4row, app.minion4col)[0]
    app.minion4cy =  getValidCellBounds(app, app.minion4row, app.minion4col)[1]

    app.minion5cx =  getValidCellBounds(app, app.minion5row, app.minion5col)[0]
    app.minion5cy =  getValidCellBounds(app, app.minion5row, app.minion5col)[1]

    app.minion6cx =  getValidCellBounds(app, app.minion6row, app.minion6col)[0]
    app.minion6cy =  getValidCellBounds(app, app.minion6row, app.minion6col)[1]

    app.movement = movement()
    """ minion DFS path is given below"""

    app.minion5path = app.movement.bfs(app.mazeGraph, (app.minion5row, app.minion5col), \
    (app.playerrow, app.playercol))

    app.minion6path = app.movement.bfs(app.mazeGraph, (app.minion6row, app.minion6col), \
    (app.playerrow, app.playercol))

    """background image"""
    # background image from https://elorapautrat.artstation.com/projects/3G69v
    app.background = app.loadImage('graphics/forestBackground1.png')
    app.background = app.scaleImage(app.background, 0.8)

    """ player Image"""
    # player images (I drew this)
    app.playerFront = app.loadImage('graphics/player/playerFront.png')
    app.playerFront = app.scaleImage(app.playerFront, 0.07)

    app.playerBack = app.loadImage('graphics/player/playerBack.png')
    app.playerBack = app.scaleImage(app.playerBack, 0.07)

    app.playerLeft = app.loadImage('graphics/player/playerLeft.png')
    app.playerLeft = app.scaleImage(app.playerLeft, 0.07)

    app.playerRight = app.loadImage('graphics/player/playerRight.png')
    app.playerRight = app.scaleImage(app.playerRight, 0.07)

    app.player = Player()
    app.playerImage = app.playerFront

    """ item fruit apple gif Image"""
    # inspired by https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
    # apple (or peach) image from https://giphy.com/stickers/peach-acnl-peche-L3pB45f3UnLAcOmVn1
    app.spriteAppleImages = loadAnimatedAppleGif('graphics/items/apple.gif')
    app.spriteAppleCounter = 0

    """ item fruit orange gif Image"""
    # orange image from https://giphy.com/stickers/happy-color-orange-H83ZXrgTKq2eCrFrTE
    app.spriteOrangeImages = loadAnimatedOrangeGif('graphics/items/orange.gif')
    app.spriteOrangeCounter = 0

    """ minion running bear gif Image"""
    # minion image from https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.timothee-lambrecq.com%2Fstills&psig=AOvVaw3GxfwP-7iFrsQokNpc_cfi&ust=1650936989421000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCNjFntmJrvcCFQAAAAAdAAAAABBj
    app.spriteMinionImages = loadAnimatedMinionGif('graphics/minion/minion.gif')
    app.spriteMinionCounter = 0

# load Animated Gif from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
def loadAnimatedAppleGif(path):
    spriteAppleImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spriteAppleImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spriteAppleImages

def loadAnimatedOrangeGif(path):
    spriteOrangeImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spriteOrangeImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spriteOrangeImages

def loadAnimatedMinionGif(path):
    # load first sprite outside of try/except to raise file-related exceptions
    spriteMinionImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spriteMinionImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spriteMinionImages

""" use isFruitCollision function in timerFired"""
def isFruitCollision(app, fruitCx, fruitCy):
    if (app.cx <= fruitCx + 25 and app.cx >= fruitCx -25) and \
        (app.cy <= fruitCy + 25 and app.cy >= fruitCy - 25):
        return True
    return False

# check this everytime the timer goes off:
def isBubbleCollision(app, cx, cy):
    """ player is near the bubble"""
    # balloon is left side
    for (bubbleCx, bubbleCy) in app.balloonCxCyList:
        if (bubbleCx <= cx <= bubbleCx + app.cellWidth + 15)\
            and (bubbleCy - app.cellHeight // 2 <= cy <= bubbleCy + app.cellHeight // 2):
            return True
        # balloon is right side
        if (bubbleCx - app.cellWidth - 15 <= cx <= bubbleCx) \
            and (bubbleCy - app.cellHeight // 2 <= cy <= bubbleCy + app.cellHeight // 2):
            return True
        # balloon is up side
        if (bubbleCx - app.cellHeight // 2 <= cx <= bubbleCx + app.cellHeight // 2) \
            and ((bubbleCy <= cy <= bubbleCy + app.cellHeight + 15)):
            return True
        # balloon is down side
        if (bubbleCx - app.cellHeight // 2 <= cx <= bubbleCx + app.cellHeight // 2) \
            and ((bubbleCy - app.cellHeight - 15 <= cy <= bubbleCy)):
            return True
    return False

""" this is the timer fired section """
def timerFired(app):
    """ Balloon Set"""
    app.balloonTimePassed += app.timerDelay
    if app.balloonTimePassed == 1000:
        if len(app.balloonCxCyList) > 0:
            app.balloonCxCyList.pop(0)

    """ GIF images Moving Function  """
    app.spriteMinionCounter = (1 + app.spriteMinionCounter) % len(app.spriteMinionImages)
    app.spriteAppleCounter = (1 + app.spriteAppleCounter) % len(app.spriteAppleImages)
    app.spriteOrangeCounter = (1 + app.spriteOrangeCounter) % len(app.spriteOrangeImages)

    """ constantly update the list of remaining Apples"""
    remainingApples = []
    for (appleCx, appleCy) in app.appleCxCys:
        if isFruitCollision(app, appleCx, appleCy) != True:
            remainingApples.append((appleCx, appleCy))
    app.appleCxCys = remainingApples

    """ constantly updating the list of remaining minions"""
    # app.minionTimePassed += app.timerDelay
    if (app.balloonTimePassed >= 900):
        for (minionCx, minionCy) in app.minionCxCys:
            if isBubbleCollision(app, minionCx, minionCy) == True:
                app.minionCxCys.remove((minionCx, minionCy))

    """ constantly update the list of remaining Oranges"""
    remainingOranges = []
    for (orangeCx, orangeCy) in app.orangeCxCys:
        if isFruitCollision(app, orangeCx, orangeCy) != True:
            remainingOranges.append((orangeCx, orangeCy))
    app.orangeCxCys = remainingOranges

    """ constantly update the player's row col location"""
    (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)
    app.minion5path = app.movement.bfs(app.mazeGraph, (app.minion5row, app.minion5col), \
    (app.playerrow, app.playercol))
    app.minion6path = app.movement.bfs(app.mazeGraph, (app.minion6row, app.minion6col), \
    (app.playerrow, app.playercol))

    # minion 1 + movement inspired by the pong game https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    """ minion 1 movement"""
    app.minion1cx += app.minion1Dx
    if isRightWalls(app, app.minion1cx + app.minion1Dx, app.minion1cy):
        app.minion1Dx = - app.minion1Dx
    elif isLeftWalls(app, app.minion1cx - app.minion1Dx, app.minion1cy) \
        or app.minion1cx - app.minion1Dx < app.margin + 20:
        app.minion1Dx = app.minion1Dx

    """ minion 5, 6 movement"""
    app.minionTimePassed += app.timerDelay
    if (app.minionTimePassed >= 1300):
        if len(app.minionCxCys) > 2:
            currentMinion5RowCol = app.minion5path[1]
            currentMinion6RowCol = app.minion6path[1]
            app.minion5row = currentMinion5RowCol[0]
            app.minion5col = currentMinion5RowCol[1]
            app.minion6row = currentMinion6RowCol[0]
            app.minion6col = currentMinion6RowCol[1]
            app.minionCxCys[-2] = getValidCellBounds(app, app.minion5row, app.minion5col)
            app.minionCxCys[-1] = getValidCellBounds(app, app.minion6row, app.minion6col)
            if len(app.minion5path)>2:
                app.minion5path.pop(0)
            if len(app.minion6path)>2:
                app.minion6path.pop(0)
            app.minionTimePassed = 0

def gameDimensions():
    (rows, cols, cellSize, margin) = (9, 9, 15, 50)
    return (rows, cols, cellSize, margin)

def getLeftWallBounds(app, row, col):
    x0 = app.margin + col * app.cellWidth
    x1 = app.margin + (col + 1) * app.cellWidth
    y0 = app.margin + row * app.cellHeight
    y1 = app.margin + (row + 1) * app.cellHeight
    left = (x0, y0, x0, y1)
    return left

def getRightWallBounds(app, row, col):
    x0 = app.margin + col * app.cellWidth
    x1 = app.margin + (col + 1) * app.cellWidth
    y0 = app.margin + row * app.cellHeight
    y1 = app.margin + (row + 1) * app.cellHeight
    right = (x1, y0, x1, y1 )
    return right

def getUpWallBounds(app, row, col):
    x0 = app.margin + col * app.cellWidth
    x1 = app.margin + (col + 1) * app.cellWidth
    y0 = app.margin + row * app.cellHeight
    y1 = app.margin + (row + 1) * app.cellHeight
    up = (x0, y0, x1, y0)
    return up

def getDownWallBounds(app, row, col):
    x0 = app.margin + col * app.cellWidth
    x1 = app.margin + (col + 1) * app.cellWidth
    y0 = app.margin + row * app.cellHeight
    y1 = app.margin + (row + 1) * app.cellHeight
    down = (x0, y1, x1, y1)
    return down

def isInBounds(app, row, col):
    if ((row >= 0 and row < app.rows) and
        (col >= 0 and col < app.cols)):
        return True

def convertCxCyToRowCol(app, cx, cy):
    row = int((cy - app.margin)) // app.cellHeight
    col = int((cx - app.margin)) // app.cellWidth
    return (row, col)

def isLeftWalls(app, cx, cy):
    for row in range(app.rows):
        for col in range(app.cols):
        # left Wall
            if (row, col -1) not in app.mazeGraph[(row, col)] and isInBounds:
                leftWallBounds = getLeftWallBounds(app, row, col)
                leftWallCx =  (leftWallBounds[0] + leftWallBounds[2])/2
                leftWallCy = (leftWallBounds[1] + leftWallBounds[3]) /2
                if (cx - 20 < leftWallCx + 25 and cx - 20 > leftWallCx - 20) and \
                (cy > leftWallCy - app.cellHeight//2 - 35 and cy < leftWallCy + app.cellHeight//2 + 10):
                    if cx > app.margin:
                        return True

def isRightWalls(app, cx, cy):
    # define the cx, cy's that the player cannot go
    for row in range(app.rows):
        for col in range(app.cols):
            # right Wall
            if (row, col + 1) not in app.mazeGraph[(row, col)] and isInBounds:
                rightWallBounds = getRightWallBounds(app, row, col)
                rightWallCx =  (rightWallBounds[0] + rightWallBounds[2])/2
                rightWallCy = (rightWallBounds[1] + rightWallBounds[3]) /2
                if (cx + 20 < rightWallCx + 5 and cx+ 13 > rightWallCx -30) and \
                (cy > rightWallCy - app.cellHeight//2 -25  and cy < rightWallCy + app.cellHeight//2 + 15):
                    return True

def isUpWalls(app, cx, cy):
            # up Wall
    for row in range(app.rows):
        for col in range(app.cols):
            if (row-1, col) not in app.mazeGraph[(row, col)] and isInBounds:
                upWallBounds = getUpWallBounds(app, row, col)
                upWallCx =  (upWallBounds[0] + upWallBounds[2])/2
                upWallCy = (upWallBounds[1] + upWallBounds[3]) /2
                if (cx > upWallCx - app.cellWidth/2 -10 and cx < upWallCx + app.cellWidth/2 + 20)\
                and (cy - 20 > upWallCy - 27 and cy - 20 < upWallCy + 15):
                    return True

def isDownWalls(app, cx, cy):
            # down Wall
    for row in range(app.rows):
        for col in range(app.cols):
            if (row + 1, col) not in app.mazeGraph[(row, col)] and isInBounds:
                downWallBounds = getDownWallBounds(app, row, col)
                downWallCx =  (downWallBounds[0] + downWallBounds[2])/2
                downWallCy = (downWallBounds[1] + downWallBounds[3]) /2
                if (cx > downWallCx - app.cellWidth//2 - 20 and cx < downWallCx + app.cellWidth//2 + 20) \
                and (cy + 20 > downWallCy -35 and cy + 20< downWallCy + 20):
                    return True

def isInBoard(app, dx, dy, cx, cy):
    if (cx + dx <= app.margin + 20) or \
    (cx + dx >= app.width - (app.margin)- (25)):
        return False
    if (cy + dy <= app.margin) or \
    (cy + dy >= app.height - (app.margin) - 40):
        return False
    else:
        return True

def keyPressed(app, event): # playerPositionUpdate
    if app.playerLoseGameOver or app.playerWinGameOver:
        return
    if app.playerWinGameOver == False and app.playerLoseGameOver == False:
        if event.key == 'Left':
            if isLeftWalls(app, app.cx, app.cy) != True:
                app.playerImage = app.playerLeft
                app.cx += -15
                # (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)

        elif event.key == 'Right':
            if isRightWalls(app, app.cx, app.cy) != True:
                app.playerImage = app.playerRight
                app.cx += 15
                # (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)
        elif event.key == 'Up':
            if isUpWalls(app, app.cx, app.cy) != True:
                app.playerImage = app.playerBack
                app.cy += -15
                # (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)
        elif event.key == 'Down':
            if isDownWalls(app, app.cx, app.cy) != True:
                app.playerImage = app.playerFront
                app.cy += 15
                # (app.playerrow, app.playercol) = convertCxCyToRowCol(app, app.cx, app.cy)
        elif event.key == "Space":
            if len(app.balloonCxCyList) <= 3:
                app.balloonCxCyList.append((app.cx, app.cy))
                app.balloonTimePassed = 0
    else:
        if event.key == 'r':
            appStarted(app)

def getValidCellBounds(app, row, col):
    x0 = app.margin + col * app.cellWidth
    x1 = app.margin + (col + 1) * app.cellWidth
    y0 = app.margin + row * app.cellHeight
    y1 = app.margin + (row + 1) * app.cellHeight
    cx = (x1 + x0)/2
    cy = (y1 + y0)/2
    return (cx, cy)

def drawCell(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            # left case
            if (row, col-1) not in app.mazeGraph[(row, col)] and isInBounds:
                canvas.create_line(getLeftWallBounds(app, row, col), width = 3)
            # right case
            if (row, col+1) not in app.mazeGraph[(row, col)] and isInBounds:
                canvas.create_line(getRightWallBounds(app, row, col), width = 3)
            # up case
            if (row-1, col) not in app.mazeGraph[(row, col)] and isInBounds:
                canvas.create_line(getUpWallBounds(app, row, col), width = 3)
            # down case
            if (row+1, col) not in app.mazeGraph[(row, col)] and isInBounds:
                canvas.create_line(getDownWallBounds(app, row, col), width = 3)

    """ the minion1 that moves left to right is just for display"""
def drawMinion1(app, canvas):
    minionImage = app.spriteMinionImages[app.spriteMinionCounter]
    canvas.create_image(app.minion1cx, app.minion1cy, image=minionImage)

def drawMinion(app, canvas):
    minionImage = app.spriteMinionImages[app.spriteMinionCounter]
    for (minionCx, minionCy) in app.minionCxCys:
        canvas.create_image(minionCx, minionCy, image=minionImage)

def drawBalloon(app, canvas):
    for (balloonCx, balloonCy) in app.balloonCxCyList:
        canvas.create_image(balloonCx, balloonCy, image = ImageTk.PhotoImage(app.balloonImage))

def drawApple(app, canvas):
    appleImage = app.spriteAppleImages[app.spriteAppleCounter]
    for (appleCx, appleCy) in app.appleCxCys:
        canvas.create_image(appleCx, appleCy, image = appleImage)

def drawOrange(app, canvas):
    orangeImage = app.spriteOrangeImages[app.spriteOrangeCounter]
    for (orangeCx, orangeCy) in app.orangeCxCys:
        canvas.create_image(orangeCx, orangeCy, image = orangeImage)

def drawPlayer(app, canvas):
    canvas.create_image(app.cx, app.cy, image = ImageTk.PhotoImage(app.playerImage))

def drawBackground(app, canvas):
    canvas.create_image(400, 400, image = ImageTk.PhotoImage(app.background))

# from https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
def drawPlayerWinGameOver(app, canvas):
    if app.playerWinGameOver == True:
        canvas.create_text(app.width/2, app.height/2, text='Player Win Game over!',
                           font='Arial 26 bold', fill='black')
# from https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
def drawPlayerLoseGameOver( app, canvas):
    if app.playerLoseGameOver == True:
        canvas.create_text(app.width/2, app.height/2, text='Player Lose Game over!',
                           font='Arial 26 bold', fill='black')

def redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawCell(app, canvas)
    drawMinion1(app, canvas)
    drawApple(app, canvas)
    drawOrange(app, canvas)
    drawMinion(app, canvas)
    drawBalloon(app, canvas)
    drawPlayer(app, canvas)
    drawPlayerWinGameOver(app, canvas)
    drawPlayerLoseGameOver( app, canvas)

# width = 790 hieght = 790
runApp(width=790, height=790)
