# ###############################################################################
# #  Description: Interactive fiction experiment with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 25 November, 2019
# ###############################################################################
# import pygame module in this program
import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
winWidth = 800
winLength = 800

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((winWidth, winLength ))

# set window name
pygame.display.set_caption('Interactive fiction')
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text suface object,
# on which text is drawn on it.
text = font.render('Luna', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()
textRect.center = (winWidth // 2, winLength // 2)

# infinite loop
while True:
    display_surface.fill(white)

    # copying the text surface object to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT then quitting the pygame and program.
        if event.type == pygame.QUIT:
            # deactivates pygame library
            pygame.quit()
            quit()
        # Draws the surface object to the screen.
        pygame.display.update()
        
#A method to quit the game
# def quitgame():
#     pygame.quit()
#     quit()
#
# quitgame()
