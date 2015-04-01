# Relic
# By: Darin Fontes
# Started: 02/13/14
# v1 Finished: ?

import sys

import pygame
from pygame.locals import *


# ----------
# Constants
# ----------

# Frames per second
FPS = 30

# Window parameters
WINDOWWIDTH = 1200
WINDOWHEIGTH = 700

# -----
# Main
# -----


def main():
    # Init pygame
    pygame.init()

    # Set up global variables
    global FPSCLOCK, DISPLAYSURF  # , BASICFONT
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
    # BASICFONT = pygame.font.Font('freesansbold.ttf ', 18)

    # Set window caption
    pygame.display.set_caption('Relic')

    # Game Loop
    while True:
        showstartscreen()
        rungame()
        showgameoverscreen()


# The main game loop that runs the game logic
def rungame():
    while True:
        checkforquit()

        # ...
        # Update display
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# --------
# Methods
# --------


# Terminates the program
def terminate():
    pygame.quit()
    sys.exit()


# Checks for quit
def checkforquit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.post(event)


# Shows the start screen
def showstartscreen():
    pass  # Finish


# Shows the game over screen
def showgameoverscreen():
    pass  # Finish

# -------------------------
if __name__ == '__main__':
    main()
