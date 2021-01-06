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
    operator = random.choice(["+", "-", "*"])
    int1 = random.randint(1, 99)
    int2 = random.randint(1, 99)

    # Find Answer
    pred_answer = int(eval("{} {} {}".format(int1, operator, int2)))

    # Overite Global Cur Question
    return [int1, operator, int2, pred_answer]


# See If The Users Input Is Valid
def check_user_input():

    # See If Input Can Be Converted To An INT
    try:
        input_int = int(lnk.usr_answer)
        lnk.input_bool = True

    except:
        lnk.input_bool = False

    # Change Input Colour Based On Input Value
    if (lnk.input_bool == True):
        lnk.usr_answer_colour = lnk.darker_grey

    else:
        # Draw Warning Message
        lnk.input_message_state = True


# If User Presses A Button On The Keyboard | For Input
def game_logic():

    # If User Clicked The Sumbit Button
    if lnk.submit_button_clicked == True:
        pygame.time.delay(100)

        # Check To See If Anser Was Correct
        try:
            if (int(lnk.usr_answer) == int(lnk.terms[3])):
                answer_bool = True
                lnk.answer_state = "Correct!"
                lnk.question_state = False
                lnk.usr_score += 1

            else:
                answer_bool = False
                lnk.answer_state = "False"
                lnk.question_state = False

        except ValueError:
            answer_bool = False
            lnk.answer_state = "False"
            lnk.question_state = False

        # Update Other Game Stats
        lnk.question_num += 1
        lnk.submit_button_clicked = False
        lnk.submit_button_hover = False



# ----------------------------------------------------------------------------------------------------------------------

# Check Events & Adjust Accordingly
def check_events(events):

    # Check For Events
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

            # If User Presses A Button | For Value Input
            elif event.key == K_BACKSPACE:
                lnk.usr_answer = lnk.usr_answer[:-1]

            elif (len(str(lnk.usr_answer)) <= len(str(lnk.terms[3]))):
                lnk.usr_answer += event.unicode
                check_user_input()

    # Run Main Game Logic
    game_logic()
