# ###############################################################################
# #  Description: Luna game with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 4 March, 2020
# #  Version: 0.1
# ###############################################################################
## NOTE: Experiment with tile maps seems fun!!

import pygame as pg
from pytmx import load_pygame #Library for tiled maps
pg.init()

#Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

Screen_size = (800, 600)

Screen = pg.display.set_mode(Screen_size,pg.FULLSCREEN)
#Controls
Keys = pg.key.get_pressed()
MOUSE = pg.mouse.get_pos()


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


#A function that sets up the tile map
def map_setup():
    global image

    #Importing the map
    tmxdata = load_pygame("Images/isometric_grass_and_water.tmx")
    width = tmxdata.width * tmxdata.tilewidth
    height = tmxdata.height * tmxdata.tileheight

    ti = tmxdata.get_tile_image_by_gid
    for layer in tmxdata.visible_layers:
        if isinstance(layer, TiledTileLayer):
            for x, y, gid, in layer:
                tile = ti(gid)
                if tile:
                    image = tmxdata.get_tile_image(0, 1, layer)

# Infinite loop of the game -> Add buttons behaviors and mouse controls
while True:
    Screen.fill(white)

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
