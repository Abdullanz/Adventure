# ###############################################################################
# #  Description: Luna game with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 4 March, 2020
# #  Version: 0.1
# ###############################################################################
## NOTE: Experiment with tile maps seems fun!!

import pygame
import pytmx #Library for tiled maps
pygame.init()

#Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# Assigning values to X and Y variable
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#Screen size
Screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT),pygame.FULLSCREEN)
#Controls
Keys = pygame.key.get_pressed()
MOUSE = pygame.mouse.get_pos()


#Buttons -> Add the photos to images file
#Config_Button = [pygame.image.load(r"C:\Users\Config.png"),
#                    pygame.image.load(r"C:\Users\Config_Over.png")]
#Play_Button = [pygame.image.load(r"C:\Users\Play.png"),
#                pygame.image.load(r"C:\Users\Play_Over.png")]
#Exit_Button = [pygame.image.load(r"C:\Users\Exit.png"),
#                pygame.image.load(r"C:\Users\Exit_Over.png")]


# Set window name & font -> Change font
pygame.display.set_caption('Luna')
font = pygame.font.Font('freesansbold.ttf', 32)

# A text suface object, on which text is drawn on it.
text = font.render('Luna', True, green, blue)

# Create a rectangular object for the text surface object
textRect = text.get_rect()
textRect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)


#


# Infinite loop of the game -> Add buttons behaviors and mouse controls
while True:
    Screen.fill(white)

    # Copying the text surface object to the display surface object at the center coordinate.
    Screen.blit(text, textRect)

    # Iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT then quitting the pygame and program.
        if event.type == pygame.QUIT:
            # deactivates pygame library
            pygame.quit()
            quit()
        # Draws the surface object to the screen.
        pygame.display.update()
