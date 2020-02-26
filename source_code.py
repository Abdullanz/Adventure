# ###############################################################################
# #  Description: Interactive fiction experiment with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 25 November, 2019
# ###############################################################################
from time import sleep
import pygame
import sys
import random

#initalize the game
pygame.init()

#Window display
display_width = 800
display_height = 600

#Colors used in the game
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 128)
bright_red = (255,0,0)
bright_green = (0,255,0)



#A method to quit the game
def quitgame():
    pygame.quit()
    quit()

quitgame()
