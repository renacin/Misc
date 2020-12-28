# Name:                                            Renacin Matadeen
# Date:                                               12/28/2020
# Title                                          Functions For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys

import pygame
from pygame.locals import *

import Data.config as lnk
# ----------------------------------------------------------------------------------------------------------------------


# Draw Title Screen
def draw_title_card():

    # Draw Backing Rectangle (X, Y, Width, Height)
    title_rect = pygame.Rect(270, 60, 400, 100)
    title_rect_colour = (255, 255, 255)
    pygame.draw.rect(lnk.window, title_rect_colour, title_rect)

    # Title Font
    titlef_path = "Data/Title_BoldOblique.ttf"
    title_font = pygame.font.Font(titlef_path, 60)

    # Game Title
    title_text = "0 - 10 GAME"
    title_render = title_font.render(title_text, True, (0, 0, 0))
    lnk.window.blit(title_render, (300, 70)) #[X, Y]


# Check Events & Adjust Accordingly
def check_events(events):
    for event in events:

        # Quit If Exit Button Pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Quit If Escape Button Pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
