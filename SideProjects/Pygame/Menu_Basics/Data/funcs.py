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
    title_rect = pygame.Rect(270, 60, 520, 100)
    title_rect_colour = (255, 255, 255)
    pygame.draw.rect(lnk.window, title_rect_colour, title_rect)

    # Game Title
    title_text = "# GUESSING GAME"
    title_render = lnk.title_font.render(title_text, True, (0, 0, 0))
    lnk.window.blit(title_render, (300, 70)) #[X, Y]



# Draw The Box That Will Store The User's Input
def draw_input_and_box():

    # Draw Box That Will Store The Users Input
    input_rect = pygame.Rect(270, 500, 100, 100)
    input_rect_colour = (255, 255, 255)
    pygame.draw.rect(lnk.window, input_rect_colour, input_rect)


    # See If Input Can Be Converted To An INT
    try:
        input_int = int(lnk.user_input)
        lnk.input_bool = True

    except:
        lnk.input_bool = False

    # Change Input Colour Based On Input Value
    if (lnk.input_bool == True) & (len(lnk.user_input) <= 2):
        lnk.input_colour = (255, 255, 255)

    else:
        lnk.input_colour = (255, 0, 0)

    # Render Users Input
    usr_in_surf = lnk.usr_inp_font.render(lnk.user_input, True, lnk.input_colour)
    lnk.window.blit(usr_in_surf, (300, 800)) #[X, Y]



# ----------------------------------------------------------------------------------------------------------------------



# Draw Entire UI Contains Other Elements
def draw_ui():

    # Draw Title Screen
    draw_title_card()

    # Draw Input Box
    draw_input_and_box()



# ----------------------------------------------------------------------------------------------------------------------


# Check Events & Adjust Accordingly
def check_events(events):
    for event in events:

        # Quit If Exit Button Pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check If A Key On The Keyboard Was Pressed
        if event.type == KEYDOWN:

            # Quit If Escape Button Pressed
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Reset User_Input If Backspace Is Pressed
            if event.key == K_BACKSPACE:
                lnk.user_input = lnk.user_input[:-1]

            else:
                lnk.user_input += event.unicode
