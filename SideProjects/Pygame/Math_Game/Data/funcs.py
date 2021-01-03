# Name:                                            Renacin Matadeen
# Date:                                               12/28/2020
# Title                                          Functions For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys, random

import pygame
from pygame.locals import *

import Data.config as lnk
# ----------------------------------------------------------------------------------------------------------------------


# Create A Random Math Question Everytime This Function Is Called, Needs To Return Numbers, And Operators
def create_question():

    # Choose An Operator
    operator = random.choice(["+", "-", "/", "*"])
    int1 = random.randint(1, 99)
    int2 = random.randint(1, 99)

    # Find Answer
    pred_answer = int(eval("{} {} {}".format(int1, operator, int2)))

    # Overite Global Cur Question
    return [int1, operator, int2, pred_answer]


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











"""

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

"""
