# Relic
# By: Darin Fontes
# Started: 02/13/14
# v1 Finished: ?

import os
import sys
import time

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

# Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

CLR_BG = BLACK
CLR_MSG = WHITE


# -----
# Main
# -----


def main():
    # Init pygame
    pygame.init()

    # Set up global variables
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
    BASICFONT = pygame.font.Font(os.path.join('..', 'data', 'font', 'freesansbold.ttf '), 30)

    # Set window caption
    pygame.display.set_caption('Relic')

    # Main Loop
    while True:
        showstartscreen()
        rungame()
        showgameoverscreen()


def showstartscreen():
    """
    Display the start screen until the player presses a key.
    Then the user can select to either start a new game or load a game.
    """
    startimg = pygame.image.load(os.path.join('..', 'data', 'image', 'start_screen.jpg'))
    startimg = pygame.transform.smoothscale(startimg, (WINDOWWIDTH, WINDOWHEIGTH))
    startrect = startimg.get_rect()

    # Show the "Press any key" flashing text
    alphaval = 0
    fadespeed = 5
    isadd = True
    keypressed = False
    while True:
        # Check for keypress
        checkforquit()
        for event in pygame.event.get():
            if event.type in (MOUSEBUTTONUP, KEYUP):
                keypressed = True
        if keypressed:
            break

        # Adjust fade
        if isadd:
            alphaval += fadespeed
            if alphaval > 255:
                alphaval = 255
                isadd = False
        else:
            alphaval -= fadespeed
            if alphaval < 0:
                alphaval = 0
                isadd = True

        text = "Press any key..."
        textsurf = BASICFONT.render(text, True, (255, 255, 255))

        alphasurf = pygame.Surface(BASICFONT.size(text))
        alpharect = alphasurf.get_rect()
        alpharect.centerx = WINDOWWIDTH/2  # TODO change this to a constant (for buttons too)
        alpharect.centery = WINDOWWIDTH/2
        alphasurf.blit(textsurf, (0, 0))
        alphasurf.set_alpha(alphaval)

        DISPLAYSURF.fill(CLR_BG)
        DISPLAYSURF.blit(startimg, startrect)
        DISPLAYSURF.blit(alphasurf, alpharect)
        updatescreen()

    # Show the buttons
    while True:
        checkforquit()

        newgamesurf, newgamerect = maketext('New Game', CLR_MSG, CLR_BG, WINDOWWIDTH/2, WINDOWWIDTH/2)
        loadgamesurf, loadgamerect = maketext('Load Game', CLR_MSG, CLR_BG, WINDOWWIDTH/2, WINDOWWIDTH/2 + 40)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if newgamerect.collidepoint(event.pos):
                    startnewgame()
                elif loadgamerect.collidepoint(event.pos):
                    loadgame()

        DISPLAYSURF.fill(CLR_BG)
        DISPLAYSURF.blit(startimg, startrect)
        DISPLAYSURF.blit(newgamesurf, newgamerect)
        DISPLAYSURF.blit(loadgamesurf, loadgamerect)
        updatescreen()


def rungame():
    """
    The main game loop that runs the game logic
    """
    while True:
        checkforquit()

        # ...

        updatescreen()


def showgameoverscreen():
    """
    Shows the game over screen
    """
    pass  # Finish


def startnewgame():
    # TODO Do real things
    surf, rect = maketext("New Game button was pressed", CLR_MSG, CLR_BG, WINDOWWIDTH/2, WINDOWHEIGTH/2)
    DISPLAYSURF.fill(CLR_BG)
    DISPLAYSURF.blit(surf, rect)
    pygame.display.update()
    time.sleep(1)


def loadgame():
    # TODO Do real things
    surf, rect = maketext("Load Game button was pressed", CLR_MSG, CLR_BG, WINDOWWIDTH/2, WINDOWHEIGTH/2)
    DISPLAYSURF.fill(CLR_BG)
    DISPLAYSURF.blit(surf, rect)
    pygame.display.update()
    time.sleep(1)

# --------
# Methods
# --------


def terminate():
    """
    Terminates the program.
    """
    pygame.quit()
    sys.exit()


def checkforquit():
    """
    Checks for quit.
    """
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def updatescreen():
    """
    Updates the screen.
    """
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def maketext(text, color, bgcolor, centerx, centery):
        """
        Create the Surface and Rect objects for some text.
        """
        textsurf = BASICFONT.render(text, True, color, bgcolor)
        textrect = textsurf.get_rect()
        textrect.centerx = centerx
        textrect.centery = centery
        return (textsurf, textrect)


# -------------------------
if __name__ == '__main__':
    main()
