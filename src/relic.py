# Relic
# By: Darin Fontes
# Started: 02/13/14
# v1 Finished: ?

import pygame, random, sys
from pygame.locals import *

#-----------
# Constants
#-----------

# Frames per second
FPS = 30

# Window parameters
WINDOWWIDTH = 1200
WINDOWHEIGTH = 700

#------
# Main
#------

def main():
    # Init pygame
    pygame.init()

    # Set up global variables
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
    BASICFONT = pygame.font.Font('freesansbold.ttf ', 18)

    # Set window caption
    pygame.display.set_caption('Relic')

    # Game Loop
    while True:
        showStartScreen()
        runGame()
        showGameOverScreen()

# The main game loop that runs the game logic
def runGame():
    while True:
        checkForQuit()

        # ...
        # Update display
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#---------
# Methods
#---------

# Terminates the program
def terminate():
    pygame.quit()
    sys.exit()


# Checks for quit
def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.post(event)


# Shows the start screen
def showStartScreen():
    pass # Finish


# Shows the game over screen
def showGameOverScreen():
    pass # Finish

#--------------------------
if __name__ == '__main__':
    main()
