# ###############################################################################
# #  Description: Luna game with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 4 March, 2020
# #  Version: 0.1
# ###############################################################################
## NOTE: Experiment with tile maps seems fun!!

import pygame as pg
import os
from options import options
from Player import Player
from pytmx import load_pygame #Library for tiled maps


class source_code(object):

   def __init__(self):
      pg.init()
      pg.mixer.init()

    #Colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    Screen_size = (800, 600)

    Screen = pg.display.set_mode(Screen_size,pg.FULLSCREEN)



    #Buttons -> Add the photos to images file
    #Config_Button = [pygame.image.load(r"C:\Users\Config.png"),
    #                    pygame.image.load(r"C:\Users\Config_Over.png")]
    #Play_Button = [pygame.image.load(r"C:\Users\Play.png"),
    #                pygame.image.load(r"C:\Users\Play_Over.png")]
    #Exit_Button = [pygame.image.load(r"C:\Users\Exit.png"),
    #                pygame.image.load(r"C:\Users\Exit_Over.png")]


    # Set window name & font -> Change font
    pg.display.set_caption('Luna')
    font = pg.font.Font('freesansbold.ttf', 32)


    # Maybe use as text bubble/ front page?
    # A text suface object, on which text is drawn on it.
    #text = font.render('Luna', True, green, blue)
    # Create a rectangular object for the text surface object
    #textRect = text.get_rect()
    #textRect.center = (800 // 2, 600 // 2)


    # Copying the text surface object to the display surface object at the center coordinate.
    #    Screen.blit(text, textRect)

    # Iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pg.event.get():
        # if event object type is QUIT then quitting the pygame and program.
        if event.type == pg.QUIT:
            # deactivates pygame library
            pg.quit()
            quit()
            # Draws the surface object to the screen.
            pg.display.update()
