# ###############################################################################
# #  Description: Luna game with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 4 March, 2020
# #  Version: 0.1
# ###############################################################################
import pygame as pg
class Player():

    #Controls
    Keys = pg.key.get_pressed()
    MOUSE = pg.mouse.get_pos()

    # this is the move method within the player class
    def move(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change

    def get_pygame_events():
        pygame_events = pg.event.get()
        return pygame_events

    def get_keys_pressed(self):
        keys_pressed = get_pygame_events()  #pygame.event.get(pygame.KEYDOWN)
        # print(keys_pressed)
        keys_pressed_list = []
        for event in keys_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    keys_pressed_list.append("left")
                if event.key == K_RIGHT:
                    keys_pressed_list.append("right")
                if event.key == K_UP:
                    keys_pressed_list.append("up")
                if event.key == K_DOWN:
                    keys_pressed_list.append("down")
                if event.key == K_a:
                    keys_pressed_list.append("a")
                if  event.key == K_d:
                    keys_pressed_list.append("b")
                if event.key == K_w:
                    keys_pressed_list.append("w")
                if event.key == K_s:
                    keys_pressed_list.append("s")
                if event.key == K_SPACE:
                    keys_pressed_list.append("space")
                if event.key == K_q:
                    keys_pressed_list.append("q")
                if event.key == K_e:
                    keys_pressed_list.append("e")
            if event.type == pg.MOUSEBUTTONDOWN:
                keys_pressed_list.append("click")
                return (keys_pressed_list, event.pos)
        return keys_pressed_list
