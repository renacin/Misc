# Name:                                            Renacin Matadeen
# Date:                                               12/27/2020
# Title                                           Classes For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

import Data.config
# ----------------------------------------------------------------------------------------------------------------------


class Button():

    #colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (0, 0, 0)
    width = 180
    height = 70



    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text



    def draw_button(self):
        # State Of Button  | True If Clicked
        action = False

        #define colours
        bg = (204, 102, 0)
        red = (255, 0, 0)
        black = (0, 0, 0)
        white = (255, 255, 255)

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                Data.config.clicked = True
                pygame.draw.rect(Data.config.screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and Data.config.clicked == True:
                Data.config.clicked = False
                action = True
                
            else:
                pygame.draw.rect(Data.config.screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(Data.config.screen, self.button_col, button_rect)

        #add text to button
        text_img = Data.config.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        Data.config.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

        return action
