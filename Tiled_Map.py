# ###############################################################################
# #  Description: The file to generate a tiled map that generates as long as the player moves
# #  Author: Abdullah Najjar
# #  Date: 6 March, 2020
# #  Version: 0.1
# ###############################################################################
from pytmx import load_pygame #Library for tiled maps


class Map(object):

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
