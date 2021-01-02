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


class bordered_rect:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render_shape(self):

        border_px = 3

        # Draw Blue Rect Bottom
        blue_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(lnk.window, lnk.main_blue, blue_rect)

        # Draw Grey Rect Top
        grey_rect = pygame.Rect((self.x + border_px),
                                (self.y + border_px),
                                (self.width - (border_px * 2)),
                                (self.height - (border_px * 2)))

        pygame.draw.rect(lnk.window, lnk.background_colour, grey_rect)


# ----------------------------------------------------------------------------------------------------------------------


# Draw The Box That Will Store The User's Input
def draw_boxes():

    # Draw Box That Will Show Question
    bordered_rect(109, 200, 280, 100).render_shape()

    # Draw Box That Will Cover Stroke On Top Box; For Style
    masking_rect = pygame.Rect(163, 185, 173, 25)
    pygame.draw.rect(lnk.window, lnk.background_colour, masking_rect)

    # Draw Box That Will Store Answer
    bordered_rect(109, 350, 111, 40).render_shape()

    # Draw Box That Will Store Button
    bordered_rect(279, 350, 111, 40).render_shape()


# Draw Title Screen
def draw_text():

    # Draw Backing Rectangle For Title | Remember [X, Y, Width, Height]
    pygame.draw.rect(lnk.window, lnk.main_blue, lnk.title_rect)

    # Draw Title Ontop Of Rectangle For Title | Remember [X, Y] Y May Vary Due To Height
    title_text = "Math 101"
    title_render = lnk.title_font.render(title_text, True, lnk.background_colour)
    lnk.window.blit(title_render, (40, 35))

    # Draw SubTitle 1 Below Title
    subtitle_text_1 = "A simple test of your math skills"
    subtitle_text_1_render = lnk.subtitle_font.render(subtitle_text_1, True, lnk.darker_grey)
    lnk.window.blit(subtitle_text_1_render, (36, 105))

    # Draw SubTitle 2 Below Title
    subtitle_text_1 = "Tests are randomly generated"
    subtitle_text_1_render = lnk.subtitle_font.render(subtitle_text_1, True, lnk.darker_grey)
    lnk.window.blit(subtitle_text_1_render, (36, 125))

    # Draw Current Date
    curdate_render = lnk.usr_inp_font.render(lnk.cur_date, True, lnk.darker_grey)
    lnk.window.blit(curdate_render, (390, 35))

    # Draw Current Question Number
    question_title = "Question {}.".format(lnk.question_num)
    question_title_render = lnk.subtitle_font.render(question_title, True, lnk.darker_grey)
    lnk.window.blit(question_title_render, (210, 190))


# ----------------------------------------------------------------------------------------------------------------------


# Draw Entire UI Contains Other Elements
def draw_ui():

    # Fill Background Window
    lnk.window.fill(lnk.background_colour)

    # Draw Input Box
    draw_boxes()

    # Draw Title Screen
    draw_text()





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
