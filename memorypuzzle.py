import random, pygame, sys
from pygame.locals import *

FPS=30  #Frames per second
WINDOWHEIGHT=640 #Height of  window in pixels
WINDOWWIDTH=480 #Width of  window in pixels
REVEALSPEED=8 #Speed box reveals & covers
BOXSIZE=40 #height&width of each square box
GAPSIZE=10 #pixels between boxes
BOARDWIDTH=2 #Number of columns of boxes
BOARDHEIGHT=2 #Number of rows of boxes
assert(BOARDWIDTH*BOARDHEIGHT)%2 == 0, 'BOARD MUST HAVE AN EVEN NUMBER OF TILES'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR=NAVYBLUE
LIGHTBGCOLOR=GRAY
BOXCOLOR=WHITE
HIGHLIGHTCOLOR=BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS)*len(ALLSHAPES)*2 >= BOARDWIDTH*BOARDHEIGHT, "Too many boxes for shapes/colours"

def main():
    # Main program code goes here
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Coderdojo Memory  Game')
    
    mainBoard = []
    mainBoard.append( [ (DONUT,RED),(DONUT,RED) ] )
    mainBoard.append( [ (SQUARE,GREEN),(SQUARE,GREEN) ])
    revealedBoxes = []
    revealedBoxes.append( [False, False] )
    revealedBoxes.append( [False, False] )
    
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update()
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()